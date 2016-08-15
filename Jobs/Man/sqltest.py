# Write an sql query to find books that have sold fewer than 
# 10 copies in the last year, excluding books that have been 
# available for less than 1 month.
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("""create table products
             (product_id number primary key,
              name varchar(128) not null,
              rrp number not null,
              available_from date not null)
             """)

c.execute("""create table orders
             (order_id number primary key,
              product_id number not null,
              quantity number not null,
              order_price number not null,
              dispatch_date date not null,
              foreign key (product_id) references product(product_id))
          """)

# Populate products table
c.execute("INSERT INTO products VALUES ('101','Bayesian Methods','94.95', '2016-08-09')")
c.execute("INSERT INTO products VALUES ('102','Next Year In Review','21.95', '2017-01-01')")
c.execute("INSERT INTO products VALUES ('103','Learn Python In 10 Minutes','2.15', '2016-05-01')")
c.execute("INSERT INTO products VALUES ('104','Sports Almanac','3.38', '2014-08-01')")
c.execute("INSERT INTO products VALUES ('105','Finance for Dummies','84.99', '2015-08-01')")

# Populate orders table
c.execute("INSERT INTO orders VALUES ('1000','101','1', '90.0', '2016-06-01')")
c.execute("INSERT INTO orders VALUES ('1001','103','1', '1.15', '2016-06-15')")
c.execute("INSERT INTO orders VALUES ('1002','101','10', '90.0', '2015-09-15')")
c.execute("INSERT INTO orders VALUES ('1003','104','11', '3.38', '2016-02-15')")
c.execute("INSERT INTO orders VALUES ('1004','105','11', '501.33', '2014-08-15')")

# Query books that have sold fewer than 10 copies in the last year, excluding books which
# have been available for less than one month
for row in c.execute("""
                     SELECT name, sum(quantity) as sum_quantity FROM
                     products inner join orders on (orders.product_id == products.product_id)
                     where products.available_from < datetime('now', '-1 month')
                     group BY orders.product_id having sum_quantity < 10
                     """):
    print row

conn.commit()
conn.close()
