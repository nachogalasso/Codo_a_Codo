/* Navbar */
const iconMenu = document.getElementById('toggle-menu');
const mainMenu = document.getElementById('main-menu');
const mainLogo = document.getElementById('logo');

/* Input time */
const lunchTime = document.getElementById('lunch');
const dinnerTime = document.getElementById('dinner');
const lunch = document.getElementById('lunch_time');
const dinner = document.getElementById('dinner_time');

iconMenu.addEventListener('click', () => {
    mainMenu.classList.toggle('show');
})

lunchTime.addEventListener('click', () => {
    lunch.classList.toggle('lunch');
    dinner.classList.remove('dinner');
})

dinnerTime.addEventListener('click', () => {
    dinner.classList.toggle('dinner');
    lunch.classList.remove('lunch');
})