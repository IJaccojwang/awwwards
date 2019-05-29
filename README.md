IJAWWWARDS
===================
## Description
IJawwwards is a web application that allows users to share their projects and have them reviewed. The best projects are displayed for users to see.

------------------------------------------------------------------------

## Features

+ [x] Posting projects to be reviewed.
+ [x] Voting on projects.
+ [x] Ranking of projects.
+ [x] User authentication system: login and sign up.
+ [x] Django admin dashboard for site management.



## Getting started

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3

### Cloning the repository
```bash
git clone https://github.com/IJaccojwang/awwwards.git && cd insta-clonewars
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
For this project you will need the following configurations plus email setup for email registration hmac verification.
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running the server
```bash
python manage.py runserver
```

### Admin Dashboard
Use django admin to manage the different users and posts.


## Running the tests
```bash
python manage.py test
```

## Live Demo

The web app can be accessed from the following link:
[IJawwwards](https://ijawwwards.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## Behaviour driven development/ Specifications

| Behaviour |  Sample Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| View Projects | On sign in | All projects displayed |
| Search for projects| Submit search form | All forms meeting the criteria are displayed|
| Post new project | Submit new project upload form| Project uploaded, view on feed|
| Rate a project | Post ratings | Ratings updated|



## Contributing

- Git clone [https://github.com/IJaccojwang/awwwards.git](https://github.com/IJaccojwang/awwwards.git)
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Ian Jaccojwang](https://github.com/IJaccojwang)
