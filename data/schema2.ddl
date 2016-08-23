-- for database "writertoys"

DROP TABLE IF EXISTS Names CASCADE;
DROP TABLE IF EXISTS Edges CASCADE;
DROP TABLE IF EXISTS Nodes CASCADE;

-- a name with type, origin, and gender
CREATE TABLE Names (
    id serial primary key,
    name TEXT,
    type TEXT, -- e.g. first, last
    gender TEXT, -- e.g. male, female, any
    origin TEXT -- e.g. country
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

