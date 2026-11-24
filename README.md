# LumaScore Support

The static website in `docs/` contains the support contact, frequently asked questions, and the app’s privacy policy. All branding and fonts are served locally.

Run `python3 -m http.server 8000 --bind 127.0.0.1 --directory docs` and open [the local preview](http://127.0.0.1:8000/). Run `python3 -m unittest discover -s tests` to check the pages and their links.

## Deploy to GitHub Pages

This repository uses **Settings → Pages → Source → GitHub Actions**. Push to `main` to run the site tests and publish `docs/`. Follow **Actions → Deploy support site to GitHub Pages** for the deployment result. You can also run that workflow manually on `main`.

After a successful deployment, use these addresses in App Store Connect.

- [Support URL](https://lumascore-cmyk.github.io/privacy_policy/)
- [Privacy Policy URL](https://lumascore-cmyk.github.io/privacy_policy/privacy.html)

Keep the online policy in sync with LumaScore’s bundled privacy notice.
