Render deployment notes

1) Environment variables to set on Render:
   - SECRET_KEY: your Django secret key (do not commit)
   - DEBUG: False
   - DATABASE_URL: (optional) Postgres URL; if not set, sqlite (db.sqlite3) will be used
   - ALLOWED_HOSTS: e.g. your-render-service-name.onrender.com

2) Static files
   - whitenoise is included in requirements. Make sure `whitenoise.middleware.WhiteNoiseMiddleware` is enabled in settings if you want to serve static files.

3) Start command
   - Procfile is provided: `web: gunicorn config.wsgi --log-file -`

4) Additional notes
   - If you use Postgres on Render, add `dj-database-url` and `psycopg2-binary` (already in requirements). Update `config/settings.py` to parse DATABASE_URL using `dj_database_url.parse` when DATABASE_URL present.
