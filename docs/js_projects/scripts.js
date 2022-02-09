/* PROJECTS SCRIPTS SHEET */

/* TOGGLE NAVBAR */
const navToggle = document.querySelector('.toggle-menu');
const links = document.querySelector('.links');


navToggle.addEventListener('click', () => {
    links.classList.toggle('show-links');
})



/* TO-DO LIST */
const todoEntry = document.getElementById('entry');
const entryBtn = document.getElementById('entryBtn');
const entryList = document.getElementById('entryList');
const remove = document.querySelectorAll('.del');

let list = [];


entryBtn.addEventListener('click', () => {
    // const itemList = document.createElement('LI')
    // itemList.innerHTML = `<p>${list}</p><span><i class="fas fa-trash-alt"></i></span>`
    // entryList.appendChild(itemList);
    
    if(todoEntry.value === '') {
        alert('ingresa un elemento');
    }else{
        list.push(todoEntry.value)
    }
    
    todoEntry.value = '';
    renderList();
})


function renderList()  {
    let itemList = '';
    for(let i=0; i < list.length; i++) {
        itemList += 
        `<li class="list-item">
        <p class="list-text">${list[i]}</p>
        <span class="del"><i class="fas fa-trash-alt"></i></span>
        </li>
        `
    }

    entryList.innerHTML = itemList;

}

console.log(list)
console.log(remove)