django-travis-selenium-s3-demo
==============================


[![Build Status](https://travis-ci.org/pebreo/django-travis-selenium-s3-demo.png)](https://travis-ci.org/pebreo/django-travis-selenium-s3-demo)

Quickstart
=========
Travis CI allows you and your team to automatically run tests on your GitHub repo(s). It makes it easy for your team to identify bugs before you deploy. To automate the process, Travis listens to your GitHub repo for any changes then it spins up a linux virtual machine and does a `git pull` on your repository and runs your tests scripts. You setup your tests scripts in the `.travis.yaml` file.  

The three steps to enable Travis CI automated tests on your repo are:

1) Sign up for a free account at travis-ci.org (if you want a private repo you must pay GitHub and Travis)

2) Create and configure a `.travis.yml` at the top of your repo

3) Tell Travis to listen for any changes in your repo so it can automatically run your tests. To do that, you click `Your name (top right) -> Select which repos to turn ON or OFF` 

Notes
=====
Keep in mind that since we are using a LiveServerTestCase, so you have to make sure that your database has the right state or else your tests might not pass because it is expecting certain data from the database. In this project, I use the fixtures (initial_data.json) to *create* the sqlite3 db then the functional tests *uses* the sqlite3 database.
