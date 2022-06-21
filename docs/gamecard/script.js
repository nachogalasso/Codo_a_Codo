/* GAME CARD FEATURES */
const home = document.getElementById("homeHeader");
const visitor = document.getElementById("visitorHeader");
const homeCard = document.querySelector(".hometeam");
const visitorCard = document.querySelector(".visitorteam");
const viewAll = document.querySelector(".show_cards");


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

