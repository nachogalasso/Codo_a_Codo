/* Let´s bring the elements */
/* NAVBAR ELEMENTS */
const navList = document.getElementById('nav-list');
const iconMenu = document.getElementById('toggle-menu');
const mainLogo = document.getElementById('main-logo');

/* GALLERY ELEMENTS */
const seeds = document.getElementById('seeds');
const seedlings = document.getElementById('seedlings');
const subtrates = document.getElementById('subtrates');
const utensils = document.getElementById('utensils');
const viewSeeds = document.querySelector('.seeds');
const viewSeedlings = document.querySelector('.seedlings');
const viewSubtrates = document.querySelector('.subtrates');
const viewUtensils = document.querySelector('.utensils');
const viewAll = document.querySelector('.all');

/* Navbar EVENT */
iconMenu.addEventListener('click', () => {
    mainLogo.classList.toggle('logo-nav');
    navList.classList.toggle('nav-list-show');
});

/* Gallery display */
viewSeeds.addEventListener('click', () => {
    seeds.classList.remove('hidden');
    seedlings.classList.add('hidden');
    subtrates.classList.add('hidden');
    utensils.classList.add('hidden');
})

viewSeedlings.addEventListener('click', () => {
    seedlings.classList.remove('hidden');
    seeds.classList.add('hidden');
})

viewSubtrates.addEventListener('click', () => {
    subtrates.classList.remove('hidden');
    seedlings.classList.add('hidden');
})

viewUtensils.addEventListener('click', () => {
    utensils.classList.remove('hidden');
    subtrates.classList.add('hidden');
})

viewAll.addEventListener('click', () => {
    seeds.classList.remove('hidden');
    seedlings.classList.remove('hidden');    
    subtrates.classList.remove('hidden');
    utensils.classList.remove('hidden');
})
