# ELSA Tool Documentation - MkDocs Edition

This repository contains the complete documentation for the ELSA (Essential Life Support Area) Integrated Spatial Planning Tool, now powered by MkDocs with Material theme.

[![Deploy MkDocs to GitHub Pages](https://github.com/UNDP-UNBL/elsa-documentation/actions/workflows/deploy.yml/badge.svg)](https://github.com/UNDP-UNBL/elsa-documentation/actions/workflows/deploy.yml)

## 🚀 Quick Start

### Using Mamba/Conda (Recommended)

```bash
# Activate the environment
mamba activate elsa-mkdocs

# Serve locally
mkdocs serve

# Build for deployment
mkdocs build
```

### Using Python Virtual Environment

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Serve locally
mkdocs serve
```

Visit http://127.0.0.1:8000 to view the documentation.

## 📁 Project Structure

```
elsa-documentation/
├── mkdocs.yml                    # MkDocs configuration
├── requirements.txt              # Python dependencies
├── environment-mkdocs.yaml       # Conda/mamba environment
├── .readthedocs.yaml            # ReadTheDocs configuration
├── docs/
│   ├── index.md                 # Homepage
│   ├── assets/
│   │   └── css/
│   │       └── elsa-custom.css  # Custom styling
│   └── elsa/                    # ELSA Tool docs (13 pages)
│       ├── index.md
│       ├── 01_overview.md
│       ├── 02_tool_purpose.md
│       └── ...
├── site/                        # Built documentation (auto-generated)
└── locales/                     # Original translations (for reference)
```

## 🌍 Multi-language Support

Documentation is available in 5 languages:
- 🇬🇧 **English** (default)
- 🇪🇸 **Spanish** (Español)
- 🇫🇷 **French** (Français)
- 🇵🇹 **Portuguese** (Português)
- 🇷🇺 **Russian** (Русский)

Language switching is available in the site header.

## 📝 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[MKDOCS_MIGRATION.md](MKDOCS_MIGRATION.md)** - Complete migration details
- **[TODO.md](TODO.md)** - Remaining tasks and roadmap
- **[TRANSLATION_MIGRATION.md](TRANSLATION_MIGRATION.md)** - Translation guide

## 🎨 Features

- ✅ Modern, mobile-responsive Material theme
- ✅ Fast client-side search
- ✅ Dark/light mode toggle
- ✅ Code syntax highlighting with copy buttons
- ✅ Image lightbox for full-size viewing
- ✅ Tabbed navigation
- ✅ GitHub integration with edit links
- ✅ Multi-language support
- ✅ Free hosting on ReadTheDocs

## 🛠️ Common Tasks

### Preview Changes Locally

```bash
mkdocs serve
# Opens at http://127.0.0.1:8000
```

### Build Documentation

```bash
mkdocs build
# Output in site/ directory
```

### Deploy to ReadTheDocs

Simply push to your repository - ReadTheDocs will automatically build and deploy.

### Add New Page

1. Create new `.md` file in `docs/` directory
2. Add to navigation in `mkdocs.yml`
3. Test with `mkdocs serve`

### Update Styling

Edit `docs/assets/css/elsa-custom.css` for custom styles.

## 📊 Build Status

- **Build time:** ~8 seconds
- **Total pages:** 72 pages in English
- **Languages:** 5 supported
- **Images:** 81 images preserved
- **Hosting:** Free on ReadTheDocs

## 🔧 Environment Setup

### Conda/Mamba Environment

The environment has already been created. To recreate:

```bash
mamba env create -f environment-mkdocs.yaml
```

### System Requirements

- Python 3.11+
- 100 MB disk space for environment
- 50 MB for built site

## 📖 Documentation Content

### ELSA Tool Documentation (13 chapters)
- Overview and introduction
- Registration and access
- Creating and editing analyses
- Running optimizations
- Viewing and downloading results
- Support and annexes

## 🤝 Contributing

1. Create a feature branch
2. Make your changes to `.md` files
3. Test locally with `mkdocs serve`
4. Submit a pull request

## 📞 Support

- **ELSA Tool Support:** support@unbiodiversitylab.org
- **Documentation Issues:** Create issues in this repository
- **MkDocs Help:** https://www.mkdocs.org/
- **Material Theme:** https://squidfunk.github.io/mkdocs-material/

## 📜 License

Documentation content © 2025 UNDP & UNEP-WCMC

## 🔗 Links

- **Live Documentation:** [Your ReadTheDocs URL]
- **UN Biodiversity Lab:** https://www.unbiodiversitylab.org
- **ELSA Tool:** https://map.unbiodiversitylab.org/earth
- **GitHub Repository:** https://github.com/UNDP-UNBL/elsa-documentation

## 🎯 Migration Status

✅ **Phase 1: Complete** - All RST files converted to Markdown
✅ **Phase 2: Complete** - MkDocs configuration and build working
🔄 **Phase 3: In Progress** - Translation migration
⏳ **Phase 4: Pending** - Content review and testing

See [TODO.md](TODO.md) for detailed status.

## 📚 Additional Resources

### For Developers
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)

### For Translators
- [Translation Migration Guide](TRANSLATION_MIGRATION.md)
- [mkdocs-static-i18n Plugin](https://github.com/ultrabug/mkdocs-static-i18n)

### For Content Authors
- [Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
- [Material Theme Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [Admonitions Guide](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

---
