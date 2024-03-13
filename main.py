import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql
from tabulate import tabulate


def connect_do_db():
    try:
        conn = pg.connect(host='127.0.0.1',
                                port = 5432,
                                dbname='postgres',
                                user='postgres',
                                password='postgres', 
                                )
        my_table    = pd.read_sql('select * from books', conn)
        print(my_table)
    except:
        print('Can`t establish connection to database')

connection = connect_do_db()
# connection.cursor()

class Order:
    def __init__(self,id,title,author,description,price,availability):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.availability = availability

class Check(Order):
    def check(self):
        check = f'select * from books'
        print(check)

class Add(Order):
    def add(self):
        pass

class Delete(Order):
    def delete(self):
        pass

class Update(Order):
    def update(self):
        pass




































# from tabulate import tabulate


# sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
# ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
# ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
# ('Loopback0', '10.1.1.1', 'up', 'up'),
# ('Loopback100', '100.0.0.1', 'up', 'up')]

# print(tabulate(sh_ip_int_br))
# # ---------------  ---------  --  --
# # FastEthernet0/0  15.0.15.1  up  up
# # FastEthernet0/1  10.0.12.1  up  up
# # FastEthernet0/2  10.0.13.1  up  up
# # Loopback0        10.1.1.1   up  up
# # Loopback100      100.0.0.1  up  up
# # ---------------  ---------  --  --