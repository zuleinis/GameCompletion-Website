from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Create a connection to the database
# db_host = 'localhost'
# db_user = 'your_database_username'
# db_pass = 'your_database_password'
# db_name = 'your_database_name'
# conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/view_all_games', methods=['POST'])
def view_all_games():
    # Retrieve the user input from the form
    username = request.form['username']

    # Check if the connection was successful
    if not conn:
        return "Connection failed"

    # Create a query to search for the username and videogame in the database
    sql = "SELECT * FROM games WHERE username=%s"
    cursor = conn.cursor()
    cursor.execute(sql, (username))
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

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Get username from the form data
        username = request.form['username']

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the SQL query to insert the username into the users table
        query = "INSERT INTO users (username) VALUES (%s)"
        cursor.execute(query, (username,))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Redirect to the homepage
        return redirect('/')

    # If the request method is GET, render the add_user.html template
    return render_template('add_user.html')

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):

    # Create a cursor object
    cursor = conn.cursor()

    # Get the current username from the database
    query = "SELECT username FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    row = cursor.fetchone()
    current_username = row[0]

    if request.method == 'POST':
        # Get the new username from the form data
        new_username = request.form['username']

        # Update the username in the database
        query = "UPDATE users SET username = %s WHERE id = %s"
        cursor.execute(query, (new_username, user_id))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Redirect to the homepage
        return redirect('/')

    # If the request method is GET, render the edit_user.html template
    return render_template('edit_user.html', username=current_username)

if __name__ == '__main__':
    app.run(debug=True)
