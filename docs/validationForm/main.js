// Tag all our id and classes from the HTML
// let username = document.getElementById('username');
// let email = document.getElementById('email');
// let password = document.getElementById('password');
const inputs = [...document.getElementsByTagName('input')];

// An other way to declare the three variables
// let username = document.getElementById('username'),
//    email = document.getElementById('email'),
//    password = document.getElementById('password');

// Or we can use an arrow function. Remember we need to add the 'return' at the end or the function will not work
// but if is it only one line, we don´t need the 'return'
// let id = () => {
   // we are going to pass the 'id' as the argument
   // return document.getElementById()
// }

let id = (id) => document.getElementById(id)
// to pass our id we change the variable declaration to
let username = id('username'),
   email = id('email');
   password = id('password');

console.log(inputs)
// here we can see that at the console we have the input with the id = username
console.log(username)

// ESTOY EN EL MIN 53
