from bson.json_util import dumps, loads
import colors as bcolor


# preprocess to aviod datatype violation error
def pre_process(cursor, result, table_schema, table_name):
    cursor.execute("""set search_path to \'{}\';""".format(table_schema))
    cursor.execute("SELECT  column_name FROM information_schema.columns WHERE table_name = \'{}\' and (data_type='date' or data_type='numeric' or data_type='Decimal' or data_type='time without time zone')".format(table_name))
    ans = []
    ans = cursor.fetchall()

    for check in result:
        for col in ans:
            check[col[0]] = (str)(check[col[0]])


# function to migrate a given tables
def migrate_table(mongodbname,myClient, cursor, data, table_name, table_schema):

    pre_process(cursor, data, table_schema, table_name)

    mydb = myClient[mongodbname]
    mycol = mydb[table_name]

    mycol.delete_many({})    # delete existing documents

    x = mycol.insert_many(data)  # insert the documents

    return len(x.inserted_ids)


# main function to migrate all data from postgres to mongodb
def migrateAll(mongodbname,myClient, schema, cursor, data, tNo, currCollec):
    success_count = 0
    fail_count = 0
    total_count = len(currCollec)
    for c in currCollec:
        try:
            print(f"{bcolor.bcolors.OKCYAN}Processing table: {c}...{bcolor.bcolors.ENDC}")
            inserted_count = migrate_table(
                mongodbname,myClient, cursor, data[tNo[c]], c, schema)
            print(
                f"{bcolor.bcolors.OKGREEN}Processing table: {c} completed. {inserted_count} documents inserted.{bcolor.bcolors.ENDC}")
            success_count += 1
        except Exception as e:
            print(f"{bcolor.bcolors.FAIL} {e} {bcolor.bcolors.ENDC}")
            fail_count += 1

    print(f"{bcolor.bcolors.OKGREEN}{success_count} of {total_count} tables migrated successfully.{bcolor.bcolors.ENDC}")

    if fail_count > 0:
        print(
            f"{bcolor.bcolors.FAIL}Migration of {fail_count} tables failed. See errors above.{bcolor.bcolors.ENDC}")
        return -2
    
