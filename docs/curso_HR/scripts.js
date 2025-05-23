// Traemos los elementos del DOM con los uque vamos a trabajar
const navBtn = document.querySelector('.nav_icon');
const navList = document.querySelector('.nav__listlinks');

// Funciones
navBtn.addEventListener('click', () => {
    navList.classList.toggle('show_nav');
});