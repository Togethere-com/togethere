#Togethere

Togethere will be a web app that is kind of like a crowd-sourced travel guide. See togethere.com for more information.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Python](https://www.python.org/)
* [Node.js](http://nodejs.org/) (with NPM)

## Installation

* `git clone https://github.com/Flobin/togethere.git` this repository
* change into the new directory
* (optional) set up a virtual environment
* `pip install -r requirements.txt`
* `cd togethere/static/togethere`
* `npm install`

## Running / Development

* (optional) go into your virtualenv
* `python manage.py runserver`

And if you want to change templates/css:

* `cd togethere/static/togethere`
* `gulp watch`

Manage data in the admin panel:

* `python manage.py createsuperuser`
* go to `http://localhost:8000/admin` and log in

### Running Tests

* `python manage.py test togethere`
* `python manage.py test functional_tests`

### Deploying

To be determined.
