-- for database "writertoys"

DROP TABLE IF EXISTS Names CASCADE;
DROP TABLE IF EXISTS RawNames CASCADE;
DROP TABLE IF EXISTS NameTypes CASCADE;
DROP TABLE IF EXISTS NameGenders CASCADE;
DROP TABLE IF EXISTS NameOrigins CASCADE;
DROP TABLE IF EXISTS Edges CASCADE;
DROP TABLE IF EXISTS Nodes CASCADE;

-- just a name (first or last, male or female or either, ...)
CREATE TABLE RawNames (
    id serial primary key,
    name TEXT
);

-- first or last
CREATE TABLE NameTypes (
    id serial primary key,
    type TEXT
);

-- male, female, or either
CREATE TABLE NameGenders (
    id serial primary key,
    type TEXT
);

-- American, Asian, Scandinavian, ...
CREATE TABLE NameOrigins (
    id serial primary key,
    name TEXT
);

-- a name with type, origin, and gender
CREATE TABLE Names (
    id serial primary key,
    RawNames_id integer REFERENCES RawNames,
    NameTypes_id integer REFERENCES NameTypes,
    NameGenders_id integer REFERENCES NameGenders,
    NameOrigins_id integer REFERENCES NameOrigins
);

CREATE TABLE Nodes (
    id serial primary key,
    Name TEXT,
    NodeType TEXT,
    Description TEXT,
    Properties TEXT
);

CREATE TABLE Edges (
    id serial primary key,
    EdgeType TEXT,
    NodeIdFrom TEXT,
    NodeIdTo TEXT,
    Properties TEXT
);

