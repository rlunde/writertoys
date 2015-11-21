
I'm using python 2.7.10 on a Macbook Pro as I develop this, and started by installing virtualenv.py for it using:

sudo easy_install virtualenv

I created a flask virtualenv directory (not to be checked in) via:

virtualenv flask

I followed the first two sections in [Miquel Grinberg's tutorial on Flask](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
(except I didn't use his microblog structure). 

...

I followed the next part of Miquel Grinberg's tutorial.

...

Finally starting to get back to the code. Test it so far by executing "run.py" and
then going to http://localhost:5000/login

I'm up to the Database section of the tutorial: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

One problem is that while I want to provide logins to users, I don't want to use OpenID (as in the example),
since that seems to be going away. I'd rather find a simple implementation of Oauth2.

I think I'll try to deploy this on heroku, so I'm also following the instructions on making a default python app on heroku:

https://devcenter.heroku.com/articles/getting-started-with-python
https://devcenter.heroku.com/articles/heroku-postgresql#local-setup

Following the heroku instructions, I got this:
$ heroku create
Creating tranquil-brook-1024... done, stack is cedar-14
https://tranquil-brook-1024.herokuapp.com/ | https://git.heroku.com/tranquil-brook-1024.git
Git remote heroku added

It looks like if I want to replace gunicorn with flask, I'll need to update the procfile:
https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile

Also, to get all the dependencies loaded:
"Heroku recognizes an app as a Python app by the existence of a requirements.txt file in the root directory. 
For your own apps, you can create one by running pip freeze."

Note: I forgot I'd already done: virtualenv flask

I did:

$ pip freeze
$ source flask/bin/activate
$ pip install -r requirements.txt --allow-all-external

Now I can run ./run.py (after the source flask/bin/activate) and it runs from the local python virtual environment.

Cool! Now I can start it locally with "heroku local web"

I want to use Postgres rather than sqlite for this (since that's what heroku needs), so I follow instructions here:
http://killtheyak.com/use-postgresql-with-django-flask/

I did:
$ createuser -s writertoys
$ createdb -U writertoys --locale=en_US.utf-8 -E utf-8 -O writertoys writertoysdb -T template0

I downloaded postico from https://eggerapps.at/postico/ to use to create the tables.

I used psql command "\password writertoys" to change the password to "happy2"

Trying db_create.py as in the tutorial I get:
ImportError: No module named psycopg2

I added this to requirements.txt:
psycopg2==2.6.1

Then I had to modify the PATH to include the bin directory included postgres stuff:
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.4/bin
pip install -r requirements.txt --allow-all-external

That finally installed psycopg2, so I could retry db_create.py, which succeeded (apparently).

Finally, I was able to run ./db_migrate.py and it created the users table!

Added another table, Story, which I expect will hold a JSON blob (hence the text data type)
of things (characters, plots, names, ...) that are "accepted" using the tool.

Added some thoughts about schema to the todo list.

Now I'm up to part 5 of Miquel Grinberg's tutorial, and (as I'd hoped) he's suggesting that
OpenID is not a good way to go, and refers to an OAuth tutorial he wrote. Despite misgivings
based on prior encounters with OAuth, I guess I'll try to tackle that.

Here's what I'm starting with for that:
http://blog.miguelgrinberg.com/post/oauth-authentication-with-flask

I think I'll ignore authorization for right now, and see if I can get some basic layout
working.

I tried adding in some of the later stuff from the tutorial, and got errors I can't yet
understand. I commented out the "@login_required" over index in the views.py file, and
commented out the database calls in the before_request, since it's somehow calling those
even when is_authenticated is False

Ah ha! is_authenticated doesn't mean what it looks like. It means "should this user be
*allowed* to authenticate. So usually you'd return true, no matter what.

I added a little more oauth stuff from Grinberg's tutorial on that, but it is still asking
for the OpenID stuff. Next step is to rip out the remaining OpenID stuff and see if I can
figure out how to mix oauth with regular logins with passwords.

OK, there's probably an example of someone using Flask that has a combination of Oath2 and
regular managed logins, which is what anybody these days wants. I'm going to spend the
rest of my time today looking for that.

Weird. I can't find anything that combines regular login/password management and Oauth, so
I get to have fun combining them myself. This looks like a good starting point for regular
login/password management:

https://github.com/lingthio/Flask-User-starter-app
I'll try combining that with the Oauth stuff from Miquel Grinberg

There are two more things that look like what I might actually want to use:
https://pythonhosted.org/Flask-Security/ -- for normal logins and passwords
https://pypi.python.org/pypi/Flask-Security
https://github.com/mattupstate/flask-security
https://pypi.python.org/pypi/Flask-Social -- for oauth plugged in to flask-security

