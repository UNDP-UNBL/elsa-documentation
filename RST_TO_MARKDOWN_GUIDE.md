# RST to Markdown Conversion Guide

This guide explains the RST (reStructuredText) to Markdown conversions used in this project.

## Summary

All RST syntax has been converted to standard Markdown or MkDocs-specific extensions. The `scripts/fix_rst_remnants.py` script automates fixing any remaining RST syntax.

## Common Conversions

### 1. Collapsible/Dropdown Sections

**RST (Sphinx):**
```rst
.. dropdown:: Windows

   Content goes here
   Indented with 3 spaces
```

**Markdown (MkDocs):**
```markdown
??? note "Windows"

    Content goes here
    Indented with 4 spaces
```

**Options:**
- `???` = Collapsed by default (click to expand)
- `???+` = Expanded by default (click to collapse)

**Admonition Types:**
- `??? note "Title"` - Note/information
- `??? tip "Title"` - Helpful tip
- `??? warning "Title"` - Warning
- `??? example "Title"` - Example
- `??? info "Title"` - Information
- `??? question "Title"` - FAQ/Question

### 2. Code Blocks

**RST (Sphinx):**
```rst
.. code-block:: r

   install.packages("sf")
   library(sf)
```

**Markdown (Standard):**
````markdown
```r
install.packages("sf")
library(sf")
```
````

**Supported Languages:**
- `r` - R code
- `python` - Python code
- `bash` - Bash/shell scripts
- `yaml` - YAML configuration
- `json` - JSON data
- Leave empty for plain text

### 3. Admonitions (Info Boxes)

**RST (Sphinx):**
```rst
.. note::
   This is a note

.. warning::
   This is a warning

.. important::
   This is important
```

**Markdown (MkDocs):**
```markdown
!!! note
    This is a note

!!! warning
    This is a warning

!!! important
    This is important
```

**Available Types:**
- `note` - Blue info box
- `warning` - Orange warning box
- `danger` - Red danger box
- `tip` - Green tip box
- `info` - Blue information box
- `example` - Purple example box
- `quote` - Quote formatting

### 4. Headings

**RST (Sphinx):**
```rst
Title
=====

Subtitle
--------

Subheading
~~~~~~~~~~
```

**Markdown (Standard):**
```markdown
# Title

## Subtitle

### Subheading
```

### 5. Links

**RST (Sphinx):**
```rst
`Link text <https://example.com>`_

:doc:`other-page`

.. _link-target:
```

**Markdown (Standard):**
```markdown
[Link text](https://example.com)

[other page](other-page.md)

[link-target]: https://example.com
```

### 6. Images

**RST (Sphinx):**
```rst
.. image:: path/to/image.png
   :alt: Alternative text
   :width: 600px
```

**Markdown (Standard):**
```markdown
![Alternative text](path/to/image.png)
```

For size control, use HTML:
```html
<img src="path/to/image.png" alt="Alternative text" width="600">
```

### 7. Lists

**RST (Sphinx):**
```rst
1. First item
#. Auto-numbered
#. Auto-numbered

- Bullet point
- Another bullet
```

**Markdown (Standard):**
```markdown
1. First item
2. Second item
3. Third item

- Bullet point
- Another bullet
```

### 8. Emphasis

**RST (Sphinx):**
```rst
*italic*
**bold**
``code``
```

**Markdown (Standard):**
```markdown
*italic*
**bold**
`code`
```

### 9. Tables

**RST (Sphinx):**
```rst
+--------+--------+
| Header | Header |
+========+========+
| Cell   | Cell   |
+--------+--------+
```

**Markdown (Standard):**
```markdown
| Header | Header |
|--------|--------|
| Cell   | Cell   |
```

### 10. Block Quotes

**RST (Sphinx):**
```rst
    This is a block quote
    Indented content
```

**Markdown (Standard):**
```markdown
> This is a block quote
> Multiple lines
```

## MkDocs-Specific Features

### Content Tabs

```markdown
=== "Tab 1"
    Content for tab 1

=== "Tab 2"
    Content for tab 2
```

### Task Lists

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

### Keyboard Keys

```markdown
++ctrl+alt+del++
```

### Footnotes

```markdown
Here is a footnote reference[^1].

[^1]: Here is the footnote content.
```

## Fixing Scripts

### Run the Fix Script

```bash
python3 scripts/fix_rst_remnants.py
```

This script automatically fixes:
- Reference-style link headers: `[id]: # Title` → `# Title`
- Dropdown directives: `.. dropdown::` → `??? note`
- Code block directives: `.. code-block::` → ` ``` `
- Excessive whitespace
- RST artifacts

### Manual Fixes

Some complex RST constructs may need manual conversion:
- Custom directives
- Complex tables
- Cross-references with specific targets
- Bibliography citations

## Verification

After conversion, verify with:

```bash
# Build the site
mkdocs build

# Serve locally
mkdocs serve
```

Check for:
- ✅ All pages render correctly
- ✅ Code blocks have proper syntax highlighting
- ✅ Dropdowns expand/collapse correctly
- ✅ Images display properly
- ✅ Links work correctly

## Common Issues

### Code Blocks Not Highlighting

**Problem:** Code appears as plain text

**Solution:** Check the language identifier
````markdown
```r
# This will highlight as R code
```

```
# This will be plain text
```
````

### Dropdowns Not Working

**Problem:** Dropdown shows as plain text

**Solution:** Check indentation (4 spaces) and question marks
```markdown
??? note "Title"

    Content indented with 4 spaces
```

### Admonitions Not Rendering

**Problem:** Admonition appears as text

**Solution:** Check the exclamation marks and indentation
```markdown
!!! note
    Content indented with 4 spaces
```

### Images Not Loading

**Problem:** Image path broken

**Solution:** Use relative paths from the markdown file
```markdown
![Alt text](images/screenshot.png)
# Not: ![Alt text](/images/screenshot.png)
```

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
- [CommonMark Spec](https://commonmark.org/)

## Quick Reference

| RST | Markdown |
|-----|----------|
| `.. dropdown::` | `??? note "Title"` |
| `.. code-block:: lang` | ` ```lang` |
| `.. note::` | `!!! note` |
| `:doc:`page`` | `[page](page.md)` |
| `Title\n=====` | `# Title` |
| `` `text <url>`_ `` | `[text](url)` |
| `**bold**` | `**bold**` |
| `*italic*` | `*italic*` |
| ` ``code`` ` | `` `code` `` |

---

**Note:** The conversion scripts have already processed all files. This guide is for reference and future conversions.
