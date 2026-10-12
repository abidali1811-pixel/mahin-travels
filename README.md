# Mahin Travels

A simple India tour-and-travel website built with **Django** (Python) and **PostgreSQL**.

Django is a good fit for this project because it already includes a login-protected admin panel, database migrations, and form handling. That keeps the codebase small while still covering packages, hotels, transport, gallery images, and enquiries.

## What you get

- Public site: home (hero, featured packages, gallery), services (all India tours plus car/bus), hotels, package detail pages, contact form
- Floating Gemini chatbot that answers from live catalog data (tours, hotels, transport, INR rates)
- Admin panel to create, edit and delete records, upload gallery images, and read form submissions
- Sample India travel data you can load in one command

## Requirements

- Python 3.10+
- PostgreSQL 13+
- A Google Gemini API key (for the chatbot)

## Setup

1. Create and activate a virtual environment:

```bash
cd mahin-travels
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. The site defaults to SQLite for a quick local start. To use PostgreSQL instead, create a database (in `psql` or any Postgres client):

```sql
CREATE DATABASE mahin_travels;
```

Create a PostgreSQL role with access to that database and put its credentials in
`.env`. Set `DATABASE_ENGINE=postgresql` when you are ready to use it. With
`DATABASE_ENGINE=sqlite` (the default), Django uses the local `db.sqlite3` file.

4. Copy the environment file and fill in your values:

```bash
copy .env.example .env
```

On macOS/Linux use `cp .env.example .env`. Edit `.env` and set `SECRET_KEY`, Postgres credentials, and `GEMINI_API_KEY`.

5. Run migrations:

```bash
python manage.py migrate
```

6. Load sample India tours, hotels, cars/buses and gallery images:

```bash
python manage.py seed_data
```

7. Create an admin login:

```bash
python manage.py createsuperuser
```

8. Start the server:

```bash
python manage.py runserver
```

On Windows, you can instead double-click `start_website.bat` in File Explorer.
It opens the site in your browser and keeps the server running in a separate
window. Close that server window when you want to stop the site.

Open:

- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Environment variables

See `.env.example`. None of these secrets belong in source code.

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Django secret key |
| `DJANGO_DEBUG` | `True` for local development |
| `ALLOWED_HOSTS` | Comma-separated hostnames |
| `POSTGRES_DB` | Database name |
| `DATABASE_ENGINE` | `sqlite` for a quick local run (default), or `postgresql` |
| `POSTGRES_USER` | Database user |
| `POSTGRES_PASSWORD` | Database password |
| `POSTGRES_HOST` | Usually `localhost` |
| `POSTGRES_PORT` | Usually `5432` |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated full origins for HTTPS deployments, e.g. `https://example.com` |
| `GEMINI_API_KEY` | Google Gemini API key |
| `GEMINI_MODEL` | Model name, default `gemini-2.0-flash` |

## Project layout

```
mahin-travels/
  config/          Django project settings and URLs
  tours/           App: models, views, admin, chatbot, seed command
  templates/       HTML pages
  static/          CSS and JavaScript
  media/           Uploaded files (created at runtime)
  .env.example     Required configuration keys
  ADMIN.md         How to use the admin panel
```

## Using the site

- **Home** shows featured packages and a gallery strip.
- **Services** lists every published India tour plus car and bus rates.
- **Hotels** shows nightly INR prices and which packages they belong to.
- **Contact** saves each enquiry to PostgreSQL (`tours_enquiry` table).
- The **Ask Mahin** bubble sends questions to Gemini using your live catalog.

Admin usage (adding images, editing rates, reading enquiries) is documented in `ADMIN.md`.
