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
