from home import *
import pandas as pd
from main import *
import configparser
import pyfiglet
import colors as bcolor


def home_page():

    title = pyfiglet.figlet_format('PostgreSQL\nto\nMongoDB', font='slant')
    print(f'{bcolor.bcolors.OKDARKGREY}{title}{bcolor.bcolors.ENDC}')
    
    # read configurations
    config = configparser.ConfigParser()
    config.read('properties.cfg')
    print(f"{c.bcolors.HEADER}Received properties from the file.{c.bcolors.ENDC}")
    Dbname = config.get('GET','DbName')
    schema = config.get('GET','schema')
    mongoHost = config.get('GET','mongoHost')
    mongo_name = config.get('GET','mongo_name')
    sqlPassword = config.get('GET','SQL_DB_PASSWORD')
    filePath = config.get('GET','filePath')

    # read contents of file in binary
    try:
        content = open(filePath, 'rb').read()
        userfile = {'filename':filePath,'content':content}
        df=pd.read_csv(userfile['filename'])
        paths=df.to_string(index=False)
        print(paths)
    except Exception as e:
        print(f"{bcolor.bcolors.FAIL} {e} {bcolor.bcolors.ENDC}")
        return

    isSuccessful=main(Dbname,schema,mongoHost,mongo_name,paths,sqlPassword)
    if(isSuccessful==-1 or isSuccessful==-2):
        print(f"{bcolor.bcolors.FAIL}Migration failed, please retry.{bcolor.bcolors.ENDC}")
          
    else:
        print(f"{bcolor.bcolors.OKGREEN}Migration completed successfully.{bcolor.bcolors.ENDC}")
       
    
if __name__ == '__main__':
    home_page()
