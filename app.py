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
def home():
    return render_template('home.html')

@app.route('/view_all_games_form')
def view_all_games_form():
    return render_template('form.html')

@app.route('/view_all_games', methods=['GET', 'POST'])
def view_all_games():
    # Retrieve the user input from the form
    username = request.form['username']

    return render_template('user_games_dummy.html', username=username)

@app.route('/video_games/<username>')
def video_games(username):
    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SQL query to retrieve the video games and progress for the user
    query = "SELECT videogame, progress FROM games WHERE username = %s"
    cursor.execute(query, (username,))
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Render the video_games.html template with the retrieved data
    return render_template('video_games.html', username=username, rows=rows)

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

# Route to handle editing the username
@app.route('/edit_username', methods=['GET', 'POST'])
def edit_username():
    if request.method == 'POST':
        # Get the current username and the new username from the form data
        current_username = request.form['current_username']
        new_username = request.form['new_username']

        # Perform the necessary logic to update the username in the database
        cursor = conn.cursor()

        # Verify the current username
        sql = "SELECT username FROM users WHERE username = %s"
        cursor.execute(sql, (current_username,))
        result = cursor.fetchone()

        if result:
            # Update the username in the database
            sql = "UPDATE users SET username = %s WHERE username = %s"
            cursor.execute(sql, (new_username, current_username))
            conn.commit()
            conn.close()
            return "Username updated successfully"
        else:
            conn.close()
            return "Incorrect current username"

    # If the request method is GET, render the edit_username.html template
    return render_template('edit_username.html')


if __name__ == '__main__':
    app.run(debug=True)
