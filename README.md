# HTS_website_UCR
Submission form for sequencing center at UCR

## Initial Setup Instructions

Clone the repo and `cd` into the cloned folder.

1. `cd hts_site`
2. Create a virtualenv __[Optional, recommended]__
3. Install the required dependencies using `pip install -r requirements.txt`
4. Run the database migrations for the site: `python manage.py migrate`
    - If running in production, the database settings should be changed before running this command.
    - If running in production, **make sure you change the SECRET_KEY in `settings.py`**
5. Start the site: `python manage.py runserver`


## Site Setup Instructions

These steps are to be completed after setting up the database and the site:

1. Make a new admin user: `python manage.py createsuperuser`
2. Add any static pages. Note that Bootstrap tags will work and as it is already imported.
3. Create endpoints for the Management and Api AppHooks
    - The API endpoint (named `Management` in the UI) should have a slug of `api`.
    - The Display endpoint should have a slug of `view`. __[Optional, recommended]__
4. Publish the pages created in step 3 to make them visible to users.
