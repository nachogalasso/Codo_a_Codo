/* Let´s bring the elements */
/* NAVBAR ELEMENTS */
const navList = document.getElementById('nav-list');
const iconMenu = document.getElementById('toggle-menu');
const mainLogo = document.getElementById('main-logo');

/* Navbar EVENT */
iconMenu.addEventListener('click', () => {
    mainLogo.classList.toggle('logo-nav');
    navList.classList.toggle('nav-list-show');
});

/* CAROUSEL IMAGES */
const carousel = document.querySelectorAll('.slide-container .slider');
const load = document.querySelector('.loader');
const nextImageDelay = 4000;
let slideIndex = 0;
// carousel[slideIndex].classList.toggle('show'); // setInverval(nextImage, nextImageDelay);

/* Carousel images */
setInterval(() => {
    load.classList.add('section-photo');
    carousel[slideIndex].classList.remove('show');
    slideIndex = (slideIndex + 1) % carousel.length;
    carousel[slideIndex].classList.toggle('show');
    
}, nextImageDelay);


/* Gallery display */
// viewSeeds.addEventListener('click', () => {
//     seeds.classList.remove('hidden');
//     seedlings.classList.add('hidden');
//     subtrates.classList.add('hidden');
//     utensils.classList.add('hidden');
// })

// viewSeedlings.addEventListener('click', () => {
//     seedlings.classList.remove('hidden');
//     seeds.classList.add('hidden');
// })

// viewSubtrates.addEventListener('click', () => {
//     subtrates.classList.remove('hidden');
//     seedlings.classList.add('hidden');
// })

// viewUtensils.addEventListener('click', () => {
//     utensils.classList.remove('hidden');
//     subtrates.classList.add('hidden');
// })

// viewAll.addEventListener('click', () => {
//     seeds.classList.remove('hidden');
//     seedlings.classList.remove('hidden');    
//     subtrates.classList.remove('hidden');
//     utensils.classList.remove('hidden');
// })



// /* Phone Option */
// emailBtn.addEventListener('click', () => {
//     phoneOpt.classList.toggle('phone-opt');
// })

// phoneBtn.addEventListener('click', () => {
//     phoneOpt.classList.remove('phone-opt');
// })

// const formIsValid = {
//     name: false,
//     email: false,
//     phone: false
// }

// formValidate.addEventListener('submit', (e) => {
//     e.preventDefault()
//     validateForm()
// })

// vName.addEventListener('change', (e) => {
//     if(e.target.value.trim().length > 0) formIsValid.name = true;
// })

// vEmail.addEventListener('change', (e) => {
//     if(e.target.value.trim().length > 0) formIsValid.email = true;
// })

// vPhone.addEventListener('change', (e) => {
//     if(e.target.value.trim().length > 0) formIsValid.phone = true;
//     formIsValid.phone ? vBtn.removeAttribute('disabled') : 
//     vBtn.setAttribute('disabled', true) 

// })

// /* Form validation */
// const validateForm = () => {
//     const formValues = Object.values(formIsValid);
//     const valid = formValues.findIndex(value => value == false);
//     if(valid == -1) {
//         formValidate.submit();
//         alert('Nos pondremos en contacto a la brevedad');
//     }else{
//         alert('Por favor complete todos los campos');
//     }    
// }

