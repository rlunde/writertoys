
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
I copied the requirements.txt file from that project, and installed its dependencies:

./venv/bin/activate
pip install -r requirements.txt

OK, as I feared, that's taking me in a direction I don't want to go, where it seems to be
dragging in a million dependencies again, and wants to do everything in react. One step
forward, two steps back. I'm going to back up again, remove react for now, and just
focus on the functionality I want. So for now, I'll stick with:

1) Flask -- because I want to learn it, and it has good reviews
2) Bootstrap -- because it does a lot of stuff without a lot of dependencies
3) jQuery -- because most things still use it
4) Backbone -- because I want to learn it better, and I like it a lot so far

I also decided to install things locally, but not check them into git. I used bower to
do that, like this:

  npm install -g bower
  bower install --save backbone
  bower install --save bootstrap
  cd bower_components/bootstrap/
  npm install -g grunt-cli
  npm install

Backbone also requires underscore, which I installed with bower.

I used dropdb to drop my old writertoysdb postgres database, since I had deleted all the
migration stuff for it. Then I used "createdb --owner=writertoys writertoysdb" to create
a new one. I changed the password for the postgres writertoys user to "none" for now,
since it's only on my local machine and isn't exposed to the internet. When I create
a database and user on digital ocean, I'll have to figure out a way to keep track of
database credentials.

Miguel Grinberg has a new Flask-Migrate tool, described here:
http://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask

For an initial schema I want a USER table, and tables to support name generation.

Even though I don't like integer IDs, I have to admit that it's pretty unlikely that
I'll need to worry about scalability for any of these tables, so I'll just stick with
defaults for now.

The first version of User I had was:

 class User(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      nickname = db.Column(db.String(64), index=True, unique=True)
      email = db.Column(db.String(120), index=True, unique=True)
      stories = db.relationship('Story', backref='author', lazy='dynamic')
      about_me = db.Column(db.String(140))
      last_seen = db.Column(db.DateTime)

I started off again with:
pip install flask-migrate

I'm using the configuration setup from:
https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

I did:
pip freeze > requirements.txt
pip install autoenv==1.0.0
touch .env

I added this to .env:
source env/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"

I also added that to my "source_me":
export DATABASE_URL="postgresql://localhost/writertoysdb"
export APP_SETTINGS="config.DevelopmentConfig"
source venv/bin/activate

I think to keep things simple, I'll just have a couple of fields for names, besides ID and
the name itself, such as type (first, last), gender (male, female, either), category (european,
asian, ..., fantasy, ...), and tags. Tags might include other things to filter by, so
a "fantasy" name might be tagged with "elf" or "dwarf", etc.

I found a recipe for serving static files and guessing their type, here:
https://codepen.io/asommer70/post/serving-a-static-directory-with-flask

It appears that you're really supposed to use nginx to serve static content, but this will
do for now.

there are a bunch of bootstrap starter templates here:
http://www.bootstrapzero.com/templates/starter

The one I grabbed to start with is here:
http://www.bootstrapzero.com/bootstrap-template/capital-city

I may use some icons from FreePik -- haven't decided yet. Unless I pay, they want
attribution (which makes sense):

<a href='http://www.freepik.com/free-vector/assorted-round-icons_745439.htm'>Designed by Freepik</a>

I also looked at "icons8" but they annoyed me with a bait-and-switch thing, where they implied
you could download vector icons, but when you unpack the download it's all PNG plus a link to
buy the SVG/etc. vector icons for way more than I'd spend on icons for an open source project.

I may just make my own cheesy icons, just for fun.



