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

cur.execute('drop table vin')

cur.execute('''create table vin(
    Name varchar(150),
    Rating varchar(150),
    Region varchar(150),
    Year varchar(150),
    atavg varchar(150),
    atmin varchar(150),
    atmax varchar(150),
    aprcp varchar(150),
    btavg varchar(150),
    btmin varchar(150),
    btmax varchar(150),
    bprcp varchar(150),
    ctavg varchar(150),
    ctmin varchar(150),
    ctmax varchar(150),
    cprcp varchar(150),
    dtavg varchar(150),
    dtmin varchar(150),
    dtmax varchar(150),
    dprcp varchar(150),
    etavg varchar(150),
    etmin varchar(150),
    etmax varchar(150),
    eprcp varchar(150),
    ftavg varchar(150),
    ftmin varchar(150),
    ftmax varchar(150),
    fprcp varchar(150),
    Predictions varchar(150)
    )''')
    


f = open(r'C:\Users\Magnus\Documents\Code\gradproj\sql\preditions.csv', 'r')
cur.copy_from(f, 'vin', sep=';')
f.close()

