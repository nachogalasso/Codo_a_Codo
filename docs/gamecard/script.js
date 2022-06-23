/* GAME CARD FEATURES */
const home = document.getElementById("homeHeader");
const visitor = document.getElementById("visitorHeader");
const homeCard = document.querySelector(".hometeam");
const visitorCard = document.querySelector(".visitorteam");
const viewAll = document.querySelector(".show_cards");
const form = document.querySelector(".card_form");

// MODAL
const modal = document.getElementById("myModal");
const closeModal = document.querySelector(".close");
const emailValid = document.getElementById("card_email");
const modalEmail = document.querySelector(".email_data");

const emailIsSet = {
  email: false,
}

window.addEventListener('DOMContentLoaded', () => {
  setTimeout(function () {
    modal.classList.add("show_modal");
  }, 2000);
})

// closeModal.addEventListener('Click', (e) => {
//   if(e.target == modal) {
//     modal.classList.remove("show_modal");
//   }
// })

window.onclick = function(e) {
  if (e.target == modal) {
    modal.classList.remove("show_modal");
  }
}

modalEmail.addEventListener('submit', (e) => {
  e.preventDefault();
  validateForm();
})

emailValid.addEventListener('change', (e) => {
  if(e.target.value.trim().length > 0) emailIsSet.email = true
})

function validateForm() {
  const formValue = Object.values(emailIsSet)
  const valid = formValue.findIndex(value => value == false);
  if(valid == -1) form.submit()
  else alert("Please enter your email")
}

/* CARD FORM */
form.addEventListener("submit", sendCardInfo);

function sendCardInfo(e) {
  e.preventDefault();
}


visitor.addEventListener('click', () => {
  visitorCard.classList.add("show");
  homeCard.classList.add("hide");
  home.className = "visitor";
  visitor.className = "home_header";
})

home.addEventListener('click', () => {
  homeCard.classList.remove("hide");
  visitorCard.classList.remove("show");
  visitor.className = "visitor";
  home.className = "home_header";
})

viewAll.addEventListener('click', () => {
  visitorCard.classList.add("show");
  homeCard.classList.remove("hide");
  home.className = "both_cards"
  visitor.className = "both_cards";
})

