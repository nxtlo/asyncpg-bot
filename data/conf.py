

class Database:
    user = '' # user -> Your postgres user.
    password = '' # password -> Your password.
    db = '' # main database name.
    host = '127.0.0.1' # 127.0.0.1 is your localhost/PC connection should be default
    port = '5432' # the default postgres port.

token='YOUR_BOT_TOKEN'

COGS = ( # if you have more cogs just add them here or use a better method like pathlib/os
    'cogs.meta',
    'cogs.info'
)