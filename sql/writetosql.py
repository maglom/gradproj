import psycopg2
import csv
import sqlalchemy
import pandas as pd

conn = psycopg2.connect(
    database="postgres",
    user='vingutta@vingutta', 
    password='purxJek3ijd956C', 
    host='vingutta.postgres.database.azure.com', 
    port='5432'
)

cur = conn.cursor()
conn.autocommit = True

f = open(r'C:\Users\Magnus\Documents\Code\finalbordeaux.csv', 'r')
cur.copy_from(f, 'viners', sep=';')
f.close()

