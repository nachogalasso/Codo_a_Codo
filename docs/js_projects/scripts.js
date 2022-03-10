/* PROJECTS SCRIPTS SHEET */

/* TOGGLE NAVBAR */
const navToggle = document.querySelector(".toggle-menu");
const links = document.querySelector(".links");

navToggle.addEventListener("click", () => {
  links.classList.toggle("show-links");
});

/* IMAGE SLIDER */
const slides = document.querySelectorAll(".slide");
const btnNext = document.querySelector(".nextBtn");
const btnPrev = document.querySelector(".prevBtn");

// We create a forEach, this allow us to go through each of our image slide and we use their index to create the %
// of the transition =>
slides.forEach(function (slide, index) {
  slide.style.left = `${index * 100}%`;
});

// Now is time to create the functionality
// Remember when we use elements that we need to be counted, don´t forget to create a "count variable". This allow
// to go up or down, increase or decrease
let counter = 0;
// we tell the buttons what to do
btnNext.addEventListener("click", () => {
  counter++;
  carousel();
});
btnPrev.addEventListener("click", () => {
  counter--;
  carousel();
});

// we create a function that allow us to display the images
function carousel() {
  // This is the logic for the previous and next buttons
  // with this configuration the slider go foward and back, and when it comes to an end it´s restart
  // if (counter === slides.length) {
  //   counter = 0;
  // }
  // if (counter < 0) {
  //   counter = slides.length - 1;
  // }

  // So now let´s add some magic
  if (counter < slides.length - 1) {
    btnNext.style.display = "block";
  } else {
    btnNext.style.display = "none";
  }

  if (counter > 0) {
    btnPrev.style.display = "block";
  } else {
    btnPrev.style.display = "none";
  }
  slides.forEach(function (slide) {
    slide.style.transform = `translateX(-${counter * 100}%)`;
  });
}
btnPrev.style.display = "none";
