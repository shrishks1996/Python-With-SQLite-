import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Create/connect to a file-based database
conn = sqlite3.connect("sales_trend.db")   # this file will be created in your current folder
cursor = conn.cursor()

#cursor.execute("""
#CREATE TABLE IF NOT EXISTS SalesDB (
#    Product_ID INTEGER PRIMARY KEY,
#    Product_Name TEXT NOT NULL,
#    Unit_Price INTEGER,
#    Quantity INTEGER,
#    Region TEXT)
#""")

"""
# Multiple rows of data
rows_to_insert = [
    (1, "Phone", 10000, 100, "Asia"), (2, "Phone", 86571, 414, "Oceania"), (3, "Keyboard", 82520, 239, "Oceania"), (4, "Keyboard", 64006, 225, "Asia"),
(5, "Accessories", 63377, 309, "Oceania"), (6, "Phone", 99097, 67, "Europe"), (7, "Keyboard", 82236, 406, "Africa"), (8, "Accessories", 29063, 174, "Asia"),
(9, "Earphones", 43572, 470, "South America"), (10, "Mouse", 76577, 109, "Africa"), (11, "Keyboard", 30881, 225, "Africa"), (12, "Accessories", 36982, 443, "Africa"),
(13, "Phone", 29845, 213, "Africa"), (14, "Mouse", 83462, 315, "Oceania"), (15, "Accessories", 10110, 208, "South America"), (16, "Phone", 35640, 490, "Oceania"),
(17, "Earphones", 59917, 243, "Asia"), (18, "Mouse", 41156, 166, "Oceania"), (19, "Phone", 89640, 78, "Europe"), (20, "Keyboard", 88084, 426, "Africa"),
(21, "Laptop", 51814, 69, "North America"), (22, "Accessories", 2053, 179, "North America"), (23, "Laptop", 29834, 182, "Europe"), (24, "Laptop", 53125, 333, "South America"),
(25, "Keyboard", 46227, 135, "South America"), (26, "Keyboard", 85488, 179, "Oceania"), (27, "Keyboard", 75341, 253, "Asia"), (28, "Earphones", 35535, 55, "South America"),
(29, "Mouse", 99393, 241, "Oceania"), (30, "Keyboard", 6632, 415, "Oceania"), (31, "Accessories", 99576, 249, "Oceania"), (32, "Accessories", 78519, 376, "South America"),
(33, "Laptop", 76332, 234, "Africa"), (34, "Mouse", 94842, 178, "North America"), (35, "Earphones", 86044, 262, "North America"), (36, "Accessories", 27675, 403, "Oceania"),
(37, "Mouse", 61606, 69, "Oceania"), (38, "Keyboard", 29799, 248, "Oceania"), (39, "Accessories", 38874, 238, "South America"), (40, "Earphones", 59990, 477, "Asia"),
(41, "Mouse", 61363, 310, "Africa"), (42, "Phone", 57382, 232, "Asia"), (43, "Mouse", 48898, 381, "Europe"), (44, "Earphones", 82369, 295, "Europe"),
(45, "Phone", 79331, 181, "Europe"), (46, "Accessories", 28304, 397, "Africa"), (47, "Mouse", 18837, 499, "Asia"), (48, "Earphones", 91276, 263, "Europe"),
(49, "Accessories", 12224, 209, "Asia"), (50, "Mouse", 46309, 173, "North America")]

# Insert multiple rows in one go
cursor.executemany("INSERT INTO SalesDB (Product_ID, Product_Name, Unit_Price, Quantity, Region) VALUES (?, ?, ?, ?, ?)", rows_to_insert)

# Commit
conn.commit()
print("✅ Multiple rows inserted successfully!")

"""
query1 = "SELECT * FROM SalesDB;"
cursor.execute(query1)
rows = cursor.fetchall()
for row in rows:
    print(row)

query2 = "SELECT * FROM SalesDB WHERE Region = 'Asia';"
cursor.execute(query2)
rows = cursor.fetchall()
for row in rows:
    print(row)

query3 = "SELECT * FROM SalesDB WHERE Product_Name = 'Mouse';"
cursor.execute(query3)
rows = cursor.fetchall()
for row in rows:
    print(row)


query4 = "SELECT Product_Name, SUM(Quantity) AS Total_Qty, SUM(Quantity * Unit_Price) AS Revenue FROM SalesDB GROUP BY Product_Name"
cursor.execute(query4)
rows = cursor.fetchall()
for row in rows:
    print(row)


df = pd.read_sql_query(query4, conn)
print(df)
conn.close()


plt.bar(df['Product_Name'], df['Revenue'])

plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Product Revenue")

plt.show()