# Nabla

Ce dépôt contient une bibliothèque personnelle de connaissances scientifiques
reconstruites à partir de notes manuscrites. Sphinx génère un site HTML statique
doté d’une navigation, d’un index et d’une recherche en français.

Les photographies de travail conservées localement dans `dirty_notes/` ne sont
pas publiées ; les fiches finalisées et leurs illustrations le sont.

## Publication

Chaque push sur la branche `main` déclenche le workflow GitHub Actions
`.github/workflows/pages.yml`. Celui-ci construit le site avec Sphinx puis le
publie automatiquement sur GitHub Pages.

## Prévisualisation locale

```powershell
python -m pip install -r requirements.txt
python -m sphinx -b html source build
python -m http.server 8000 -d build
```

Le site est ensuite disponible à l'adresse `http://localhost:8000`.

## Organisation

```text
source/
├── _ext/        # extensions Sphinx locales
├── _static/     # styles du site
├── knowledge/   # fiches et collections
└── sources/     # emplacement des références futures
```

Chaque capsule possède un `index.md` et peut recevoir son propre dossier
`assets/` lorsqu'elle contient des images, données ou autres pièces jointes.

## Backlinks automatiques

L'extension locale `source/_ext/backlinks.py` analyse les liens internes écrits
dans le contenu Markdown. Lorsqu'une page A contient un lien vers une page B,
la version HTML de B reçoit automatiquement une section **Liens entrants** qui
renvoie vers A. Les liens issus des sommaires `toctree` sont ignorés.

Les backlinks sont regroupés en fiches associées, parcours, sources et autres
pages. Il n'y a rien à renseigner deux fois : un lien Markdown normal suffit.
