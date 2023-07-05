import sqlite3

conn = sqlite3.connect('product_db.db') 
c = conn.cursor()
                   
c.execute('''
          INSERT INTO products (id, name, supplier, store)

                VALUES
                (1,'Iphone', 'Apple', 'Nairobi'),
                (2,'MacBook', 'Apple', 'Mombasa'),
                (3,'Tablet', 'Samsung', 'Nairobi'),
                (4,'Desk', 'DELL', 'New York'),
                (5,'Ipod', 'Apple', 'New Delhi')
          ''')

c.execute('''
          INSERT INTO prices (id, price, discount_pcnt)

                VALUES
                (1,1000, 5),
                (2,3000, 7),
                (3,2300, 10),
                (4,1500, 12),
                (5,3500, 3)
          ''')

conn.commit()