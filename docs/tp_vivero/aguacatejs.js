/* Let´s bring the elements */
/* NAVBAR ELEMENTS */
const navList = document.getElementById('nav-list');
const iconMenu = document.getElementById('toggle-menu');
const mainLogo = document.getElementById('main-logo');

/* CAROUSEL IMAGES */
const carousel = document.querySelectorAll('.slide-container .slider');
const nextImageDelay = 4000;
let slideIndex = 0;
// carousel[slideIndex].classList.toggle('show'); // setInverval(nextImage, nextImageDelay);

iconMenu.addEventListener('click', () => {
    mainLogo.classList.toggle('logo-nav');
    navList.classList.toggle('nav-list-show');
});


setInterval(() => {
    carousel[slideIndex].classList.remove('show');
    slideIndex = (slideIndex + 1) % carousel.length;
    carousel[slideIndex].classList.toggle('show');
    
}, nextImageDelay);

