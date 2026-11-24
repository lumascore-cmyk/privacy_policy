# LumaScore Support

The static website in `docs/` contains the support contact, frequently asked questions, and the app’s privacy policy. All branding and fonts are served locally.

Run `python3 -m http.server 8000 --bind 127.0.0.1 --directory docs` and open [the local preview](http://127.0.0.1:8000/). Run `python3 -m unittest discover -s tests` to check the pages and their links.

The directory is ready for GitHub Pages using the `/docs` publishing folder. Use the site root for support and `privacy.html` for the privacy policy. Keep the policy in sync with LumaScore’s bundled privacy notice.
