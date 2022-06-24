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
const openModal = document.querySelector(".emailBtn");
const emailValid = document.getElementById("card_email");
const modalEmail = document.querySelector(".email_data");

const emailIsSet = {
  email: false,
}

/* Close MODAL, clicking outside the window */
window.onclick = function(e) {
  if (e.target == modal) {
    modal.classList.remove("show_modal");
  }
}

/* Handling the email form */
/* Prevent from sending the form without an email */
  modalEmail.addEventListener('submit', (e) => {
    e.preventDefault();
    validateForm();
    
  })

/* EventListener for the input */
emailValid.addEventListener('change', (e) => {
  if(e.target.value.trim().length > 0) emailIsSet.email = true
})

/* Function to validate the email address */
function validateForm() {
  const formValue = Object.values(emailIsSet)
  const valid = formValue.findIndex(value => value == false);
  if(valid == -1) {
    form.submit();
    modal.classList.remove("show_modal");
  }else alert("Please enter your email")
}

/* CARD FORM */
form.addEventListener("submit", sendCardInfo);

function sendCardInfo(e) {
  e.preventDefault();
}

/* OPEN MODAl */
openModal.addEventListener('click', () => {
  modal.classList.add("show_modal")
})

/* Close Modal */
closeModal.addEventListener('click', () => {
  modal.classList.remove("show_modal")
})

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
