#!/usr/bin/env python3
"""
Setup MkDocs i18n structure for multi-language documentation.
This script helps migrate from Sphinx gettext to MkDocs i18n plugin structure.
"""

import os
import shutil
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"

# Languages to support
LANGUAGES = ["es", "fr", "pt", "ru"]


def create_i18n_structure():
    """
    Create the directory structure for mkdocs-static-i18n plugin.

    The plugin expects translated files in the same directory structure
    with language suffix: file.es.md, file.fr.md, etc.
    """
    print("=" * 70)
    print("Setting up MkDocs i18n structure")
    print("=" * 70)

    print("\nCreating language-specific documentation structure...")
    print("\nFor mkdocs-static-i18n with 'suffix' structure:")
    print("  - English files: filename.md")
    print("  - Spanish files: filename.es.md")
    print("  - French files: filename.fr.md")
    print("  - Portuguese files: filename.pt.md")
    print("  - Russian files: filename.ru.md")

    # Find all markdown files
    md_files = list(DOCS_DIR.glob("**/*.md"))
    md_files = [f for f in md_files if not any(lang in f.stem for lang in LANGUAGES)]

    print(f"\nFound {len(md_files)} English markdown files")

    # Create placeholder files for each language
    for md_file in md_files:
        relative_path = md_file.relative_to(DOCS_DIR)

        for lang in LANGUAGES:
            # Create language-specific filename: filename.lang.md
            lang_file = md_file.parent / f"{md_file.stem}.{lang}.md"

            if not lang_file.exists():
                # Create placeholder with notice
                content = f"""# Translation Placeholder ({lang.upper()})

This file is a placeholder for the {lang.upper()} translation of `{md_file.name}`.

The original Sphinx translations are in the `locales/{lang}/` directory as `.po` files.
These need to be manually reviewed and converted to markdown format.

## Translation Process

1. Locate the corresponding .po file in `locales/{lang}/LC_MESSAGES/`
2. Extract the translated content from the .po file
3. Replace this placeholder with the translated markdown content
4. Ensure all formatting, links, and images are properly updated

## Original File

- English source: `{relative_path}`
"""
                lang_file.write_text(content, encoding='utf-8')
                print(f"  Created placeholder: {lang_file.relative_to(DOCS_DIR)}")

    print("\n" + "=" * 70)
    print("i18n structure setup complete!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Review the .po files in docs/locales/<lang>/LC_MESSAGES/")
    print("2. Extract translations and update the .<lang>.md files")
    print("3. You can use tools like po2txt or manual extraction")
    print("4. Test each language with: mkdocs build -f mkdocs.yml")


def create_translation_guide():
    """Create a guide for manual translation migration."""

    guide_content = """# Translation Migration Guide

This guide explains how to migrate translations from Sphinx gettext (.po files)
to MkDocs i18n structure.

## Current Structure

Your Sphinx translations are located in:
```
docs/locales/
├── es/LC_MESSAGES/  (Spanish)
├── fr/LC_MESSAGES/  (French)
├── pt/LC_MESSAGES/  (Portuguese)
└── ru/LC_MESSAGES/  (Russian)
```

Each directory contains .po files with translations for each documentation page.

## Target Structure

MkDocs with mkdocs-static-i18n uses a suffix structure:
```
docs/
├── index.md          (English - default)
├── index.es.md       (Spanish translation)
├── index.fr.md       (French translation)
├── index.pt.md       (Portuguese translation)
└── index.ru.md       (Russian translation)
```

## Migration Process

### Option 1: Manual Migration (Recommended for Quality)

1. Open the English .md file
2. Open the corresponding .po file for the target language
3. Copy the English markdown structure
4. Replace English text with translations from .po file's `msgstr` fields
5. Verify all formatting, links, and images

### Option 2: Automated Extraction

Use the provided script to extract translations:

```bash
python3 extract_po_translations.py --lang es --input docs/locales/es/LC_MESSAGES/index.po --template docs/index.md --output docs/index.es.md
```

### Option 3: Use Professional Tools

- **Crowdin**: Import .po files, export as markdown
- **Transifex**: Similar workflow
- **po2txt**: Command-line tool for extraction

## PO File Format

Each .po file contains:
```
#: ../../source/file.rst:10
msgid "English text here"
msgstr "Translated text here"
```

## Validation

After creating translated files, test with:
```bash
mkdocs build
mkdocs serve
```

Then navigate to different language versions in your browser.

## Tips

- Maintain the same markdown structure across all languages
- Update internal links to use .md extension (not .rst)
- Verify image paths work in all languages
- Test special markdown features (admonitions, code blocks) in each language

## Getting Help

If you need assistance with translation migration:
1. Check the mkdocs-static-i18n documentation
2. Review the Material for MkDocs i18n guide
3. Consider hiring translation services for bulk conversion
"""

    guide_file = BASE_DIR / "TRANSLATION_MIGRATION.md"
    guide_file.write_text(guide_content, encoding='utf-8')
    print(f"\nCreated translation guide: {guide_file.name}")


if __name__ == "__main__":
    create_i18n_structure()
    create_translation_guide()
