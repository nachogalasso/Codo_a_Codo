/* GIFT LIST SCRIPTS */

/* Calling HTML Elements */
const alert = document.querySelector(".alert"); // alert messages
const alert2 = document.querySelector(".alert2"); // alert messages
const form = document.querySelector(".gift-entry"); // list gift form
const giftEntry = document.getElementById("ventry"); // input value
const entryBtn = document.getElementById("entryBtn"); // add button
const numGifts = document.getElementById("numentry"); // number of gifts
const namEntry = document.getElementById("namentry"); // name value
const giftLink = document.getElementById("giftlink"); // image link
const giftPrice = document.getElementById("priceentry"); // image link
const container = document.querySelector(".container-list"); // container List
const list = document.getElementById("list"); // Gift list
const deleteAll = document.querySelector(".clearBtn"); // delete all list button
const text = document.querySelector(".text"); // info text
const modal = document.querySelector(".modal"); // modal form
const openModal = document.querySelector(".modalBtn"); // open modal
const closeModal = document.querySelector(".closeModal"); // close modal
const randomBtn = document.getElementById("randomBtn"); // random present btn
const giftsTotal = document.querySelector('.gift-total'); // show gifts subtotal
const subtotal = document.querySelector('.subtotal'); // show preview container
const preview = document.querySelector('.gift-content') // preview items
const previewBtn = document.querySelector('.previewBtn') // display the preview gift list
const closePreview = document.querySelector('.close-list') // btn to close the preview list

/* Variables for later use */
let editElement;
let editPerson;
let editNumber;
let editLink;
let editPrice;
let editItems = false;
let editID = "";
let giftLocalStorage = []

/* LIST EVENTLISTENERS */
openModal.addEventListener("click", () => {
	closeModal.classList.remove("hide");
	randomBtn.classList.remove("hide");
	modal.classList.add("show");

});

closeModal.addEventListener("click", () => {
	modal.classList.remove("show");
	setBackToDefault()
});

closePreview.addEventListener('click', () => {
	subtotal.classList.remove('subtotal');
})

// Submit form items
form.addEventListener("submit", addItem); // Submit form items

// Delete All items list
deleteAll.addEventListener('click', clearItems); 

// Setup items from LocalStorage
window.addEventListener('DOMContentLoaded', setupItems);

// random gift function
randomBtn.addEventListener("click", getRandomGifts);

// preview modal
previewBtn.addEventListener('click', () => {
	subtotal.classList.add("subtotal");
});

// Getting items from Form
function addItem(e) {
	e.preventDefault()
	const iValue =  giftEntry.value.toLowerCase()
	const id = Math.floor(Math.random() * 1000) + (1).toString()
	const num = numGifts.value;
	const honored = namEntry.value.toLowerCase();
	const image = giftLink.value;
	const price = giftPrice.value;

	if(iValue !== "" && editItems === false) {
		
		createGiftList(iValue, id, num, honored, image, price);
    	displayAlert("Regalo ingresado", "exito");

		container.classList.add('show-container');
		text.classList.add('hide');
		addToLocalStorage(iValue, id, num, honored, image, price);
		setGiftValues();

		setBackToDefault()

	} else if(iValue !== "" && editItems === true) {

		editElement.innerHTML = iValue;
		editNumber.innerHTML = num;
		editPerson.innerHTML = honored;
		editLink.src = image;
		editPrice.innerHTML = price;
		displayAlert('Gift modified', 'exito');
		editLocalStorage(iValue, editID, honored, image, num, price);
		setGiftValues();

		setBackToDefault();
		modal.classList.remove("show");
		
	} else {
		displayAlert("Por favor ingresa un regalo", "error");
	}
}

// DISPLAY ITEMS
// Display Alert
function displayAlert(text, action) {
	alert.textContent = text;
	alert.classList.add(`alert-${action}`)
	alert2.textContent = text;
	alert2.classList.add(`alert-${action}`)
	

	// Alert Timeout
	setTimeout(function () {
		(alert.textContent = ""), alert.classList.remove(`alert-${action}`);
	}, 1000);
	setTimeout(function () {
		(alert2.textContent = ""), alert2.classList.remove(`alert-${action}`);
	}, 1000);
}

// Clear Items
function clearItems() {
	const items = document.querySelectorAll(".gift-item");
	if(items.length > 0) {
		items.forEach(item => {
			list.removeChild(item);
		});
	}
	container.classList.remove("show-container");
	text.classList.remove("hide");
	displayAlert("All items removed", "error");
	setBackToDefault();
	localStorage.removeItem("giftList");
}

// Delete and Edit Buttons
function deleteGift(e) {
	const element = e.currentTarget.parentElement.parentElement;
	const id = element.dataset.id;
	list.removeChild(element);
	if(list.children.length === 0) {
		container.classList.remove("show-container");
		text.classList.remove("hide");
	}
	displayAlert("Regalo Eliminado", "error");
	setBackToDefault();
	removeItemLocalStorage(id)
}

function editGift(e) {
	const element = e.currentTarget.parentElement.parentElement;
	editLink = e.currentTarget.parentElement.parentElement.childNodes[1]
	editElement = e.currentTarget.parentElement.previousElementSibling.childNodes[1];
	editPerson = e.currentTarget.parentElement.previousElementSibling.childNodes[3];
	editNumber = e.currentTarget.parentElement.previousElementSibling.childNodes[5];
	editPrice = e.currentTarget.parentElement.previousElementSibling.childNodes[7];
	// display values in inputs
	giftEntry.value = editElement.textContent;
	namEntry.value = editPerson.textContent;
	numGifts.value = editNumber.textContent;
	giftPrice.value = editPrice.innerHTML;
	giftLink.value = editLink.src
	editItems = true;
	editID = element.dataset.id;
	displayAlert("Edit your gift", "error");
	entryBtn.textContent = "Editar";
	closeModal.classList.add("hide");
	modal.classList.add("show");
	randomBtn.classList.add('hide');
}

// All values to Default
function setBackToDefault() {
  giftEntry.value = "";
  numGifts.value = "";
  namEntry.value = "";
  giftLink.value = "";
  giftPrice.value = "";
  editItems = false;
  editID = "";
  editElement = "";
  editName = "";
  editImage = "";
  editNumber = 1;
  entryBtn.textContent = "Agregar";
//   randomBtn.classList.remove("hide");
}

// random Gifts
async function getRandomGifts() {
	try {
		let result = await fetch('gifts.json');
		let data = await result.json();
		let products = data.gifts
		products = products.map(item => {
			const id = item.id;
			const value = item.value;
			const link = item.link;
			const price = item.price;
			return {id, value, link, price}
		}) 
		// add products to a variable
		let glist = products

		// get a random ID to bring an item
		rdmGift = Math.floor(Math.random() * 11);
		// loop through the list of products to match ID´s and bring the values
		for (let i = 0; i < glist.length; i++) {
			if (glist[i].id == rdmGift) {
				console.log(glist[i].id);
				giftEntry.value = glist[i].value;
				giftPrice.value = glist[i].price;
				giftLink.value = glist[i].link;
			}
		}
	} catch (err) {
		console.error(err);
	}
}

// Set GiftList Values
function setGiftValues() {
	let tempTotal = 0;
	let giftTotal = 0;
	let items = getLocalStorage();
	giftLocalStorage = [...items]
	console.log(giftLocalStorage)
	giftLocalStorage.map(item => {
		tempTotal += item.quantity * item.price;
		giftTotal += item.quantity
	})
	console.log(tempTotal, giftTotal)
	giftsTotal.textContent = tempTotal;
}
// setGiftValues()

// LocalStorage Items
function addToLocalStorage(iValue, id, num, honored, image, price) {
	const gift = {
		id: id,
		value: iValue,
		quantity: num,
		person: honored,
		link: image,
		price: price,
	};
	let item = getLocalStorage();
	item.push(gift);
	localStorage.setItem("giftList", JSON.stringify(item));
}

// Edit the localStorage
function editLocalStorage(iValue, editID, honored, image, num, price) {
	let item = getLocalStorage();
	item = item.map((items) => {
		if (items.id === editID) {
			items.value = iValue;
			items.quantity = num;
			items.person = honored;
			items.link = image;
			items.price = price;
		}
		return items;
	});
	localStorage.setItem("giftList", JSON.stringify(item));
}

// Remove Item from LocalStorage
function removeItemLocalStorage(id) {
	let item = getLocalStorage();
	item = item.filter(items => {
		if(items.id !== id) {
			return items;
		};
	});
	localStorage.setItem("giftList", JSON.stringify(item))
}

function getLocalStorage() {
	return localStorage.getItem("giftList") ? JSON.parse(localStorage.getItem("giftList")) : [];
}

// Setup Items from localStorage
function setupItems() {
	let items = getLocalStorage();
	if(items.length > 0) {
		items.forEach(item => {
			createGiftList(
				item.value,
				item.id,
				item.quantity,
				item.person,
				item.link,
				item.price
			);
		});
		setGiftValues();

		container.classList.add("show-container");
		text.classList.add("hide");
	}
}


// SETUP ITEMS
function createGiftList(iValue, id, num, honored, image, price) {
	// New HTML element
	const element = document.createElement('section');
	element.classList.add("gift-item");
	// Element attribute
	const attr = document.createAttribute("data-id");
	attr.value = id;
	element.setAttributeNode(attr);
	// Whole element code
	element.innerHTML = `
	<img src="${image}" alt="${iValue}">
	<div class="display-item">
		<p class="gift-text">${iValue}</p>
		<p class="gift-text">${honored}</p>
		<p class="gift-text">${num}</p>
		<p class="gift-text">${num * price}</p>
	</div>
	<div class="btns">
		<button type="button" class="editBtn btn" title="Edit Gift">
			<i class="fas fa-edit"></i>
		</button>
		<button type="button" class="deleteBtn btn" title="Delete Gift">
			<i class="fas fa-trash"></i>
		</button>
	</div>
	`
	// Edit and Delete buttons
	const deleteBtn = element.querySelector('.deleteBtn');
	const editBtn = element.querySelector('.editBtn');
	deleteBtn.addEventListener('click', deleteGift);
	editBtn.addEventListener('click', editGift);

	// Append the whole gift list
	list.appendChild(element);
}

// Preview Gift List
function showPreviewList() {
	const element = document.createElement("div");
	element.classList.add("gift-prev");
	let items = getLocalStorage()
	console.log(items)
	let result = "";
	items.forEach(item => {
		result = `
		<!-- cart item start -->
			<div class="items-cont" id=${item.id}>
				<img src=${item.link} alt=${item.value}>
				<div class="items">
				<p class="gift-text">${item.value}</p>
				<p class="gift-text">${item.person}</p>
				<p class="gift-text">${item.quantity}</p>
			</div>
		<!-- cart item end -->
			`;
		
	});
		element.innerHTML = result;
		preview.appendChild(element);

}
showPreviewList()