-------------------------------------------------INSTALLATION-------------------------------------------------

Installing python (Platform specific):
> Installation link- 'https://www.python.org/downloads/'

Installing postgreSQL (Platform specific)
> Installation link- 'https://www.enterprisedb.com/downloads/postgres-postgresql-downloads'

Installing pgAdmin (UI for postgreSQL, Platform specific):
> Installation link- 'https://www.pgadmin.org/download/'

Installing mongoDB Shell:
> Installation link- 'https://www.mongodb.com/try/download/shell'

Installing mongoDB Compass (UI for mongoDB):
> Installation link- 'https://www.mongodb.com/try/download/compass'

Set postgreSQL and mongoDB path in your environment variables:
NOTE: Variable name should be path and the value should be the directory where the respective softwares are installed.
> PostgreSQL
    name: path
    value: C:\Program Files\PostgreSQL\15\bin
  MongoDB
    name: path
    value: C:\Program Files\MongoDB\Server\6.0\bin
  Python
    name: path
    value1: C:\Users\Kaustubha Rao\AppData\Local\Programs\Python\Python311\Scripts
    value2: C:\Users\Kaustubha Rao\AppData\Local\Programs\Python\Python311

Installing dependencies:
> pip install pandas
> pip install configparser
> pip install rich pyfiglet
> pip install psycopg2
> pip install pymongo
> pip install bson
> pip install unittest

-------------------------------------------------PROGRAM RUN-------------------------------------------------

In order to perform the migration, run the home.py python file.
> python home.py from your terminal

Logs will be displayed in the terminal.