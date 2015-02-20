# Spacewalls
Scrape space-themed wallpapers from various sources, provide a viewer of images that have been scraped and a cronjob that will update your desktop background to a random image each day.

Instructions for setup

1) Clone this repo and set up a Python virutal environment by running the following in Terminal:

```
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

2) Run the scraper to get the space images. The spiders available are spacex and hubble.

```
cd space_scrape
scrapy crawl spacex -o ../app/static/images/spacex.json
scrapy crawl hubble -o ../app/static/images/hubble.json
```

3) Create a Postgres database 'spacewalls' then create the model for the database in the python interprer as follows.

```
cd ../app
python
from app import db
db.create_all()
exit()
```

4) Run the following command to seed the database.

```
python seed.py
```

5) Generate bundle.js

```
cd ..
npm install
npm start
```

6) Start the web application.

```
python app/app.py
```
