import mysql.connector
from mysql.connector import errorcode
from parameter import get_para

class record:   
    
    def __init__(self):
        pass
    
    
    def setting(self):
        try:
            cnx = mysql.connector.connect(user='', password='', host='')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print('successfully connected to mysql service.')
            
        cursor = cnx.cursor()
        
        #create database if not exist---------------------------------------------------------------------------
        DB_NAME = get_para('DATABASE_NAME')
        def create_database(cursor):
            try:
                cursor.execute(
                    " CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8' ".format(DB_NAME))
            except mysql.connector.Error as err:
                print("Failed creating database: {}".format(err))
                exit(1)

        try:
            cursor.execute("USE {}".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print("Database {} created successfully.".format(DB_NAME))
                cnx.database = DB_NAME
            else:
                print(err)
                exit(1)
        return cursor, cnx
    
    
    def create_table(self, cursor, name):
        TABLES = {}
        TABLES[name] = (
            f"CREATE TABLE {name} ("
            "  `id` int NOT NULL,"
            "  `questions` varchar(1000) NOT NULL,"
            "  `optionA` varchar(100) NOT NULL,"
            "  `optionB` varchar(100) NOT NULL,"
            "  `optionC` varchar(100) NOT NULL,"
            "  `optionD` varchar(100) NOT NULL,"
            "  `answer` varchar(100) NOT NULL,"
            "  `explaintion` varchar(1000) NOT NULL,"
            "  `date` DATETIME,"
            "  PRIMARY KEY(`id`)"
            ") ENGINE=InnoDB")


        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else: 
                    print(err.msg)
            else:
                print("OK")
    
        
    def append(self, cursor, cnx, content, which_table):
        add_product = (f"INSERT ignore INTO {which_table}"
                       "(id, questions, optionA, optionB, optionC, optionD, answer, explaintion, date) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(add_product, content)
        cnx.commit()  
        print(f'successfully append items to {which_table}')
        # cursor.close()
        # cnx.close()
              
              
    def fetch(self, cursor, cnx, which_table, which_item, criteria): 
        #items:(id, questions, optionA, optionB, optionC, optionD, answer, explaintion, date)
        if criteria:
            query = (f"SELECT {which_item} FROM {which_table} WHERE {criteria}")
        else:
            query = (f"SELECT {which_item} FROM {which_table}")
        cursor.execute(query)
        box = []
        for goals in cursor:
            box.append(goals)
        # cursor.close()
        # cnx.close()
        return box


    def delete(self, cursor, cnx, which_table, criteria):
        delete_query = ( f"DELETE FROM {which_table} WHERE {criteria}" )
        cursor.execute(delete_query)
        cnx.commit()
        # print(f"Deleted content from {which_table}")
        
        
    def show_tables(self, cursor):
        cursor.execute("SHOW TABLES")
        existed_tables = []
        for table in cursor:
            table = str(table[0])
            existed_tables.append(table)
        return existed_tables