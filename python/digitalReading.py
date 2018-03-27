# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from time import gmtime, strftime

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(4, GPIO.BOTH)

count = 0

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

def my_callback(data):
    print data
    if __name__ == '__main__':
      main()
    GPIO.output(27, GPIO.input(4))
GPIO.add_event_callback(4, my_callback)
