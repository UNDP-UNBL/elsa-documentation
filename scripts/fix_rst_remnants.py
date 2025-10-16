#!/usr/bin/env python3
"""
Fix remaining RST syntax that didn't convert properly to Markdown.
Handles:
- Reference-style link headers: [id]: # Title
- RST dropdown directives: .. dropdown:: -> ??? note
- Excessive whitespace and formatting issues
"""

import re
from pathlib import Path

def fix_markdown_file(file_path: Path) -> bool:
    """Fix RST remnants in a markdown file. Returns True if changes were made."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix reference-style link headers: [identifier]: # Title
    # Convert to proper markdown heading
    content = re.sub(
        r'^\[[\w_]+\]: # (.+)$',
        r'# \1',
        content,
        flags=re.MULTILINE
    )

    # Fix RST dropdown directives to MkDocs collapsible admonitions
    # .. dropdown:: Title -> ??? note "Title"
    content = re.sub(
        r'^\.\. dropdown:: (.+)$',
        r'??? note "\1"',
        content,
        flags=re.MULTILINE
    )

    # Fix RST code-block directives to Markdown fenced code blocks
    # .. code-block:: language\n   code -> ```language\ncode\n```
    # This handles both non-indented and indented (inside dropdowns) code blocks

    def replace_code_block_indented(language, code_content, base_indent):
        """Handle indented code blocks."""
        language = language or ''
        lines = code_content.split('\n')
        processed_lines = []

        for line in lines:
            if line.strip():
                # Remove base indent + 3 spaces (RST code indent)
                if len(line) > base_indent + 3:
                    processed_lines.append(line[base_indent + 3:])
                else:
                    processed_lines.append(line.lstrip())
            elif processed_lines:  # Keep blank lines within code
                processed_lines.append('')

        code = '\n'.join(processed_lines).rstrip()
        indent = ' ' * base_indent
        return f"{indent}```{language}\n{code}\n{indent}```"

    # Match code-block directive (possibly indented) and capture content
    content = re.sub(
        r'^(\s*)\.\. code-block:: (\w*)\s*\n((?:\1   .+\n|\s*\n)*)',
        lambda m: replace_code_block_indented(m.group(2), m.group(3), len(m.group(1))),
        content,
        flags=re.MULTILINE
    )

    # Fix nested !!! note blocks that need proper indentation
    # Already properly formatted - just ensure consistency

    # Clean up excessive blank lines (more than 2 consecutive)
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    # Fix spacing around list items in admonitions
    # Remove trailing |  characters left over from RST
    content = re.sub(r'^\s+\|\s*$', '', content, flags=re.MULTILINE)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False


def main():
    """Fix all markdown files in the docs directory."""
    docs_dir = Path(__file__).parent.parent / "docs"

    print("=" * 70)
    print("Fixing RST Remnants in Markdown Files")
    print("=" * 70)

    # Find all markdown files
    md_files = list(docs_dir.glob("**/*.md"))

    print(f"\nFound {len(md_files)} markdown files")

    fixed_count = 0
    fixed_files = []

    for md_file in md_files:
        if fix_markdown_file(md_file):
            fixed_count += 1
            fixed_files.append(md_file.relative_to(docs_dir))
            print(f"  ✓ Fixed: {md_file.relative_to(docs_dir)}")

    print("\n" + "=" * 70)
    print(f"Fixed {fixed_count} files")
    print("=" * 70)

    if fixed_files:
        print("\nFixed files:")
        for file in fixed_files:
            print(f"  - {file}")
    else:
        print("\nNo files needed fixing")


if __name__ == "__main__":
    main()
