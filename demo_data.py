import sqlite3

conn = sqlite3.connect(r'demo_data.sqlite3')

curs = conn.cursor()

# Create an empty table with columns 's', 'x', 'y'
create_table = ("""
CREATE TABLE IF NOT EXISTS demo(s string, x int, y int);
""")

curs.execute(create_table)

# Determine if the table is empty, if so add some values
if not curs.execute("""SELECT * FROM demo""").fetchall():

    value_insert = ("""
        INSERT INTO demo VALUES
            ('g', 3, 9),
            ('v', 5, 7),
            ('f', 8, 7)
        """)

    curs.execute(value_insert)

    conn.commit()

# Determine the number of rows in the table
row_count = ("""
SELECT count(*) FROM demo;
""")

# Determine rows where 'x', and 'y' are greater than or equal to 5
xy_at_least_5 = ("""
SELECT * FROM demo where x >= 5 AND y >= 5;
""")

# Calculate the number of unique 'y' values
unique_y = ("""
SELECT COUNT(DISTINCT y) FROM demo;
""")

print(curs.execute(row_count).fetchall())
print('----------------------------------')
print(curs.execute(xy_at_least_5).fetchall())
print('----------------------------------')
print(curs.execute(unique_y).fetchall())



