
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



