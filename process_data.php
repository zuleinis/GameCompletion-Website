<?php
// Retrieve the user input from the form
$username = $_POST['username'];

// Create a connection to the database
$db_host = 'localhost';
$db_user = 'your_database_username';
$db_pass = 'your_database_password';
$db_name = 'your_database_name';
$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);

// Check if the connection was successful
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Create a query to search for the username and videogame in the database
$sql = "SELECT * FROM games WHERE username='$username'";
$result = mysqli_query($conn, $sql);

// Check if the query was successful
if (!$result) {
    die("Query failed: " . mysqli_error($conn));
}

// Display the results of the query
if (mysqli_num_rows($result) > 0) {
    while ($row = mysqli_fetch_assoc($result)) {
        echo "Username: " . $row['username'] . "<br>";
        echo "Other data: " . $row['other_data'] . "<br>";
    }
} else {
    echo "No results found.";
}

// Close the database connection
mysqli_close($conn);
?>
