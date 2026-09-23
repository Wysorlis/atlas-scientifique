"""Backlinks automatiques entre les documents Sphinx.

L'extension collecte les liens internes compris par Sphinx/MyST puis ajoute,
en bas de chaque document cible, la liste des documents qui pointent vers lui.
Les entrées de ``toctree`` ne sont volontairement pas considérées comme des
liens : seuls les liens placés dans le contenu d'une page créent un backlink.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable

from docutils import nodes
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment


BacklinkMap = dict[str, tuple[str, ...]]


def _collect_backlinks(app: Sphinx, env: BuildEnvironment) -> Iterable[str]:
    """Construit l'index inverse et demande la réécriture des pages modifiées."""
    collected: dict[str, set[str]] = defaultdict(set)

    for source_doc in env.found_docs:
        doctree = env.get_doctree(source_doc)

        for link in doctree.findall(addnodes.pending_xref):
            if link.get("refdomain") != "doc":
                continue

            target_doc = link.get("reftarget")
            if target_doc in env.found_docs and target_doc != source_doc:
                collected[target_doc].add(source_doc)

    new_map: BacklinkMap = {
        target: tuple(sorted(sources))
        for target, sources in collected.items()
    }
    old_map: BacklinkMap = getattr(env, "knowledge_backlinks", {})
    env.knowledge_backlinks = new_map

    # Lors d'une compilation incrémentale, une page cible doit être réécrite
    # si l'une de ses listes de backlinks a changé.
    changed_targets = {
        target
        for target in old_map.keys() | new_map.keys()
        if old_map.get(target) != new_map.get(target)
    }
    return changed_targets


def _document_title(env: BuildEnvironment, docname: str) -> str:
    title = env.titles.get(docname)
    return title.astext() if title is not None else docname


def _category(docname: str) -> tuple[int, str]:
    if docname.startswith("knowledge/"):
        return 0, "Fiches associées"
    if docname.startswith("paths/"):
        return 1, "Parcours"
    if docname.startswith("sources/"):
        return 2, "Sources"
    return 3, "Autres pages"


def _inject_backlinks(app: Sphinx, doctree: nodes.document, docname: str) -> None:
    backlinks: BacklinkMap = getattr(app.env, "knowledge_backlinks", {})
    source_docs = backlinks.get(docname, ())
    if not source_docs:
        return

    section = nodes.section(ids=["liens-entrants"], classes=["backlinks"])
    section += nodes.title(text="Liens entrants")
    section += nodes.paragraph(
        text="Ces pages mentionnent directement cette fiche."
    )

    grouped: dict[tuple[int, str], list[str]] = defaultdict(list)
    for source_doc in source_docs:
        grouped[_category(source_doc)].append(source_doc)

    for (_, label), documents in sorted(grouped.items()):
        section += nodes.rubric(text=label)
        bullet_list = nodes.bullet_list()

        for source_doc in sorted(
            documents, key=lambda name: _document_title(app.env, name).casefold()
        ):
            item = nodes.list_item()
            paragraph = nodes.paragraph()
            paragraph += nodes.reference(
                text=_document_title(app.env, source_doc),
                refuri=app.builder.get_relative_uri(docname, source_doc),
                internal=True,
            )
            item += paragraph
            bullet_list += item

        section += bullet_list

    # Les pages MyST sont généralement enveloppées dans une section racine
    # portant leur titre. Y insérer le bloc donne un vrai sous-titre (h2) au
    # lieu de créer un second titre principal (h1).
    container: nodes.Element = doctree
    for child in doctree.children:
        if isinstance(child, nodes.section):
            container = child
            break
    container += section


def setup(app: Sphinx) -> dict[str, object]:
    app.connect("env-updated", _collect_backlinks)
    app.connect("doctree-resolved", _inject_backlinks)

    return {
        "version": "1.0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
