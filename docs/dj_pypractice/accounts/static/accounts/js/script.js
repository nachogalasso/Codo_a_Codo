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