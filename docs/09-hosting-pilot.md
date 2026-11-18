# Hosting the pilot

Version 0.1, 18 Nov 2026. Draft. Needs two choices from the project owner (see the end). Nothing here is a clinical claim.

## What is hosted

`dist/app/` is a folder of static files (course app, sweep trainer, pilot test page). It needs no database. It works from any web server that can serve files over HTTPS; the app installs and runs offline after the first visit.

## Rules

1. The whole folder sits behind a password. The pilot test must not be reachable by anyone who has not been invited.
2. Clips never pass through this repository. They are copied to the server by hand into `media/` (below). `tools/deploy_pilot.sh` excludes `media/`, so a later upload does not delete them.
3. Only anonymised clips (rule 6 of CLAUDE.md). Check each clip once more before upload.
4. HTTPS only.

## Steps

1. Build: `python tools/build.py`
2. On the server, create the folder (for example `fetal-echo-pilot` under the web root of the chosen site).
3. Password. Apache: in that folder create `.htpasswd` with `htpasswd -c .htpasswd learner01` (add more users without `-c`), and `.htaccess`:

       AuthType Basic
       AuthName "Fetal echo pilot"
       AuthUserFile /full/path/to/fetal-echo-pilot/.htpasswd
       Require valid-user

   Nginx: use `auth_basic` and `auth_basic_user_file` in the location block. On a WordPress host with cPanel, "Directory Privacy" does the same without editing files. Give each learner their own login (a code, not a name) so results stay under a code.
4. Upload: `tools/deploy_pilot.sh user@host:/path/to/fetal-echo-pilot --dry-run`, then again without `--dry-run`. If the host offers only FTP or a file manager, upload the contents of `dist/app/` by hand, except any `media/` folder.
5. Clips: on the machine at the clinic run `python tools/clinic/build_media.py clean` (it writes `clean/media.json` and lists only clips checked by two different people). Copy the clip files and `media.json` into a folder `media` beside `index.html` on the server (pilot clips in `media/pilot`) with the host's file manager or `scp -r`. See `tools/clinic/README.md`, section 3.
6. Check: open the address in a private window. It must ask for a password. Log in; open the app, the sweep trainer and the test page; confirm clips play. Then try the address without logging in from a phone on mobile data.
7. After the pilot, delete `media/` and the learner logins from the server.

## Two choices needed from the project owner

- Where: a folder or subdomain on the clinic website host, or a separate small host.
- Password: one shared login, or one per learner (recommended, since results are by code).

Note: the clinic hub sites are WordPress; the app should live in its own folder or subdomain, not inside a WordPress page, so the service worker and offline mode work.
