# ELSA Tool Documentation

Documentation for the ELSA (Essential Life Support Area) Integrated Spatial Planning Tool from the UN Biodiversity Lab.

**🌐 Live Documentation**: https://undp-unbl.github.io/elsa-documentation/

Available in 5 languages: English, Spanish, French, Portuguese, Russian

## Directory Structure

```
elsa/
├── README.md                 # This file
├── environment.yml           # Conda environment specification
├── conf.py                   # Sphinx configuration (integration-ready)
├── Makefile                  # Build automation
├── index.rst                 # Main ELSA documentation index
├── overview.rst              # Tool overview and capabilities
├── getting-started.rst       # Registration and access procedures
├── creating-analysis.rst     # Creating new analysis runs
├── editing-analysis.rst      # Parameter configuration guide
├── running-optimization.rst  # Analysis execution
├── viewing-results.rst       # Results interpretation
├── downloading-results.rst   # Data export and downloads
├── support.rst              # Support and additional resources
├── annexes.rst              # Reference materials and data specs
└── _static/                 # Static files (CSS, images)
    └── elsa-custom.css      # ELSA-specific styling
```

## Integration into Existing Documentation

### Method 1: As a New Section

1. **Copy files to your docs directory:**
   ```bash
   cp -r elsa/ /path/to/your/docs/
   ```

2. **Add to your main `index.rst` or `toctree`:**
   ```rst
   .. toctree::
      :maxdepth: 2
      :caption: Tools and Platforms
      
      existing-section-1
      existing-section-2
      elsa/index
      other-sections
   ```

3. **Update your main `conf.py`:**
   ```python
   # Add ELSA-specific extensions if needed
   extensions.extend([
       # your existing extensions
   ])
   
   # Include ELSA intersphinx mappings
   from elsa.conf import elsa_intersphinx_mapping
   intersphinx_mapping.update(elsa_intersphinx_mapping)
   ```

### Method 2: Merge into Existing Structure

1. **Integrate individual files:**
   ```
   your-docs/
   ├── tools/
   │   ├── existing-tool-1.rst
   │   ├── elsa-overview.rst        # renamed from overview.rst
   │   ├── elsa-getting-started.rst
   │   └── ...
   └── user-guides/
       ├── existing-guide.rst
       ├── elsa-user-guide.rst      # combined or split as needed
       └── ...
   ```

2. **Update cross-references:**
   ```rst
   # Change internal links from:
   :doc:`editing-analysis`
   
   # To:
   :doc:`tools/elsa-editing-analysis`
   ```

## Environment Setup

### Using Conda/Mamba

```bash
# Create environment from file
conda env create -f environment.yml

# Or with mamba (faster)
mamba env create -f environment.yml

# Activate environment
conda activate elsa-docs
```

### Manual Installation

```bash
# Create new environment
conda create -n elsa-docs python=3.8

# Activate and install dependencies
conda activate elsa-docs
conda install -c conda-forge sphinx sphinx_rtd_theme sphinx-autodoc-typehints

# Optional extensions
conda install -c conda-forge sphinx-copybutton sphinx-tabs myst-parser
```

## Building Documentation

**Important:** All build commands must be run from the `docs/` directory.

### Standalone Build

```bash
# Navigate to docs directory
cd docs

# Build HTML documentation
make html

# Build with live reload for development (requires sphinx-autobuild)
make livehtml

# Clean build directory
make clean

# Check external links
make linkcheck
```

### Integration Build

When integrated into existing documentation, use your project's existing build process:

```bash
# From your main docs directory
make html
# or
sphinx-build -b html . _build/html
```

## Configuration Notes

### For ReadTheDocs

The documentation is configured to work with ReadTheDocs out of the box:

1. **Set up ReadTheDocs project**
2. **Point to your repository**
3. **Specify `environment.yml` in Advanced Settings:**
   - Python configuration file: `environment.yml`
   - Use system packages: ✓

### For Existing Projects

The `conf.py` file is designed to detect when it's being integrated:

- **Standalone mode**: Full configuration with theme and project settings
- **Integration mode**: Only ELSA-specific settings, inherits from parent

### Custom Styling

ELSA-specific CSS is in `_static/elsa-custom.css`:

```css
/* Example customizations */
.elsa-note {
    border-left: 4px solid #2980B9;
    background-color: #f8f9fa;
    padding: 10px;
}

.elsa-highlight {
    background-color: #e8f4fd;
    border: 1px solid #2980B9;
}
```
## Translation and Localization

### Multi-language Support

The ELSA Tool documentation needs to be translated into multiple languages to support global KMGBF implementation:

**Target Languages:**
- English (primary/source)
- Spanish 
- French
- Russian
- Portuguese

### Translation Workflow

**Important:** All translation commands must be run from the `docs/` directory.

**Step 1: Prepare source files**
```bash
# Navigate to docs directory
cd docs

# Extract translatable strings
sphinx-build -b gettext . _build/gettext

# Create/update .pot files for translators
sphinx-intl update -p _build/gettext -d locales -l es -l fr -l ru -l pt
```

**Step 2: Translate content**
- Translation files (.po files) are located in `docs/locales/{language}/LC_MESSAGES/`
- Translators edit these files, filling in the `msgstr` fields with translations
- Spanish translations are in `locales/es/`, French in `locales/fr/`, etc.

**Step 3: Build translated documentation**
```bash
# Still in docs/ directory

# Build Spanish version
sphinx-build -b html -D language=es . _build/html/es

# Build all languages
for lang in es fr ru pt; do
  sphinx-build -b html -D language=$lang . _build/html/$lang
done
```

**Step 4: View translated documentation**
```bash
# Open Spanish docs
xdg-open _build/html/es/index.html

# Or use your browser
firefox _build/html/es/index.html

## Content Organization

### Document Hierarchy

1. **Quick Start** (`index.rst`) - Overview and navigation
2. **Setup** (`getting-started.rst`) - Account and workspace access
3. **Basic Usage** (`creating-analysis.rst`, `editing-analysis.rst`) - Core functionality
4. **Advanced Features** (`running-optimization.rst`, `viewing-results.rst`) - Detailed analysis
5. **Data Management** (`downloading-results.rst`) - Export and integration
6. **Support** (`support.rst`, `annexes.rst`) - Help and reference

### Cross-References

Internal links use Sphinx references:

```rst
# Link to other sections
:doc:`viewing-results`

# Link to specific sections
:ref:`annex-1`

# Link to glossary terms
:term:`Planning feature`
```

## Maintenance and Updates

### Version Control

- Each major ELSA tool update should increment version numbers in `conf.py`
- Keep change log in `CHANGELOG.md` (create if needed)
- Tag documentation versions to match tool releases

### Content Updates

**Regular updates needed for:**
- Feature additions and interface changes
- Updated contact information and links

**Update frequency:**
- **Major updates**: With each ELSA tool release
- **Minor updates**: Quarterly for contact info, links
- **Content fixes**: As needed for accuracy

### Quality Assurance

Before publishing updates:

```bash
# Check for broken links
make linkcheck

# Validate RST syntax
sphinx-build -b dummy . _build/dummy

# Review rendering
make html && open _build/html/index.html
```

## Support and Contributions

### Getting Help

- **ELSA Tool Support**: support@unbiodiversitylab.org
- **Documentation Issues**: Create issues in your project repository
- **Sphinx/RST Help**: [Sphinx Documentation](https://www.sphinx-doc.org/)

### Contributing Updates

1. **Fork/branch** your documentation repository
2. **Make changes** to relevant `.rst` files
3. **Test locally** with `make html`
4. **Submit pull request** with description of changes
5. **Review and merge** following your project's workflow

### Content Guidelines

- **Use clear, concise language** suitable for non-technical users
- **Include practical examples** and screenshots where helpful
- **Maintain consistent formatting** with existing documentation style
- **Test all procedures** described in the documentation
- **Keep external links current** and functional

This documentation structure provides flexibility for integration while maintaining the complete ELSA tool user guide in a professional, searchable format.