
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
...
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

I've been spending time looking at other examples. Amazing to me that most "real" web
sites use a combination of Oauth and regular accounts, and none of the examples I've
been able to find do.

I think, since I'm basically trying to do the same thing in both python/flask, golang,
and ruby/rails, that I'll see if I can make a tiny sample project in each that does
nothing except user management with a regular login/password and Oauth2. Maybe add a
code generator?

For the moment, I want to focus on actually getting something working specific to
this project, though. I'll try to get the Oauth stuff working by itself, and then
later come back and try to add support for normal accounts/passwords as well.

First up, Facebook integration. It looks like they have a good tutorial for web
Oauth integration here:
https://developers.facebook.com/docs/facebook-login/web

I created apps in both Facebook and Twitter, so I'm ready to try continuing in
the Oauth tutorial from Grinberg.

I made a file called secret_config.py that is included from an environment variable,
WRITERTOYS_SETTINGS that holds the path to the file. That has the API secrets
and database password, etc. That I don't want to check in to github.

I should make a log of all the things that should just happen, but don't because
they're all things you have to go learn in their own context.

You should be able to:
  a) select heroku from a dropdown list, then fill out credentials
  b) select postgres from a dropdown list, then fill out credentials
  c) select Facebook and Twitter (etc.) from a dropdown list, and be guided through getting app IDs, etc.
  d) generate code that makes a basic app, including authentication with Oauth2, login/password

I'm not going to do that now, for this, but it's obviously something that could accelerate new
projects a great deal.

I believe I have all the infrastructure in place now, so all I need to do (in theory)
is wire everything up in the login form.

Not quite -- I forgot I needed to add the "social_id" to the User model. I did that, but
still need to figure out how to get the db_* scripts working with the new "secret" config
stuff that I don't want to check in to github.

For now, I just added a basedir to db_migrate like in config.py, then directly imported
the database URI from app.secret_config. I want that to be in an environment variable,
but I'll figure that out later.

Baby steps today -- need to finish updating login html. Also, figure out where to user g.user
and where to use current_user.

Another step -- now I think I actually need to be running this on my actual domain for the
callback from OAuth to work. Progress!

Looking on Heroku, under tranquil-brook (my app there for this), it turns out that I can
add config values under "settings" -- I'm not sure if that is environment variables or something
else. Also, I've already added a Postgres database, but I don't know yet how to update it
with the latest schema.

It looks like I can get a URL to the postgres database from their web page under my app, and
the password, and then I can connect to it using the code explained here:

https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python

I will need to figure out how to change all of the db_*.py scripts as well as the app
to use that URL and password, using an environment variable for each.

The configuration section on Heroku to set variables under here, and already has DATABASE_URL,
so I think it's very likely that it's setting environment variables:
https://dashboard.heroku.com/apps/tranquil-brook-1024/settings

I'm going to try using the remote (heroku) database from the db_migrate scripts. Here goes nothing!

[x] modify app/secret_config.py to use DATABASE_URL as seen in the heroku project settings
[x] modify db_create.py and db_migrate.py to use postgres database on heroku
[x] run db_create.py and db_migrate.py
[x] look at database on heroku using postico (wow, it somehow knew all the connection info -- must have already done something)

I fiddled around on the heroku web page, when I got an error the first time, and then it opened a sample page:

source source_me
source source_me.private
heroku ps:scale web=1 --app tranquil-brook-1024
heroku open --app tranquil-brook-1024
heroku logs --app tranquil-brook-1024

That opened the web page: https://tranquil-brook-1024.herokuapp.com/

Unfortunately, that didn't look at all like the web page I get when I run run.py locally.

I hadn't added heroku as a remote git repo, so I did:
heroku git:remote -a tranquil-brook-1024

After an enormous amount of git stuff, I think I got the stuff I wanted merged into heroku's git repo,
and now it is broken, but at least the logs show me a hint about what I need to fix:

bash: run.py: command not found
2016-01-22T03:06:25.631384+00:00 heroku[web.1]: State changed from starting to crashed
2016-01-22T03:06:25.632568+00:00 heroku[web.1]: State changed from crashed to starting
2016-01-22T03:06:25.622394+00:00 heroku[web.1]: Process exited with status 127
2016-01-22T03:06:28.476806+00:00 heroku[web.1]: Starting process with command `run.py`
2016-01-22T03:06:30.332711+00:00 app[web.1]: bash: run.py: command not found
2016-01-22T03:06:31.045577+00:00 heroku[web.1]: State changed from starting to crashed
2016-01-22T03:06:31.025317+00:00 heroku[web.1]: Process exited with status 127
2016-01-22T03:06:44.847714+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=tranquil-brook-1024.herokuapp.com request_id=49854e95-5e09-4a34-836a-413b075e3d41 fwd="71.112.205.133" dyno= connect= service= status=503 bytes=
2016-01-22T03:06:52.600477+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=tranquil-brook-1024.herokuapp.com request_id=0785e577-2222-4733-881a-10c00ecaaa72 fwd="71.112.205.133" dyno= connect= service= status=503 bytes=

That's enough for tonight.

