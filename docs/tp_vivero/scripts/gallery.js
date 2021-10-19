/* Let´s bring the elements */
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
