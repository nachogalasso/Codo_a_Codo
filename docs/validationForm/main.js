// Tag all our id and classes from the HTML
// let username = document.getElementById('username');
// let email = document.getElementById('email');
// let password = document.getElementById('password');
const inputs = [...document.getElementsByTagName('input')];
const error = [...document.querySelectorAll('.error')];
const form = document.querySelector('.form-section');
const cancel = document.querySelector('.cancel');


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

// lo que estamos haciendo es crear un arrow function en la cual le vamos a pasar un argumento (id o las clases),
// las cuales luego identificamos en otra variable y lo que va a suceder es que al pasar esas variables en nuestra
// arrow function, va a identificar esa variable y va a tomar el elemento que le corresponda. Así nos evitamos
// una a una las cosas y no repetimos tanto código. 
let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes); 
// to pass our id we change the variable declaration to
let username = id('username'),
   email = id('email'),
   password = id('password'),
   errorMsg = classes('error'),
   successIcon = classes('success'),
   failureIcon = classes('failure');
// we can use the same command to select all the div with the error class, remember that what this does is, we 
// are telling the program that for each variable the class or id is gonna have the name we pass between the ()


// here we can see that at the console we have the input with the id = username

form.addEventListener('submit', (e) => {
	e.preventDefault();

	// engine(username, 0, 'You forgot or wrong username');
	// engine(email, 1, "You forgot or wrong email");
	// engine(password, 2, 'You forgot or wrong password');

	newEngine();
})

  cancel.addEventListener("click", () => {
      for(let i = 0; i < errorMsg.length; i++) {
         errorMsg[i].textContent = ''
      }
      for(let i = 0; i < failureIcon.length; i++) {
         failureIcon[i].style.opacity = '0'
      }
      for(let i = 0; i < successIcon.length; i++) {
         successIcon[i].style.opacity = '0'
      }
  });

// in our eventListener we can use => 
// if (username.value === "") {
// 	errorMsg[0].textContent = "You forgot to enter your username";
// 	successIcon[0].style.opacity = "0";
// 	failureIcon[0].style.opacity = "1";
// } else {
// 	errorMsg[0].textContent = "";
// 	failureIcon[0].style.opacity = "0";
// 	successIcon[0].style.opacity = "1";
// }

// to aviod writing a repeated code we are going to use an arrow function, we pass the variables as arguments
// then this arrow function is pass and we put the values there.
let engine = (id, serial, message) => {
   // to avoid for the user entering white values or spaces, we use .trim() so if the user use a white space the
   // it will work but JS will remove all the white spaces enterend, it will only display the error if the user
   // entered all white spaces.
   if(id.value.trim() === '') {
      errorMsg[serial].textContent = message;
      failureIcon[serial].style.opacity ='1';
      successIcon[serial].style.opacity = '0';
   }else{
      errorMsg[serial].textContent = '';
      failureIcon[serial].style.opacity = "0";
		successIcon[serial].style.opacity = "1";
   }
}


function newEngine() {
   inputs.forEach(item => {
         if (item.id === "username") {
				console.log(item.value);
				engine(username, 0, 'You forgot or wrong username');

				// if(item.value.trim() === '') {
				// 	errorMsg[0].textContent = "You forgot or wrong username";
				// 	failureIcon[0].style.opacity ='1';
				// 	successIcon[0].style.opacity = '0';
				// }else{
				// 	errorMsg[0].textContent = '';
				// 	failureIcon[0].style.opacity = "0";
				// 	successIcon[0].style.opacity = "1";
				// }
			}
         if(item.id === "email") {
            let emailValue = item.value;
            validateEmail(emailValue);
         }
         if(item.id === "password") {
				engine(password, 2, 'You forgot or wrong password');
            let passValue = item.value;
            validatePasswordModerate(passValue)

				// if (item.value.trim() === "") {
				// 	errorMsg[2].textContent = "You forgot or wrong password";
				// 	failureIcon[2].style.opacity = "1";
				// 	successIcon[2].style.opacity = "0";
				// } else {
				// 	errorMsg[2].textContent = "";
				// 	failureIcon[2].style.opacity = "0";
				// 	successIcon[2].style.opacity = "1";
				// }
			}
   })
}

// Email Regex validation
const validateEmail = (emailValue) => {
	const emailRegex =
		/^(([^<>()\[\]\\.,:\s@"]+(\.[^<>()\[\]\\.,:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

	if (emailRegex.test(emailValue)) {
      console.log("email válido");
      errorMsg[1].textContent = "";
      failureIcon[1].style.opacity = "0";
		successIcon[1].style.opacity = "1";
   } else {
      errorMsg[1].textContent = "You forgot or wrong email";
      failureIcon[1].style.opacity = "1";
		successIcon[1].style.opacity = "0";
      console.log("email incorrecto");
   } 
};

// Password Regex Validation
const validatePasswordModerate = (passValue) => {
	//Should have 1 lowercase letter, 1 uppercase letter, 1 number, and be at least 8 characters long
	const passwordRegex =
		/(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.{8,}$/;

	if (passwordRegex.test(passValue)) {
      console.log("password válido");
   } else {
      console.log("password incorrecto");
   }
};