/* PROJECTS SCRIPTS SHEET */

/* TOGGLE NAVBAR */
const navToggle = document.querySelector(".toggle-menu");
const links = document.querySelector(".links");

navToggle.addEventListener("click", () => {
 links.classList.toggle("show-links");
});

/* TO-DO LIST */
const todoEntry = document.getElementById("entry");
const entryBtn = document.getElementById("entryBtn");
const entryList = document.getElementById("containerList");
const alert = document.querySelector(".alert");
const form = document.querySelector(".data-entry");
const showContainer = document.getElementById("containerList");
const clearInput = document.querySelector(".clear");

// Variables for later
let list = [];
let editEl;
let editItems = false;
let editID = "";

/* EVENTLISTENERS */
form.addEventListener("submit", addItem);

// Clear items container
clearInput.addEventListener("click", clearItems);

/* FUNCTIONS */
function addItem(e) {
 e.preventDefault();
 const itemValue = todoEntry.value;
 const randomId = Math.floor(Math.random() * 1000) + (1).toString();
 console.log(randomId);

 //Enter Task Logic
 if (itemValue !== "" && editItems === false) {
  const element = document.createElement("section");
  element.classList.add("entry-list");
  // new attr with unique id
  const attr = document.createAttribute("item-id");
  attr.value = randomId;
  element.setAttributeNode(attr);
  // add the list
  element.innerHTML = `
            <div class="item-list">
                <input type="checkbox" name="" id="check">
                <p class="list-text">${itemValue}</p>
            </div>
            <div class="btns">
                <button type="button" class="editBtn">
                    <i class="fas fa-edit"></i>
                </button>
                <button type="button" class="deleteBtn">
                    <i class="fas fa-trash"></i>
                </button>
            </div>`;
  // Edit and delete btns
  const deleteBtn = element.querySelector(".deleteBtn");
  const editBtn = element.querySelector(".editBtn");
  deleteBtn.addEventListener("click", deleteItem);
  editBtn.addEventListener("click", editItem);

  entryList.appendChild(element);
  displayAlert("Task added corectly", "good");
  // display container
  showContainer.classList.add("show-container");
  // add to our local storage
  addToLocalStorage(randomId, itemValue);
  // set defualt
  setBackToDefault();
 } else if (itemValue !== "" && editItem === true) {
  console.log("editing");
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
 showContainer.classList.remove("show-container");
 displayAlert("All items removed", "wrong");
 setBackToDefault();
 // localStorage.removeItem('entryList')
}

// Delete and Edit btns functions
function deleteItem(e) {
 const delItem = e.currentTarget.parentElement.parentElement;
 // calling the randomId
//  const id = element.dataset.id;
 entryList.removeChild(delItem);
 if (entryList.children.length === 0) {
  showContainer.classList.remove("show-container");
 }
 displayAlert("Item removed", "wrong");
 setBackToDefault();
 // Finally we remove from local storage
 // removeItemLocalStorage(id)
}

function editItem() {
 console.log("edit item");
}

function setBackToDefault() {
 todoEntry.value = "";
 editItems = false;
 editID = "";
 entryBtn.textContent = "Go, Do it!";
 // showContainer.classList.remove('show-container');
 console.log("back to default");
}

/* LOCAL STORAGE */
function addToLocalStorage(randomId, itemValue) {
 console.log("added to storage");
}

function removeItemLocalStorage(id) {}
