I think it may be easiest to evolve the website by:

 1. write a command line interface that does the operations
 2. convert the CLI into a shell and a library that implements the API
 3. call the API from a web interface

This part is just step 1.

I'm starting with name generation. I only realized how hard it would
be to do a random selection from a database after I loaded the database.
Databases don't generally have a way to get a random row of a table,
and I designed the schema to put all the names in one table, whether
male, female, first, or last.

I think what I'll try (nothing I've thought of so far will be efficient)
will be:

 1. count the number of records in the names table
 2. choose N (e.g. 25) random integers between 1 and Count
 3. select rows that have the right gender and type that are in the list of random numbers
 4. if none, select all rows of the right gender and type into an array
 5. pick a random array element

If this was going to be persistent, I'd just do 4 and 5 for everything. Maybe
I should start off that way, since we'll want the web app to do that anyway?


