/* PROJECTS SCRIPTS SHEET */

/* TOGGLE NAVBAR */
const navToggle = document.querySelector(".toggle-menu");
const links = document.querySelector(".links");

navToggle.addEventListener("click", () => {
 links.classList.toggle("show-links");
});

