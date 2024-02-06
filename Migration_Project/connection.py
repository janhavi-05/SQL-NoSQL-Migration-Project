import psycopg2
import psycopg2.extras
import pymongo
from bson.json_util import dumps, loads
import colors as c

def connectDB(dbName,mongodb_host,sqlPassword):
    try:
        print(f"{c.bcolors.HEADER}Initializing database connections...{c.bcolors.ENDC}")
        
        #Postgres connection
        print(f"{c.bcolors.OKCYAN}Connecting to PostgreSQL server...{c.bcolors.ENDC}")
        pgsqldb = psycopg2.connect(database=dbName,user="postgres",password=sqlPassword)
        cursor = pgsqldb.cursor()
        print(f"{c.bcolors.OKGREEN}Connection to Postgres db succeeded.{c.bcolors.ENDC}")

        #MongoDB connection
        print(f"{c.bcolors.OKCYAN}Connecting to MongoDB server...{c.bcolors.ENDC}")
        myClient = pymongo.MongoClient(mongodb_host,tls=False, tlsAllowInvalidCertificates=True)
        print(f"{c.bcolors.OKGREEN}Connection to MongoDB Server succeeded.{c.bcolors.ENDC}")
        print(f"{c.bcolors.HEADER}Database connections initialized successfully.{c.bcolors.ENDC}")
        
        return [myClient,cursor]
    
    except Exception as e:
        print(f"{c.bcolors.FAIL} {e} {c.bcolors.ENDC}")
        return -2