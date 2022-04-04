<!DOCTYPE html>
<html>
	<head> 
		<link href="StyleProg.css" rel="stylesheet" type="text/css">
		<meta charset="UTF-8">
		<title>Norberto's Website</title>
	</head>
	
	
	<body>
	
		<header>
			<div class="container">
				<img src="Images/Profile pic Jay Carlton-MUSIC.png" alt="logo" class="logo">
				<nav>
					<ul>
						<li><a href="index.html">Home</a></li>
						<li><a href="CV.html">Curriculm Vitae</a></li>
						<li><a href="Programs.html">Programs</a></li>
						<li><a href="#">ProgramsPHP</a></li>
					</ul>
				</nav>
			</div>
		</header>

		<div class="Image">
			<h1>Norberto Collazo's COMP4036 Website</h1>
		</div>
	
	

			



<form action="Programs.php" method="post">


<p class="text_prog">(Php)Multiplication:</p>

<div class="fancy2">
<input type="number" name="input">
<input type="number" name="input2">
<input type="submit">

</form>

</body>
</html>
<?php
function Multi_Php() {
    $Input = $_POST["input"];
    $Input2 = $_POST["input2"];
    

    echo $Input2*$Input;
}

Multi_Php();

?>
<html>
    <body>
    <form action="Programs.php" method="post">
        <p class="text_prog">(Php)Which is the higher number?:</p>
        <div class="fancy2">
        <input type="number" name="inputmax">
        <input type="number" name="inputmax2">
        <input type="submit">
    </form>
    </body>
</html>
<?php
function MaxI()
{
    $Input = $_POST["inputmax"];
    $Input2 = $_POST["inputmax2"];
    echo(max($Input2, $Input));
}MaxI();
?>
<html>
    <body>
    <form action="Programs.php" method="post">
        <p class="text_prog">(Php)Returning the Absolute (positive) value:</p>
        <div class="fancy2">
        <input type="number" name="inputabs">
        
        <input type="submit">
    </form>
    </body>
</html>
<?php
function AbsI()
{
    $Input = $_POST["inputabs"];
    
    echo(abs($Input));
}AbsI();
?>


	