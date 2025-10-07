# repo-unroll-priv
Get all non-gitignored text into context.

Simple script to get all non-gitgnored ASCII text from a repo into a single string.

It traverses each directory recurisvely and copies the relevant textual code in.

## usage
```bash
python repo_unroll.py [path]
python repo_unroll.py -c
python repo_unroll.py ~/projects/foo
```

The final output looks something likes this:

```
./examples/single_string.rs:
<rust code for this example>

./examples/multiple_string.rs:
<rust code for this example.>

./src/lib.rs:
<code for the lib>

<and so on for each directory recursively>
```

Useful if for example you want to copy all of a repository and put it in chatbot.

For example for this repo you get the following output from `python repo_unroll.py ./`

```
./.gitignore:
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py.cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock
#poetry.toml

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
#pdm.lock
#pdm.toml
.pdm-python
.pdm-build/

# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
#pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.envrc
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Abstra
# Abstra is an AI-powered process automation framework.
# Ignore directories containing user credentials, local state, and settings.
# Learn more at https://abstra.io/docs
.abstra/

# Visual Studio Code
#  Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore
#  that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#  and can be added to the global gitignore or merged into this file. However, if you prefer,
#  you could uncomment the following to ignore the entire vscode folder
# .vscode/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

# Cursor
#  Cursor is an AI-powered code editor. `.cursorignore` specifies files/directories to
#  exclude from AI features like autocomplete and code analysis. Recommended for sensitive data
#  refer to https://docs.cursor.com/context/ignore-files
.cursorignore
.cursorindexingignore

# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/


./README.md:
# repo-unroll-priv
Get all non-gitignored text into context.

Simple script to get all non-gitgnored ASCII text from a repo into a single string.

It traverses each directory recurisvely and copies the relevant textual code in.

## usage
```bash
python repo_unroll.py [path]
python repo_unroll.py -c
python repo_unroll.py ~/projects/foo
```

The final output looks something likes this:

```
./examples/single_string.rs:
<rust code for this example>

./examples/multiple_string.rs:
<rust code for this example.>

./src/lib.rs:
<code for the lib>

<and so on for each directory recursively>
```

Useful if for example you want to copy all of a repository and put it in chatbot.

For example for this repo you get the following output from `python repo_unroll.py ./`

```
./repo_unroll.py:
import argparse
import os
import subprocess
import sys
from pathlib import Path


def is_binary(file_path):
    """Check if a file is binary by reading the first 8192 bytes."""
    try:
        with open(file_path, "rb") as f:
            chunk = f.read(8192)
            if not chunk:
                return False
            return b"\0" in chunk
    except (IOError, OSError):
        return True


def get_gitignored_files(repo_path):
    """Get set of files that should be ignored according to git."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "--ignored", "--exclude-standard", "--others", "--directory"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            ignored = set()
            for line in result.stdout.splitlines():
                if line:
                    ignored.add(os.path.normpath(line.rstrip("/")))
            return ignored
        return set()
    except (subprocess.SubprocessError, FileNotFoundError):
        return set()


def is_ignored(file_path, repo_path, ignored_files):
    """Check if a file path should be ignored."""
    try:
        rel_path = os.path.relpath(file_path, repo_path)
        normalized = os.path.normpath(rel_path)

        if normalized in ignored_files:
            return True

        parts = Path(normalized).parts
        for i in range(len(parts)):
            partial_path = os.path.join(*parts[: i + 1])
            if partial_path in ignored_files:
                return True

        return False
    except (ValueError, OSError):
        return True


def unroll_repo(repo_path):
    """Unroll repository into a single text string."""
    repo_path = Path(repo_path).resolve()

    if not repo_path.is_dir():
        raise RuntimeError(f"Error: {repo_path} is not a directory")

    ignored_files = get_gitignored_files(repo_path)

    output_lines = []

    for root, dirs, files in os.walk(repo_path):
        root_path = Path(root)

        dirs[:] = [
            d
            for d in dirs
            if not is_ignored(root_path / d, repo_path, ignored_files) and d != ".git"
        ]
        dirs.sort()

        for file in sorted(files):
            file_path = root_path / file

            if is_ignored(file_path, repo_path, ignored_files):
                continue

            if is_binary(file_path):
                continue

            try:
                rel_path = os.path.relpath(file_path, repo_path)

                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                output_lines.append(f"./{rel_path}:")
                output_lines.append(content)
                output_lines.append("")

            except (IOError, OSError) as e:
                print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
                continue

    return "\n".join(output_lines)


def main():
    parser = argparse.ArgumentParser(description="Unroll a repository into a single text output")
    parser.add_argument(
        "path", nargs="?", default=".", help="Path to the repository (default: current directory)"
    )
    parser.add_argument(
        "--clipboard",
        "-c",
        action="store_true",
        help="Copy output to clipboard (requires pbcopy on macOS)",
    )

    args = parser.parse_args()

    output = unroll_repo(args.path)

    print(output)

    if args.clipboard:
        try:
            proc = subprocess.Popen(
                ["pbcopy"],
                stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            proc.communicate(output.encode("utf-8"))
            if proc.returncode == 0:
                print("\n✓ Copied to clipboard", file=sys.stderr)
            else:
                print("\n✗ Failed to copy to clipboard", file=sys.stderr)
        except FileNotFoundError:
            print("\n✗ pbcopy not found (clipboard copy only works on macOS)", file=sys.stderr)
        except Exception as e:
            print(f"\n✗ Failed to copy to clipboard: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
