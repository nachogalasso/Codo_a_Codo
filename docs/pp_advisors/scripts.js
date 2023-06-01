const modal = document.querySelector('.modal');
const modalBtn = document.querySelectorAll('.modal-btn');
const navBtn = document.querySelector('.display-nav');
const closeModalBtn = document.querySelector('.close-modal');
const navList = document.querySelector('.nav__header-linkslist');
const sliderContainer = document.querySelector('.slide_container');
// firstSlide = sliderContainer.querySelectorAll('.slide')[0];
const arrowIcons = document.querySelectorAll('.slider-btn i');




// Modal Event Handler
modalBtn.forEach(item => {
    item.addEventListener('click', () => {
        modal.classList.add('show');
    })
});

closeModalBtn.addEventListener('click', () => {
    modal.classList.remove('show');
});

navBtn.addEventListener('click', () => {
    navList.classList.toggle('show-nav');
});


// CAROUSEL SLIDER
var swiper = new Swiper(".slide_container", {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    grabCursor: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
      },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      991: {
        slidesPerView: 3,
      },
    },
  });

// FEATURES CAROUSEL
var swiper = new Swiper(".featured-container", {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    grabCursor: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
      },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      991: {
        slidesPerView: 3,
      },
    },
  });
