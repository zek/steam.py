# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import re
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))


# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib_trio",
    "exception_hierarchy",
    "enums",
    "events",
]

autodoc_member_order = "bysource"  # TODO I feel like there is a way to get a better order
autodoc_typehints = "none"

# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aio": ("https://docs.aiohttp.org/en/stable", None),
}

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
.. |maybecallabledeco| replace:: This decorator *could be callable*.
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "steam.py"
copyright = "2020, Gobot1234"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

with open("../steam/__init__.py") as f:
    search = re.search(r'^__version__\s*=\s*"([^"]*)"', f.read(), re.MULTILINE)

# The full version, including alpha/beta/rc tags.
release = search.group(1)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

locale_dirs = ["locale/"]
gettext_compact = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "friendly"


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "basic"

html_context = {
    "discord_invite": "https://discord.gg/MQ68WUS",
    "module_extensions": [
        ("steam.ext.commands", "ext/commands"),
    ],
    "repository": "https://github.com/Gobot1234/steam.py",
}

extlinks = {
    "issue": (f"{html_context['repository']}/%s", "GH-"),
}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "images/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
html_search_scorer = "_static/scorer.js"

html_js_files = ["custom.js", "settings.js", "copy.js", "sidebar.js"]
