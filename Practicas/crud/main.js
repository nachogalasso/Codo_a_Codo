// C->create |R->read |U->update |D->delete

// HTML elements
const form = document.querySelector('.input-form');
const inputData = document.getElementById('msgInput');
const itemData = document.querySelector('.posts-container');
const alertMsg = document.querySelector('.msgAlert');

// APP LOGIC

// variables to use later
let editEl;
let editItems = false;
let editID = "";

// form
form.addEventListener('submit', addItem)

// add task
function addItem(e) {
  e.preventDefault();
  const taskValue = inputData.value.toLowerCase();
  const randomId = Math.floor(Math.random() * 1000) + (1).toString();
  
  if(taskValue !== "" ) {
    // & editItem === false
    createTaskList(randomId, taskValue);
    displayAlert('task added', 'good')
    dataStorage(randomId, taskValue); 
  }else{
    displayAlert("You forgot to post something!!", "wrong");
  }
  

  // formValidation(); // remember this is a function, we need to define later
}

// function to determine if there is text in the input
// function formValidation() {
  
//   if (inputData.value == "") {
//     alertMsg.textContent = "You forgot to post something!!";
//     setTimeout(function () {
//       alertMsg.textContent = "";
//     }, 1500);
//   } else {
//     alertMsg.innerHTML = "";
//     dataStorage(); // function to make an object with the data
    
//   } else if(taskValue !== "" && )
// }

function displayAlert(text, action) {
  alertMsg.textContent = text
  alertMsg.classList.add(`alert-${action}`)

  setTimeout(function () {
    (alertMsg.textContent = ""), alertMsg.classList.remove(`alert-${action}`)
  }, 1500)
}

itemData.addEventListener("click", (e) => {
  console.log(e.target)
  const itemPost = [... document.querySelectorAll('.post-item')] 
  itemPost.forEach(ids => {
    let id = ids.dataset.id
    removeItemStorage(id);
  })
  if (e.target.classList.contains("delete")) {
    e.target.parentElement.parentElement.remove();
    // inputData.value = "";
  } else {
    inputData.value = e.target.parentElement.previousElementSibling.innerText;
    alertMsg.textContent = "Edit you Task";
    e.target.parentElement.parentElement.remove();
  }
});


// Let´s storage the data in an object
function dataStorage(randomId, taskValue) {
  
  const data = { id: randomId, text: taskValue };
  let item = getLocalStorage();
  item.push(data)
  localStorage.setItem("tasks", JSON.stringify(item));
}

// remove item from storage
function removeItemStorage(randomId) {
  let item = getLocalStorage();
  item = item.filter(function (items) {
    if (items.id != randomId) {
      return items;
    }
  });
  localStorage.setItem('tasks', JSON.stringify(item))
}

// edit Items from localStorage
function editLocalStorage(randomId, taskValue) {
  let items = getLocalStorage();
  items = items.map(function (item) {
    if (item.id === randomId) {
      item.value = taskValue;
    }
    return item;
  });
  localStorage.setItem('tasks', JSON.stringify(items))
}



function getLocalStorage() {
  return localStorage.getItem('tasks') ? JSON.parse(localStorage.getItem('tasks')) : [];
}

function createTaskList(randomId, taskValue) {
  itemData.innerHTML += `
    <div class="post-item" data-id=${randomId}>
      <p>${taskValue}</p>
      <span class="options">
        <i class="fas fa-edit"></i>
        <i class="fas fa-trash-alt delete"></i>
      </span>
    </div>`;

  inputData.value = "";
}