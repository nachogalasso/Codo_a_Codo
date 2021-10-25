/* Let´s bring the elements */
/* NAVBAR ELEMENTS */
const navList = document.getElementById('nav-list');
const iconMenu = document.getElementById('toggle-menu');
const mainLogo = document.getElementById('main-logo');

/* FORM ELEMENTS */
/* Email-Phone option elements */
const phoneBtn = document.getElementById('phoneradio');
const phoneOpt = document.getElementById('phoneopt');
const emailBtn = document.getElementById('emailradio');
/* Form Elements */
const formValidate = document.getElementById('contact-form');
const vBtn = document.getElementById('submitBtn');
const vName = document.getElementById('name');
const vEmail = document.getElementById('email');
const vPhone = document.getElementById('phone');

/* Navbar EVENT */
iconMenu.addEventListener('click', () => {
    mainLogo.classList.toggle('logo-nav');
    navList.classList.toggle('nav-list-show');
});

/* Phone Option */
emailBtn.addEventListener('click', () => {
    phoneOpt.classList.toggle('phone-opt');
})

phoneBtn.addEventListener('click', () => {
    phoneOpt.classList.remove('phone-opt');
})

/* form validation */
const formIsValid = {
    name: false,
    email: false,
    phone: false
}

formValidate.addEventListener('submit', (e) => {
    e.preventDefault()
    validateForm()
})

vName.addEventListener('change', (e) => {
    if(e.target.value.trim().length > 0) formIsValid.name = true;
})

vEmail.addEventListener('change', (e) => {
    if(e.target.value.trim().length > 0) formIsValid.email = true;
})

vPhone.addEventListener('change', (e) => {
    if(e.target.value.trim().length > 0) formIsValid.phone = true;
    formIsValid.phone ? vBtn.removeAttribute('disabled') : 
    vBtn.setAttribute('disabled', true) 

})

/* Form validation */
const validateForm = () => {
    const formValues = Object.values(formIsValid);
    const valid = formValues.findIndex(value => value == false);
    if(valid == -1) {
        formValidate.submit();
        alert('Nos pondremos en contacto a la brevedad');
    }else{
        alert('Por favor complete todos los campos');
    }    
}
