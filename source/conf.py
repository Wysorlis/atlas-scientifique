import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent / "_ext"))

project = "Nabla"
author = "Bibliothèque personnelle"
language = "fr"

extensions = [
    "myst_parser",
    "sphinx.ext.mathjax",
    "backlinks",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "tasklist",
]
myst_heading_anchors = 3

html_theme = "furo"
html_title = "Nabla"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_favicon = "_static/favicon.svg"
html_search_language = "fr"
html_show_sourcelink = True
html_copy_source = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

mathjax3_config = {
    "loader": {"load": ["[tex]/cancel"]},
    "tex": {"packages": {"[+]": ["cancel"]}},
}
