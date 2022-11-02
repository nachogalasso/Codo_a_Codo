// C->create |R->read |U->update |D->delete

// HTML elements
const form = document.querySelector('.input-form');
const inputData = document.getElementById('msgInput');
const itemData = document.querySelector('.posts-container');
const alertMsg = document.querySelector('.msgAlert');
const submitBn = document.querySelector('.submitBtn');

// APP LOGIC

// variables to use later
let editEl;
let editItems = false;
let editID = "";

// form
form.addEventListener('submit', addItem);

// Set data from localStorga with the page being loaded
window.addEventListener('DOMContentLoaded', setItems)

// add task
function addItem(e) {
  e.preventDefault();
  const taskValue = inputData.value.toLowerCase();
  const randomId = Math.floor(Math.random() * 1000) + (1).toString();
  
  if (taskValue !== "" && editItems === false) {
    createTaskList(randomId, taskValue);
    displayAlert("task added", "good");
    dataStorage(randomId, taskValue);
    setToDefault()
  } else if (taskValue !== "" && editItems === true) {
    editEl.innerHTML = taskValue;
    displayAlert('Task Changed', 'good');
    editLocalStorage(editID, taskValue);
    setToDefault();
  }else {
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


// ALERT MESSAGES
function displayAlert(text, action) {
  alertMsg.textContent = text
  alertMsg.classList.add(`alert-${action}`)

  setTimeout(function () {
    (alertMsg.textContent = ""), alertMsg.classList.remove(`alert-${action}`)
  }, 1000)
}

// DELETE TASKS
function deleteItem(e) {
  const element = e.currentTarget.parentElement.parentElement
  const id = element.id
  itemData.removeChild(element)
  displayAlert('Item removed', 'good');
  setToDefault()
  removeItemStorage(id)
}

// EDIT TASKS
function editItem(e) {
  const element = e.currentTarget.parentElement.parentElement
  editEl = e.currentTarget.parentElement.parentElement.childNodes[1];
  inputData.value = editEl.innerHTML;
  editItems = true;
  editID = element.id;
  submitBn.textContent = "Edit"
  inputData.focus()
}

// SET TO DEFAULT
function setToDefault() {
  inputData.value = "";
  editItems = false;
  editID = "";
  submitBn.textContent = "Post";
}


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
      item.text = taskValue;
    }
    return item;
  });
  localStorage.setItem('tasks', JSON.stringify(items))
}


// Get Items from localStorage
function getLocalStorage() {
  return localStorage.getItem('tasks') ? JSON.parse(localStorage.getItem('tasks')) : [];
}

// Set Items from localStorage
function setItems() {
  let items = getLocalStorage();
  if (items.length > 0) {
    items.forEach(function (item) {
      createTaskList(item.id, item.text);
    });
    
  }
}

function createTaskList(randomId, taskValue) {
  const fragment = document.createDocumentFragment()
  const task = document.createElement('div');
  task.classList.add('post-item');
  const attr = document.createAttribute('id');
  attr.value = randomId;
  task.setAttributeNode(attr);

  task.innerHTML += `
    
      <p>${taskValue}</p>
      <span class="options">
        <i class="fas fa-edit edit" title="Edit"></i>
        <i class="fas fa-trash-alt delete" title="Delete"></i>
      </span>`;

  fragment.appendChild(task);
  itemData.appendChild(fragment);
  inputData.value = "";
  const deleteBtn = task.querySelector('.delete');
  const editBtn = task.querySelector('.edit');
  deleteBtn.addEventListener('click', deleteItem);
  editBtn.addEventListener('click', editItem);
}