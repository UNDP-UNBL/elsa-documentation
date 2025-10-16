#!/usr/bin/env python3
"""
Convert Sphinx RST documentation to MkDocs Markdown format.
Handles the conversion of all .rst files in the docs directory.
"""

import os
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple

# Base directory for documentation
DOCS_DIR = Path(__file__).parent / "docs"


def convert_rst_to_markdown(rst_content: str, file_path: Path) -> str:
    """
    Convert RST content to Markdown format.

    Args:
        rst_content: The RST content as a string
        file_path: Path to the original RST file for context

    Returns:
        Converted Markdown content
    """
    md_content = rst_content

    # Convert title underlines (=== style)
    lines = md_content.split('\n')
    new_lines = []
    i = 0

    while i < len(lines):
        current_line = lines[i]

        # Check if next line is a title underline
        if i + 1 < len(lines):
            next_line = lines[i + 1]

            # Main title (===)
            if re.match(r'^=+\s*$', next_line) and current_line.strip():
                level = 1
                new_lines.append(f"{'#' * level} {current_line.strip()}")
                i += 2
                continue

            # Section title (---)
            elif re.match(r'^-+\s*$', next_line) and current_line.strip():
                level = 2
                new_lines.append(f"{'#' * level} {current_line.strip()}")
                i += 2
                continue

            # Subsection title (~~~)
            elif re.match(r'^~+\s*$', next_line) and current_line.strip():
                level = 3
                new_lines.append(f"{'#' * level} {current_line.strip()}")
                i += 2
                continue

            # Subsubsection title (^^^)
            elif re.match(r'^\^+\s*$', next_line) and current_line.strip():
                level = 4
                new_lines.append(f"{'#' * level} {current_line.strip()}")
                i += 2
                continue

        new_lines.append(current_line)
        i += 1

    md_content = '\n'.join(new_lines)

    # Convert toctree to basic list (will need manual adjustment for nav)
    md_content = re.sub(
        r'\.\. toctree::\s*\n(?:\s+:[^:]+:[^\n]*\n)*\s*\n((?:\s+[^\n]+\n)*)',
        lambda m: '<!-- Navigation items:\n' + m.group(1) + '-->\n',
        md_content
    )

    # Convert :doc: cross-references to markdown links
    # Pattern: :doc:`text </path/to/doc>`
    md_content = re.sub(
        r':doc:`([^<]+)\s*<([^>]+)>`',
        lambda m: f"[{m.group(1).strip()}]({m.group(2).strip().replace('/elsa/', 'elsa/').replace('/trainings/', 'trainings/').replace('/guidance/', 'guidance/')}.md)",
        md_content
    )

    # Convert simple :doc:`path` references
    md_content = re.sub(
        r':doc:`([^`]+)`',
        lambda m: f"[{m.group(1).split('/')[-1]}]({m.group(1)}.md)",
        md_content
    )

    # Convert .. note:: directive to markdown admonition
    md_content = re.sub(
        r'\.\. note::\s*\n\s+(.+?)(?=\n\n|\n\.\.|$)',
        r'!!! note\n    \1',
        md_content,
        flags=re.DOTALL
    )

    # Convert .. warning:: directive
    md_content = re.sub(
        r'\.\. warning::\s*\n\s+(.+?)(?=\n\n|\n\.\.|$)',
        r'!!! warning\n    \1',
        md_content,
        flags=re.DOTALL
    )

    # Convert .. important:: directive
    md_content = re.sub(
        r'\.\. important::\s*\n\s+(.+?)(?=\n\n|\n\.\.|$)',
        r'!!! important\n    \1',
        md_content,
        flags=re.DOTALL
    )

    # Convert .. tip:: directive
    md_content = re.sub(
        r'\.\. tip::\s*\n\s+(.+?)(?=\n\n|\n\.\.|$)',
        r'!!! tip\n    \1',
        md_content,
        flags=re.DOTALL
    )

    # Convert .. image:: directive
    md_content = re.sub(
        r'\.\. image::\s+([^\n]+)(?:\s+:([^:]+):\s+([^\n]+))*',
        lambda m: f"![{m.group(1).split('/')[-1]}]({m.group(1)})",
        md_content
    )

    # Convert .. figure:: directive
    md_content = re.sub(
        r'\.\. figure::\s+([^\n]+)\s*\n(?:\s+:[^:]+:[^\n]*\n)*\s*\n\s+(.+?)(?=\n\n|\n\.\.|$)',
        lambda m: f"![{m.group(2).strip()}]({m.group(1).strip()})\n\n*{m.group(2).strip()}*",
        md_content,
        flags=re.DOTALL
    )

    # Convert code blocks (:: at end of line)
    md_content = re.sub(
        r'::(\s*\n\s*\n)((?:(?:\s{3,}.+|\s*)\n)+)',
        lambda m: f"```\n{m.group(2).strip()}\n```\n",
        md_content
    )

    # Convert inline code
    md_content = re.sub(r'``([^`]+)``', r'`\1`', md_content)

    # Convert bold text
    md_content = re.sub(r'\*\*([^*]+)\*\*', r'**\1**', md_content)

    # Convert italic text (single asterisk, but not double)
    md_content = re.sub(r'(?<!\*)\*(?!\*)([^*]+)\*(?!\*)', r'*\1*', md_content)

    # Convert external links: `text <url>`_
    md_content = re.sub(r'`([^<]+)<([^>]+)>`_', r'[\1](\2)', md_content)

    # Convert link definitions (.. _name: url)
    md_content = re.sub(r'\.\. _([^:]+):\s+(.+)', r'[\1]: \2', md_content)

    # Convert numbered lists (preserve existing markdown format)
    # RST uses #. for auto-numbering, convert to 1., 2., etc.
    lines = md_content.split('\n')
    counter = 1
    new_lines = []
    for line in lines:
        if re.match(r'^\s*#\.', line):
            indent = len(line) - len(line.lstrip())
            new_lines.append(' ' * indent + f"{counter}. {line.lstrip()[3:]}")
            counter += 1
        else:
            if not re.match(r'^\s*$', line):
                counter = 1
            new_lines.append(line)
    md_content = '\n'.join(new_lines)

    # Clean up excessive blank lines
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)

    return md_content


def convert_file(rst_file: Path, output_dir: Path) -> None:
    """
    Convert a single RST file to Markdown.

    Args:
        rst_file: Path to the RST file
        output_dir: Directory to write the Markdown file
    """
    print(f"Converting {rst_file.relative_to(DOCS_DIR)}...")

    # Read RST content
    with open(rst_file, 'r', encoding='utf-8') as f:
        rst_content = f.read()

    # Convert to Markdown
    md_content = convert_rst_to_markdown(rst_content, rst_file)

    # Determine output path
    relative_path = rst_file.relative_to(DOCS_DIR)
    md_file = output_dir / relative_path.with_suffix('.md')

    # Create parent directories
    md_file.parent.mkdir(parents=True, exist_ok=True)

    # Write Markdown file
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"  -> {md_file.relative_to(output_dir)}")


def move_static_assets(docs_dir: Path) -> None:
    """
    Move static assets to the appropriate MkDocs structure.

    Args:
        docs_dir: Documentation directory
    """
    print("\nMoving static assets...")

    # Create assets directory
    assets_dir = docs_dir / "assets"
    assets_dir.mkdir(exist_ok=True)

    # Move CSS files
    static_dir = docs_dir / "_static"
    if static_dir.exists():
        css_dir = assets_dir / "css"
        css_dir.mkdir(exist_ok=True)

        for css_file in static_dir.glob("*.css"):
            target = css_dir / css_file.name
            print(f"  Copying {css_file.name} -> {target.relative_to(docs_dir)}")
            target.write_text(css_file.read_text())

    # Images are already in appropriate locations (elsa/images/, etc.)
    # Just note them
    image_dirs = list(docs_dir.glob("**/images"))
    if image_dirs:
        print(f"\n  Found {len(image_dirs)} image directories (keeping in place):")
        for img_dir in image_dirs:
            num_images = len(list(img_dir.glob("*.png"))) + len(list(img_dir.glob("*.jpg")))
            print(f"    - {img_dir.relative_to(docs_dir)} ({num_images} images)")


def main():
    """Main conversion process."""
    print("=" * 70)
    print("ELSA Documentation: Sphinx RST to MkDocs Markdown Conversion")
    print("=" * 70)

    # Find all RST files
    rst_files = list(DOCS_DIR.glob("**/*.rst"))
    rst_files = [f for f in rst_files if '_build' not in str(f)]

    print(f"\nFound {len(rst_files)} RST files to convert\n")

    # Convert each file
    for rst_file in rst_files:
        convert_file(rst_file, DOCS_DIR)

    # Move static assets
    move_static_assets(DOCS_DIR)

    print("\n" + "=" * 70)
    print("Conversion complete!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Review the converted Markdown files")
    print("2. Manually adjust any complex RST directives")
    print("3. Update image paths if needed")
    print("4. Test the build with: mkdocs serve")
    print("5. Update translations using the i18n plugin")


if __name__ == "__main__":
    main()
