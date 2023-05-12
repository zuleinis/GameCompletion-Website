import pymysql

# Create a connection to the database
db_host = 'csmath.uprm.com'
db_user = 'zuleinisrl'
db_pass = 'comp4018'
db_name = 'db_ZuleinisNorbertoJose'
conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)

cursor = conn.cursor()

# Execute the SQL query to retrieve the video games and progress for the user
query = "SELECT * FROM `VideoGame` WHERE 1 "
cursor.execute(query)
rows = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

for row in rows:
    print(row)