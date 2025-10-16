# MkDocs Migration TODO List

## ✅ Completed

- [x] Created MkDocs configuration (`mkdocs.yml`)
- [x] Converted all 72 RST files to Markdown
- [x] Set up multi-language support structure (5 languages)
- [x] Migrated CSS files to `docs/assets/css/`
- [x] Preserved image directories in place (81 images)
- [x] Updated ReadTheDocs configuration
- [x] Created conda/mamba environment (`environment-mkdocs.yaml`)
- [x] Created Python requirements file (`requirements.txt`)
- [x] Fixed navigation structure in `mkdocs.yml`
- [x] Created missing index files (elsa/index.md)
- [x] Tested build successfully (builds in ~8 seconds)
- [x] Verified all 5 language builds work
- [x] Created migration documentation
- [x] Created quick start guide

## 🔄 In Progress / Recommended Next Steps

### High Priority

- [ ] **Review converted Markdown files** - Check that complex RST directives converted correctly
- [ ] **Fix external links** - Update `www.7-zip.org` link in training5/05_installing_gurobi.md to include `https://`
- [ ] **Test all internal links** - Verify cross-references between pages work
- [ ] **Review images** - Ensure all images display correctly and paths are correct

### Medium Priority

- [ ] **Complete translations** - Migrate content from .po files to .lang.md files
  - Option A: Run `python3 setup_i18n.py` to create placeholders
  - Option B: Use translation management platform (Crowdin, Transifex)
  - Option C: Manual extraction from .po files
- [ ] **Add missing index files** - Create comprehensive index.md files for subsections
- [ ] **Update custom CSS** - Review and update `docs/assets/css/elsa-custom.css` for Material theme
- [ ] **Add logo and favicon** - Update paths in mkdocs.yml if you have logo files

### Low Priority

- [ ] **Add social cards** - Configure Material theme's social cards feature
- [ ] **Set up versioning** - Use mike for documentation versioning if needed
- [ ] **Add analytics** - Configure Google Analytics or privacy-friendly alternative
- [ ] **Improve SEO** - Add meta descriptions to pages
- [ ] **Add search configuration** - Fine-tune search behavior if needed
- [ ] **Create custom 404 page** - Add docs/404.md for better error handling

## 📋 Testing Checklist

Before deploying to production:

- [ ] Build succeeds without errors: `mkdocs build --strict`
- [ ] Local preview works: `mkdocs serve`
- [ ] Test all major pages load correctly
- [ ] Test navigation between sections
- [ ] Test language switcher
- [ ] Test search functionality
- [ ] Test on mobile/tablet devices
- [ ] Test images and diagrams display
- [ ] Test code blocks and syntax highlighting
- [ ] Test admonitions (notes, warnings, etc.)
- [ ] Verify ReadTheDocs build succeeds
- [ ] Test deployed site on ReadTheDocs URL

## 🐛 Known Issues

### Minor Warnings (Non-blocking)

1. **Link warning**: `trainings/training5/05_installing_gurobi.md` contains link to `www.7-zip.org` without protocol
   - **Fix**: Add `https://` to the link

### Navigation Improvements Needed

1. Some Ecuador/Peru guidance subsections not in nav (files exist but not linked)
   - Files: `021_what.md`, `022_functions.md`, `023_lock.md`, etc.
   - **Decision needed**: Should these be separate nav items or included in parent pages?

## 📝 Translation Status

### English
- ✅ 100% complete (72 files converted)

### Spanish (es)
- ⏳ Structure ready
- ❌ Content needs migration from .po files
- Total: 71 .po files in `docs/locales/es/LC_MESSAGES/`

### French (fr)
- ⏳ Structure ready
- ❌ Content needs migration from .po files
- Total: 71 .po files in `docs/locales/fr/LC_MESSAGES/`

### Portuguese (pt)
- ⏳ Structure ready
- ❌ Content needs migration from .po files
- Total: 71 .po files in `docs/locales/pt/LC_MESSAGES/`

### Russian (ru)
- ⏳ Structure ready
- ❌ Content needs migration from .po files
- Total: 71 .po files in `docs/locales/ru/LC_MESSAGES/`

## 🎯 Milestone Goals

### Milestone 1: Basic Migration ✅
- Convert all RST to Markdown
- Set up MkDocs configuration
- Get builds working
- Update ReadTheDocs config

### Milestone 2: Content Review (Current)
- Review converted content
- Fix any conversion issues
- Test all features work
- Fix broken links

### Milestone 3: Translations
- Migrate translations from .po to Markdown
- Test all language versions
- Verify content accuracy

### Milestone 4: Production Ready
- All tests passing
- All languages complete
- ReadTheDocs deployment successful
- Documentation reviewed by team

## 🚀 Deployment Plan

1. **Staging**: Test on a branch/fork
2. **Review**: Team reviews the new MkDocs site
3. **Parallel run**: Keep Sphinx running while testing MkDocs
4. **Switch**: Update main branch and ReadTheDocs points to MkDocs
5. **Monitor**: Watch for any issues in first week
6. **Cleanup**: Remove old Sphinx files after successful migration (optional)

## 💡 Tips

- Keep the Sphinx files for now as backup
- Test thoroughly before switching ReadTheDocs
- Consider a "preview" deployment to a different URL first
- Document any custom changes for future reference
- Set up CI/CD to automatically test builds on PRs

## 📞 Resources

- MkDocs Docs: https://www.mkdocs.org/
- Material Theme: https://squidfunk.github.io/mkdocs-material/
- i18n Plugin: https://github.com/ultrabug/mkdocs-static-i18n
- Migration Guide: See `MKDOCS_MIGRATION.md`
- Quick Start: See `QUICKSTART.md`
