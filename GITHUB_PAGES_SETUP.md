# GitHub Pages Setup Guide

This documentation is now configured to automatically deploy to GitHub Pages instead of ReadTheDocs.

## 🚀 Quick Setup

### One-Time GitHub Settings

1. **Go to your repository on GitHub**: https://github.com/UNDP-UNBL/elsa-documentation

2. **Go to Settings → Pages** (left sidebar)

3. **Configure Source:**
   - Source: `Deploy from a branch`
   - Branch: `gh-pages`
   - Folder: `/ (root)`

4. **Save** the settings

That's it! The GitHub Action will handle everything else automatically.

## 📦 What Happens When You Push

When you push to the `main` branch:

1. **GitHub Action triggers** automatically
2. **Builds the site** using MkDocs
3. **Deploys to `gh-pages` branch**
4. **GitHub Pages serves** the static site

**Build time**: ~2-3 minutes
**Live URL**: https://undp-unbl.github.io/elsa-documentation/

## 🌍 Multi-Language Support

All 5 languages are automatically deployed:
- 🇬🇧 English: https://undp-unbl.github.io/elsa-documentation/
- 🇪🇸 Spanish: https://undp-unbl.github.io/elsa-documentation/es/
- 🇫🇷 French: https://undp-unbl.github.io/elsa-documentation/fr/
- 🇵🇹 Portuguese: https://undp-unbl.github.io/elsa-documentation/pt/
- 🇷🇺 Russian: https://undp-unbl.github.io/elsa-documentation/ru/

## 🔄 Deployment Workflow

```
Push to main
    ↓
GitHub Actions triggered
    ↓
Install Python & dependencies
    ↓
Run mkdocs gh-deploy
    ↓
Build site to gh-pages branch
    ↓
GitHub Pages serves site
    ↓
Live in ~2-3 minutes
```

## 📁 Files Created

- **`.github/workflows/deploy.yml`** - GitHub Actions workflow
- **`gh-pages` branch** - Created automatically (contains built site)

## ✅ Verification

After pushing to main, check:

1. **Actions Tab**: https://github.com/UNDP-UNBL/elsa-documentation/actions
   - Should show "Deploy MkDocs to GitHub Pages" running
   - Wait for green checkmark ✅

2. **Visit Site**: https://undp-unbl.github.io/elsa-documentation/
   - Should display your documentation
   - Test language switcher
   - Check images and navigation

## 🔧 Manual Deployment (Optional)

You can also deploy manually from your local machine:

```bash
# Activate environment
mamba activate elsa-mkdocs

# Deploy to GitHub Pages
mkdocs gh-deploy

# Or with custom message
mkdocs gh-deploy -m "Updated documentation"
```

This will:
1. Build the site locally
2. Push to `gh-pages` branch
3. GitHub Pages will update automatically

## 🆚 GitHub Pages vs ReadTheDocs

### GitHub Pages (Current Setup)
✅ Completely free
✅ Automatic deployment on push
✅ No account/project setup needed
✅ Fast builds (~2-3 minutes)
✅ Unlimited bandwidth
✅ Multi-language support
✅ Custom domains supported
✅ HTTPS by default

### ReadTheDocs (Previous Setup)
❌ Required paid plan for multi-language
❌ More complex configuration
❌ Account management needed
✅ PDF generation built-in
✅ Versioning features

## 💾 Storage

- **Repository size**: ~50 MB (docs + images)
- **Built site size**: ~30 MB (static HTML)
- **GitHub Pages limit**: 1 GB (plenty of room)

## 🌐 Custom Domain (Optional)

To use your own domain (e.g., docs.unbiodiversitylab.org):

1. **Add CNAME file**:
   ```bash
   echo "docs.unbiodiversitylab.org" > docs/CNAME
   ```

2. **Update mkdocs.yml**:
   ```yaml
   site_url: https://docs.unbiodiversitylab.org
   ```

3. **Configure DNS** at your domain registrar:
   - Add CNAME record: `docs` → `undp-unbl.github.io`

4. **Enable in GitHub Settings → Pages**:
   - Custom domain: `docs.unbiodiversitylab.org`
   - Enforce HTTPS: ✓

## 🐛 Troubleshooting

### Build Fails
- Check Actions tab for error messages
- Verify `requirements.txt` has all dependencies
- Test build locally: `mkdocs build`

### Site Not Updating
- Check Actions tab shows green checkmark
- Wait 2-3 minutes after push
- Hard refresh browser (Ctrl+Shift+R)

### 404 Error
- Verify GitHub Pages is enabled in Settings
- Check branch is set to `gh-pages`
- Make sure first deploy has completed

### Images Not Loading
- Check image paths are relative
- Verify images exist in `docs/` directory
- Test locally with `mkdocs serve`

## 📊 Analytics (Optional)

To add Google Analytics:

Add to `mkdocs.yml`:
```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

## 🔒 Security

- All connections use HTTPS
- No sensitive data in public repository
- GitHub Pages is secure and maintained by GitHub

## 💰 Cost

**Total cost: $0/month**

- GitHub Pages: Free
- GitHub Actions: Free (2,000 minutes/month for public repos)
- Storage: Free (within limits)
- Bandwidth: Free (unlimited)

**Annual savings vs ReadTheDocs paid plan: $600-1,800**

## 📞 Support

- **GitHub Pages Docs**: https://docs.github.com/en/pages
- **MkDocs Deployment**: https://www.mkdocs.org/user-guide/deploying-your-docs/
- **GitHub Actions**: https://docs.github.com/en/actions

## 🎉 Next Steps

1. **Commit these changes**:
   ```bash
   git add .
   git commit -m "Configure GitHub Pages deployment"
   git push origin main
   ```

2. **Watch the Action run**:
   - Go to Actions tab
   - Click on the running workflow
   - Watch the deployment progress

3. **Visit your site**:
   - https://undp-unbl.github.io/elsa-documentation/

4. **Share the URL** with your team!

---

**Note**: The first deployment may take 5-10 minutes. Subsequent deployments are faster (~2-3 minutes).
