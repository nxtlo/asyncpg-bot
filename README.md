## This repo is still unfinished but will give you and idea about how to make a discord bot using discord.py and asyncpg


### Requirements

* [PostgreSQL](https://www.postgresql.org/download/) >= 9.5 the database we're using.
* [asyncpg](https://github.com/MagicStack/asyncpg) an Asynchronous python library designed for PostgreSQL


### Setting up a venv

```
# Windows
py -3 -m venv venv

# Linux
python3 -m venv venv
```

### Access the venv

```
# Windows 
/venv/Scripts/activate

# Linux
source venv/bin/activate
```


### Installing dependencies
```
# Windows
py -m pip install -U -r requirements.txt

# Linux
python -m pip install -U -r requirements.txt
```

### Running the bot
```
# Windows 
py bot.py

# Linux
python bot.py
```