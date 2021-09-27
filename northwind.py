import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

curs = conn.cursor()

# Select the top 10 most expensive products
expensive_items = ("""
SELECT * 
FROM Product SORT 
ORDER BY UnitPrice 
DESC LIMIT 10;
""")

# Calculate the average of an employee at hire
avg_hire_age = ("""
SELECT
    (SELECT AVG(HireDate) FROM Employee) 
  - (SELECT AVG(BirthDate) FROM Employee);
""")

# Reselect the top 10 most expensive products and include which supplier sent the product
ten_most_expensive = ("""
SELECT Product.*, Supplier.CompanyName
FROM Product
LEFT JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC 
LIMIT 10;
""")

# Calculate the highest occurring Category of Product
largest_category = ("""
SELECT CategoryId, 
COUNT(CategoryId) 'value_occurrence'
FROM Product
GROUP BY CategoryId
ORDER BY 'value_occurrence' DESC
LIMIT 1
""")

# Execute queries
if __name__ == '__main__':
    queries = [expensive_items, avg_hire_age, ten_most_expensive, largest_category]

    for query in queries:
        results = curs.execute(query).fetchall()
        print(results)
        print('-------------------------')

conn.close()
