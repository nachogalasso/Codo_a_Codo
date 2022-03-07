/* TO-DO LIST */
const todoEntry = document.getElementById("entry");
const entryBtn = document.getElementById("entryBtn");
const entryList = document.getElementById("containerList");
const alert = document.querySelector(".alert");
const form = document.querySelector(".data-entry");
const clearInput = document.querySelector(".clear");

// Variables for later
let editEl;
let editItems = false;
let editID = "";

/* EVENTLISTENERS */
form.addEventListener("submit", addItem);

// Clear items container
clearInput.addEventListener("click", clearItems);

// Load Items
window.addEventListener("DOMContentLoaded", setupItems);

/* FUNCTIONS */
function addItem(e) {
  e.preventDefault();
  const itemValue = todoEntry.value.toLowerCase();
  const randomId = Math.floor(Math.random() * 1000) + (1).toString();
  //  console.log(randomId);

  //Enter Task Logic
  if (itemValue !== "" && editItems === false) {
    createToDoList(randomId, itemValue);
    //   const element = document.createElement("section");
    //   element.classList.add("entry-list");
    //   // new attr with unique id
    //   const attr = document.createAttribute("id");
    //   attr.value = randomId;
    //   element.setAttributeNode(attr);
    //   // add the list
    //   element.innerHTML = `
    //             <div class="item-list">
    //                 <input type="checkbox" name="" id="check">
    //                 <p class="list-text">${itemValue}</p>
    //             </div>
    //             <div class="btns">
    //                 <button type="button" class="editBtn" title="Edit Task">
    //                     <i class="fas fa-edit"></i>
    //                 </button>
    //                 <button type="button" class="deleteBtn" title="Delete Task">
    //                     <i class="fas fa-trash"></i>
    //                 </button>
    //             </div>`;
    //   // Edit and delete btns
    //   const deleteBtn = element.querySelector(".deleteBtn");
    //   const editBtn = element.querySelector(".editBtn");
    //   deleteBtn.addEventListener("click", deleteItem);
    //   editBtn.addEventListener("click", editItem);

    //   entryList.appendChild(element);
    displayAlert("Task added corectly", "good");
    // display container
    entryList.classList.add("show-container");
    // add to our local storage
    addToLocalStorage(randomId, itemValue);
    // set defualt
    setBackToDefault();
  } else if (itemValue !== "" && editItems === true) {
    editEl.innerHTML = itemValue;
    displayAlert("Task changed", "good");
    // Local storage edit function
    editLocalStorage(editID, itemValue);
    setBackToDefault();
  } else {
    displayAlert("Please enter TASK", "wrong");
  }
}

// Alert Display
function displayAlert(text, action) {
  alert.textContent = text;
  alert.classList.add(`alert-${action}`);

  // remove alert
  setTimeout(function () {
    (alert.textContent = ""), alert.classList.remove(`alert-${action}`);
  }, 1000);
}

// Clear Items Function
function clearItems() {
  const items = document.querySelectorAll(".entry-list");
  if (items.length > 0) {
    items.forEach(function (item) {
      entryList.removeChild(item);
    });
  }
  entryList.classList.remove("show-container");
  displayAlert("All items removed", "wrong");
  setBackToDefault();
  localStorage.removeItem("toDoList");
}

// Delete and Edit btns functions
function deleteItem(e) {
  const element = e.currentTarget.parentElement.parentElement;
  // calling the randomId
  const id = element.id;
  entryList.removeChild(element);
  if (entryList.children.length === 0) {
    entryList.classList.remove("show-container");
  }
  displayAlert("Item removed", "wrong");
  setBackToDefault();
  //  console.log(element);
  // Finally we remove from local storage
  removeItemLocalStorage(id);
}

function editItem(e) {
  const element = e.currentTarget.parentElement.parentElement;
  editEl = e.currentTarget.parentElement.previousElementSibling.childNodes[3];
  // call the value so we can edit it
  todoEntry.value = editEl.innerHTML;
  editItems = true;
  editID = element.id;
  displayAlert("Edit your entry", "wrong");
  entryBtn.textContent = "Go, Edit!";
  //  console.log(editID);
  //  console.log(editEl);
  //  console.log(element);
}

function setBackToDefault() {
  todoEntry.value = "";
  editItems = false;
  editID = "";
  entryBtn.textContent = "Go, Do it!";
}

/* LOCAL STORAGE */
function addToLocalStorage(randomId, itemValue) {
  // with ES6 if the parametres are = to the data variable, we can put only the names
  const toDo = { id: randomId, value: itemValue };
  // now we need to know is the items are getting there so we create a new array variable with getItem. We are gonna
  // see that at the first the item is gonna be 'null', so first check if the value is 'null', if that happens create
  // and empty array []. The 2do time it´s gonna pass the values to the array. Use a ternary ?
  let item = getLocalStorage();
  //  console.log(item);
  //  console.log(toDo);
  item.push(toDo);
  // the we set the items, DON´T FORGET TO PUSH THEM BEFORE!!! =>
  localStorage.setItem("toDoList", JSON.stringify(item));
}

function removeItemLocalStorage(randomId) {
  // here we acces to our localStorage Array
  let item = getLocalStorage();

  item = item.filter(function (items) {
    if (items.id !== randomId) {
      return items;
    }
    //   console.log(item);
  });
  localStorage.setItem("toDoList", JSON.stringify(item));
}

function editLocalStorage(randomId, itemValue) {
  let items = getLocalStorage();
  items = items.map(function (item) {
    if (item.id === randomId) {
      item.value = itemValue;
    }
    return item;
  });
  localStorage.setItem("toDoList", JSON.stringify(items));
}

// the getItem can be used as a function =>
function getLocalStorage() {
  return localStorage.getItem("toDoList")
    ? JSON.parse(localStorage.getItem("toDoList"))
    : [];
}

/* When we use the local storage the most common commands are:
localStorage API
setItem
getItem
removeItem
obviusly we need to save all the things as strings, so we are going to use JSON.stringify and JSON.parse
localStorage.setItem('key=name', JSON.stringify(['item', 'item2']))
when we use the 'getItem' we need to store it in a variable =>
const name = JSON.parse(localStorage.getItem('key=name'))
localStorage.removeItem('key=name') */

/* SETUP ITEMS */
function setupItems() {
  let items = getLocalStorage();
  if (items.length > 0) {
    items.forEach(function (item) {
      createToDoList(item.id, item.value);
    });
    entryList.classList.add("show-container");
  }
}

function createToDoList(randomId, itemValue) {
  const element = document.createElement("section");
  element.classList.add("entry-list");
  // new attr with unique id
  const attr = document.createAttribute("id");
  attr.value = randomId;
  element.setAttributeNode(attr);
  // add the list
  element.innerHTML = `
            <div class="item-list">
                <input type="checkbox" name="" id="check">
                <p class="list-text">${itemValue}</p>
            </div>
            <div class="btns">
                <button type="button" class="editBtn" title="Edit Task">
                    <i class="fas fa-edit"></i>
                </button>
                <button type="button" class="deleteBtn" title="Delete Task">
                    <i class="fas fa-trash"></i>
                </button>
            </div>`;
  // Edit and delete btns
  const deleteBtn = element.querySelector(".deleteBtn");
  const editBtn = element.querySelector(".editBtn");
  deleteBtn.addEventListener("click", deleteItem);
  editBtn.addEventListener("click", editItem);

  entryList.appendChild(element);
}
