import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    database="postgres",
    user='vingutta@vingutta', 
    password='purxJek3ijd956C', 
    host='vingutta.postgres.database.azure.com', 
    port='5432'
)

cur = conn.cursor()
conn.autocommit = True


def query(x):
    cur.execute(
        f"""
        {x}
        """
    )
    return cur.fetchall()
    
