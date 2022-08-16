const userInput = document.getElementById("username");
const passInput = document.getElementById("password");
const reader = document.getElementById("reader");

function login()
{
fetch("/login", {
method: "POST",
headers: {
"Content-Type": "application/json"},
body: JSON.stringify({
"username": userInput.value ,
"password": passInput.value
})
})
.then(function(response){
response.json().then(function(json){
reader.innerHTML = json['result'];
})
})
}