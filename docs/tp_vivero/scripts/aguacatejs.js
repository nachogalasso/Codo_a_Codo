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

/* CAROUSEL IMAGES 1 */
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
