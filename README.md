django-travis-selenium-s3-demo
==============================


[![Build Status](https://travis-ci.org/pebreo/django-travis-selenium-s3-demo.png)](https://travis-ci.org/pebreo/django-travis-selenium-s3-demo)

Notes
=====
Keep in mind that since we are using a LiveServerTestCase, so you have to make sure that your database has the right state or else your tests might not pass because it is expecting certain data from the database. In this project, I use the fixtures (initial_data.json) to *create* the sqlite3 db then the functional tests *uses* the sqlite3 database.
