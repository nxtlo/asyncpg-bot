-- just a simple script to make our tables easier :p 

CREATE TABLE IF NOT EXISTS prefixes (
    guild_id Character varying PRIMARY KEY,
    prefix TEXT
);

CREATE TABLE IF NOT EXISTS guilds (
    guild_id Character varying PRIMARY KEY,
    members TEXT
);