'''
Created on 1 May 2020

@author: shree

Modified by Zijian on Aug 2022
'''

import psycopg2


def create_connection(host="localhost", database="Prac3", user="p3", password='infs3200'):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)  # if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print('PostgreSQL database version:')
    print(db_version)
    return conn
