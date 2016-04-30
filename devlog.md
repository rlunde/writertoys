
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
since that seems to be going away. 

* I deleted a bunch of stuff about Heroku deployment, since I decided not to go that way

Note: I forgot I'd already done: virtualenv flask

I did:

$ pip freeze
$ source flask/bin/activate
$ pip install -r requirements.txt --allow-all-external

Now I can run ./run.py (after the source flask/bin/activate) and it runs from the local python virtual environment.

I want to use Postgres rather than sqlite for this 

For now, I just added a basedir to db_migrate like in config.py, then directly imported
the database URI from app.secret_config. I want that to be in an environment variable,
but I'll figure that out later.

Baby steps today -- need to finish updating login html. Also, figure out where to use g.user
and where to use current_user.

OK, I've let myself get sidetracked (in several projects), by spending way too much time
trying to figure out how to get things working on heroku, when I don't want to run it there myself in the
longer term, anyway, and I don't want people who start with my repo to have to figure out how to move
it elsewhere. So I'm looking at alternatives that are more just a regular VM (linode, digital ocean, aws)
and plan to start over with that.

No matter where I deploy this, I will need some login management, so here is another alternative to look at:
https://flask-login.readthedocs.org/en/latest/
http://gouthamanbalaraman.com/blog/minimal-flask-login-example.html
https://realpython.com/blog/python/using-flask-login-for-user-management-with-flask/

The last link looks like it may have most of the pieces.

I'm starting over again. This time just using the flask documentation itself, and not being
so impatient.

First: 
$ sudo -H pip install virtualenv

(But I had it already installed, from the first time.)

$ pip install --upgrade virtualenv
...took me from 13.1.2 to 15.0.1

Then:
$ virtualenv venv
$ . venv/bin/activate
$ pip install Flask

The latter said:
Successfully installed Flask-0.10.1 Jinja2-2.8 MarkupSafe-0.23 Werkzeug-0.11.5 itsdangerous-0.24

Next I'm going to start via the quickstart section: http://flask.pocoo.org/docs/0.10/quickstart/

It looks like the next thing to do is just make a static layout of the index page.

It looks like I just need to put all such things under a /static directory, for now.

I decided to work on the HTML a little, just to get layout going. I created a templates directory
and made an index.html based on a Flask React tutorial and a React tutorial.

I think I should start with a standard Bootstrap layout for navbar and menus and such.
https://getbootstrap.com/components/#navbar

I added a template (with just HTML so far) with a Bootstrap menu, that I still need to
style as well as hook anything up to.

I'm not so sure this is a great time to learn React, since I'm just learning Flask, but I
won't give up just yet.

I'm starting from here: https://realpython.com/blog/python/the-ultimate-flask-front-end/

