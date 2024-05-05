'''
Created on 1 May 2020

@author: shree

Modified by Zijian on Aug 2022
'''
import sys
sys.path.append('/home/s4833842/DataLinkage_py/')
print(sys.path)
import src.psql.DBconnect as db
from src.data.restaurant import restaurant as res
import datetime
import src.data.csv_loader as csv
import src.data.measurement as measure


def nested_loop_by_name(csv_path, benchmark_path):

    # Read data from city is 'new york'
    con = db.create_connection()
    cur = con.cursor()
    string_query = "SELECT * FROM RESTAURANT WHERE city = 'new york'"
    cur.execute(string_query)
    count1 = 0
    for rid, name, address, city in cur:
        count1 += 1
    cur.close()
    con.close()
    print(count1)

    # Read data from city is 'new york city'
    con = db.create_connection()
    cur = con.cursor()
    string_query = "SELECT * FROM RESTAURANT WHERE city = 'new york city'"
    cur.execute(string_query)
    count2 = 0
    for rid, name, address, city in cur:
        count2 += 1
    cur.close()
    con.close()
    print(count2)

    # Count distinct cities
    con = db.create_connection()
    cur = con.cursor()
    string_query = "SELECT * FROM RESTAURANT"
    cur.execute(string_query)
    city_set = set()
    for rid, name, address, city in cur:
        city_set.add(city)
    cur.close()
    con.close()
    print(len(city_set))


# End of function

nested_loop_by_name("/home/uqzwan25/DataLinkage_py/data/restaurant.csv", "/home/uqzwan25/DataLinkage_py/data/restaurant_pair.csv")
