from bson.json_util import dumps, loads
import datetime
from extractSchema import *
from migrateTable import *
from connection import *
from algo import *
from embedAndLinking import *
import colors as c


# fetches access paths from file
def getAccessPaths(file_paths) :
    accessPaths = []
    table = file_paths.split('\n')

    for lines in table:
        lines=lines.strip()
        x = lines.split('/')
        accessPaths.append(x)
    return accessPaths


def pre_process(cursor,result,table_schema,table_name):
  cursor.execute("""set search_path to \'{}\';""".format(table_schema))
  cursor.execute("SELECT  column_name FROM information_schema.columns WHERE table_name = \'{}\' and (data_type='date' or data_type='numeric' or data_type='Decimal' or data_type='time without time zone')".format(table_name))
  ans=[]
  ans=cursor.fetchall()

  for check in result:
    for col in ans:
      check[col[0]]=(str)(check[col[0]])


# main function
def main(dbName, schema, mongodb_host, mongodb_dbname, file_paths, sqlPassword):
    try:
        begin_time = datetime.datetime.now()
        print(f"{c.bcolors.HEADER}Script started at: {begin_time} {c.bcolors.ENDC}")

        # DATABASE CONNECTIONS BEGINS
        [myClient,cursor] = connectDB(dbName,mongodb_host,sqlPassword)

        # Get Access Paths
        paths = getAccessPaths(file_paths)
        print(f"{c.bcolors.WARNING}Received paths: {paths} {c.bcolors.ENDC}")

        # SCHEMA EXTRACTION   
        [tables, tNo, pks,relations] = extractSchema(cursor,schema)
        
        # Algorithm starts 
        [currCollec, relax, work, adj2] = algo(tables, tNo, relations, paths)

        # Embedding and Linking
        data = embedAndLinking(cursor, schema, tables, tNo, relax, pks, work, adj2, relations)

        for t in tables:
            pre_process(cursor,data[tNo[t]],schema,t)

        # Data Migration
        isMigrationSuccess = migrateAll( mongodb_dbname,myClient, schema, cursor, data, tNo, currCollec)
        if(isMigrationSuccess == -2):
           return -2

        end_time = datetime.datetime.now()
        print(f"{c.bcolors.HEADER}Script completed at: {end_time} {c.bcolors.ENDC}")
        print(f"{c.bcolors.HEADER}Total execution time: {end_time-begin_time} {c.bcolors.ENDC}")
        return 1
    except:
        return -1

