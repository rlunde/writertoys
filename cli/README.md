I think it may be easiest to evolve the website by:

 1. write a command line interface that does the operations
 2. convert the CLI into a shell and a module that implements the API
 3. call the API from a web interface

This part is just step 1.

I'm starting with name generation. I only realized how hard it would
be to do a random selection from a database after I loaded the database.
Databases don't generally have a way to get a random row of a table,
and I designed the schema to put all the names in one table, whether
male, female, first, or last.

I ended up just loading the whole thing into memory, then picking
a random sample. This should work OK for this use case, in a web
app, since the name data isn't going to change between requests,
so it can be cached, and it's not big enough to worry about caching
it.

Next step: convert to a shell and a module.

I think I'll stick with modules for now, rather than go all the way to
making a package.

