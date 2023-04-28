const modal = document.querySelector('.modal');
const modalBtn = document.querySelectorAll('.modal-btn');
const navBtn = document.querySelector('.display-nav');
const closeModalBtn = document.querySelector('.close-modal')
const navList = document.querySelector('.nav__header-linkslist')
console.log(modal)

modalBtn.forEach(item => {
    item.addEventListener('click', () => {
        modal.classList.add('show');
    })
});

closeModalBtn.addEventListener('click', () => {
    modal.classList.remove('show');
});

navBtn.addEventListener('click', () => {
    navList.classList.toggle('show-nav');
});