import psycopg2 as psql
import main
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query, typ):
        db = psql.connect(
            database=os.getenv('DB_NAME'),
            host=os.getenv("DB_HOST"),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        cursor = db.cursor()
        cursor.execute(query)
        datas = ['CREATE', 'INSERT', 'UPDATE', 'DELETE']
        if typ in datas:
            if typ == 'CREATE':
                db.commit()
                return 'created successful'
            elif typ == 'INSERT':
                db.commit()
                return 'insert successful'
            elif typ == 'UPDATE':
                db.commit()
                return 'update successful'
            else:
                db.commit()
                return 'delete successful'
        elif typ == 'SELECT':
            return cursor.fetchall()
        else:
            print("ERROR")
            return main.main()




