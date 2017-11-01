select rawnames.name from names, namegenders, nametypes, rawnames where
  rawnames.id = names.rawnames_id
  and names.nametypes_id = nametypes.id
  and nametypes.type = 'first'
  and rawnames.id in [1,2,3,4];

