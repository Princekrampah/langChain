import sqlite3

conn = sqlite3.connect('product_db.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS products
          (
            [id] INTEGER PRIMARY KEY, 
            [name] TEXT, 
            [supplier] TEXT, 
            [store] TEXT
          )
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS prices
          (
              [id] INTEGER PRIMARY KEY, 
              [price] INTEGER,
              [discount_pcnt] INTEGER
          )
          ''')

conn.commit()
