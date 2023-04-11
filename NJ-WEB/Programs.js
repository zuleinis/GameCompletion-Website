
function Multi(){
    
    let Input = document.getElementById("input");
    let Input2 = document.getElementById("input2");
    let Result = document.getElementById("Multi");

    Result.innerHTML = Input.value * Input2.value;
}

function abs(){
    //https://www.w3schools.com/js/tryit.asp?filename=tryjs_math_abs
    let Input = document.getElementById("inputabs");
    

    document.getElementById("Abs").innerHTML = Math.abs(Input.value);
}
function Max(){
    
    let Input = document.getElementById("inputmax");
    let Input2 = document.getElementById("inputmax2");
    let Result = document.getElementById("Max");

    Result.innerHTML = Math.max(Input.value, Input2.value);
}