from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/view_all_games', methods=['POST'])
def view_all_games():
    # Retrieve the user input from the form
    username = request.form['username']
    videogame = request.form['videogame']

    # Create a connection to the database
    db_host = 'localhost'
    db_user = 'your_database_username'
    db_pass = 'your_database_password'
    db_name = 'your_database_name'
    conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)

    # Check if the connection was successful
    if not conn:
        return "Connection failed"

    # Create a query to search for the username and videogame in the database
    sql = "SELECT * FROM games WHERE username=%s"
    cursor = conn.cursor()
    cursor.execute(sql, (username, videogame))
    result = cursor.fetchall()

    # Display the results of the query
    if result:
        for row in result:
            print("Username:", row[0])
            print("Videogame:", row[1])
            print("Other data:", row[2])
    else:
        print("No results found.")

    # Close the database connection
    conn.close()
    return "Data processed successfully"

if __name__ == '__main__':
    app.run(debug=True)
