const linkList = document.querySelector('.links-list');
const navBtn = document.querySelector('.fa-bars');

console.log(linkList)
console.log(navBtn)

navBtn.addEventListener('click', ()  => {
    linkList.classList.toggle('show')
})