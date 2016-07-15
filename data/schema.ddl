DROP TABLE IF EXISTS Names CASCADE;
DROP TABLE IF EXISTS RawNames CASCADE;
DROP TABLE IF EXISTS NameTypes CASCADE;
DROP TABLE IF EXISTS NameOrigins CASCADE;

CREATE TABLE RawNames (
    id serial primary key,
    name TEXT
);

CREATE TABLE NameTypes (
    id serial primary key,
    type TEXT
);

CREATE TABLE NameOrigins (
    id serial primary key,
    name TEXT
);

CREATE TABLE Names (
    id serial primary key,
    RawNames_id integer REFERENCES RawNames,
    NameTypes_id integer REFERENCES NameTypes,
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

