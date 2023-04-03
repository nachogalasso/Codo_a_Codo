const linkList = document.querySelector('.links-list');
const navBtn = document.querySelector('.fa-bars');

function toggleMenu() {
    navBtn.addEventListener('click', ()  => {
        linkList.classList.toggle('show')
    })
}

navBtn.addEventListener('click', toggleMenu)

function handleResize() {
    let navBtn = document.querySelector('.fa-bars');
    if (window.innerWidth > 768) {
        navBtn.removeEventListener('click', toggleMenu);
    }
}

window.addEventListener('resize', handleResize)

// Register form
const inputs = [...document.getElementsByTagName('input')];
const error = [...document.querySelectorAll('.error')];
const form = document.querySelector('.form-section');
const cancel = document.querySelector('.cancel');

let id = (id) => document.getElementById(id);

inputs[1].placeholder = 'Enter your username';
inputs[2].placeholder = 'example@email.com';
inputs[3].placeholder = 'Enter your password here';
inputs[4].placeholder = 'Re-enter your password';

let classes = (classes) => document.getElementsByClassName(classes);
let username = id('id_username'),
    email = id('id_email'),
    password = id('id_password1'),
    password2 = id('id_password2'),
    // confirmPassword = id('confirm-password'),
    errorMsg = classes('error'),
    successIcon = classes('success'),
    failureIcon = classes('failure');

// form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     newEngine();
// })

cancel.addEventListener('click', () => {
    for (let i = 0; i < errorMsg.length; i++) {
        errorMsg[i].textContent = "";
    }
    for (let i = 0; i < failureIcon.length; i++) {
        failureIcon[i].style.opacity = '0';
    }
    for (let i = 0; i < successIcon.length; i++) {
        successIcon[i].style.opacity = '';
    }
})

let engine = (id, serial, message) => {
    if(id.value.trim() === "") {
        errorMsg[serial].textContent = message;
        failureIcon[serial].style.opacity = '1';
        successIcon[serial].style.opacity = '0';
    }else{
        errorMsg[serial].textContent = "";
        failureIcon[serial].style.opacity = '0';
        successIcon[serial].style.opacity = '1';
    }
}

function newEngine() {
    inputs.forEach(item => {
        if(item.id === 'id_username') {
            engine(username, 0, 'You forgot or wrong username');
        }
        if(item.id === 'id_email') {
            engine(email, 1, 'You forgot or wrong email');
            // let emailValue = item.value
            // validateEmail(emailValue)
        }
        if(item.id === 'id_password1') {
            engine(password, 2, 'You forgot or wrong password');
            // let passValue = item.value
            // validatePasswordModerate(passValue)
        }
        if(item.id === 'id_password2') {
            engine(password2, 3, 'You forgot or wrong username');
            // let passValue2 = item.value
            // validateSecondPassword(passValue2, passValue)
            
        }
    })
}

// REGEX Email and Password Validation
// const validateEmail = (emailValue) => {
//     const emailRegex = /^(([^<>()\[\]\\.,:\s@"]+(\.[^<>()\[\]\\.,:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

//     if(emailRegex.test(emailValue)) {
//         errorMsg[1].textContent = "";
//         failureIcon[1].style.opacity = '0';
//         successIcon[1].style.opacity = '1';
//     }else{
//         errorMsg[1].textContent = "You forgot or wrong email";
//         failureIcon[1].style.opacity = '1';
//         successIcon[1].style.opacity = '0';
//     }
// }

// const validatePasswordModerate = (passValue) => {
//     const passwordRegex = /(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.{8,}$/;

//     if(passwordRegex.test(passValue)) {
//         errorMsg[2].textContent = "";
//         failureIcon[2].style.opacity = '0';
//         successIcon[2].style.opacity = '1';
        
//     }else{
//         errorMsg[2].textContent = "You forgot or wrong password";
//         failureIcon[2].style.opacity = '1';
//         successIcon[2].style.opacity = '0';
        
//     }
   
// }

// const validateSecondPassword = (passValue2, passValue) => {
//     if(passValue2 === passValue) {
//         errorMsg[3].textContent = "";
//         failureIcon[3].style.opacity = '0';
//         successIcon[3].style.opacity = '1';
//     }else{
//         errorMsg[3].textContent = "Wrong password";
//         failureIcon[3].style.opacity = '1';
//         successIcon[3].style.opacity = '0';
//     }
// }