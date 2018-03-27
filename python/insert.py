from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from time import gmtime, strftime

 def insert_count():
  dateTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  query = "INSERT INTO count_passengers (reg_date) " \
          "VALUES('" + dateTime + "')"

  try:
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)

    cursor = conn.cursor()
    cursor.execute(query)

    if cursor.lastrowid:
        print('last insert id', cursor.lastrowid)
    else:
        print('last insert id not found')

    conn.commit()
  except Error as error:
    print(error)

  finally:
    cursor.close()
    conn.close()
 
def main():
   insert_count()
 
if __name__ == '__main__':
  main()