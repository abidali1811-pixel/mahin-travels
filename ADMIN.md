# Admin guide

The admin panel is Django’s built-in staff area. It is login-protected.

Address: http://127.0.0.1:8000/admin/

Sign in with the user you created via `python manage.py createsuperuser`.

## Daily workflow

1. Open **Tours and Travel** on the admin home page.
2. Choose the model you want to change (packages, hotels, transport, gallery, or enquiries).
3. Use **Add**, the pencil icon to **edit**, or the action menu to **delete**.
4. Click **Save**. Changes appear on the public site immediately.

Uncheck **Is published** if you want to hide a record without deleting it.

## Website colors

Open **Website colors** to update the public site's page and section backgrounds,
card background, text colors, primary colors, accent color, and borders. Choose a
color with the swatch picker, then save; the change appears across the public site
on the next page load. Keep text and background colors easy to read together.

## Tour packages and rates

Open **Tour packages**.

- **Per person rate inr** is the public per-person price in Indian Rupees.
- **Typical group size** is only used to show an *example total* (`per person × group size`) on the website.
- Tick **Is featured** to show the package on the home page.
- Fill **Slug** (or let Django fill it from the title). It becomes the page URL, for example `/packages/golden-triangle-classic/`.
- Put one itinerary day per line and one highlight per line.

You can upload a **cover image** file, or leave **cover image url** filled (sample data uses URLs). If both are set, the uploaded file wins.

## Hotels

Open **Hotels**.

- **Price per night inr** is the nightly rate shown on the Hotels page and on each linked package.
- Use the **Packages** boxes to attach a hotel to one or more tours.
- Amenities are a comma-separated list (for example `Wi-Fi, Breakfast, Pool`).

## Cars and buses

Open **Transport options**.

- Set **Transport type** to Car or Bus.
- **Rate per day inr** is the vehicle hire price.
- **Rate per person inr** is the share/seat price (especially useful for buses).
- Attach options to packages the same way as hotels.

## Gallery images

Open **Gallery images**.

- Click **Add gallery image**.
- Enter a title (and optional caption).
- Upload a file in **Image**, *or* paste a public URL in **Image url**.
- **Sort order** controls display order (lower numbers first).
- The home page shows the first eight published images; the Gallery page shows all of them.

Uploaded files are stored on disk under `media/`; the image path and gallery details are saved in PostgreSQL. Back up the `media/` folder along with the database.

## Enquiries (contact form)

Open **Enquiries**.

Every Contact page submission is stored here: name, email, phone, optional package, hotel, transport choice, message, and date.

- Tick **Is read** after you have followed up.
- Fields are read-only so a submission cannot be accidentally rewritten.
- You may delete spam entries.

## Chatbot

The site chatbot does not have its own admin screen. It reads the published packages, hotels and transport rows and sends that catalog to Google Gemini.

If replies say the assistant is not configured, add `GEMINI_API_KEY` to `.env` and restart `runserver`.

## Reloading sample data

```bash
python manage.py seed_data
```

This updates the sample India records by slug/name. It does not remove enquiries or extra records you created yourself.
