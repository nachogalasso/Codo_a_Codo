const modal = document.querySelector('.modal');
const modalBtn = document.querySelectorAll('.modal-btn, .modal-logo');
const navBtn = document.querySelector('.display-nav');
const closeModalBtn = document.querySelector('.close-modal');
const navList = document.querySelector('.nav__header-linkslist');
const sliderContainer = document.querySelector('.slide_container');
// firstSlide = sliderContainer.querySelectorAll('.slide')[0];
const arrowIcons = document.querySelectorAll('.slider-btn i');
// MODAL FORM VALIDATION
const inputs = [...document.getElementsByTagName('input')];
const error = [...document.querySelectorAll('.error')];
const form = document.querySelector('.form-section');
const cancel = document.querySelector('.cancel');




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

// CLIENTS REVIEWS
const reviews = [
  {
      id: 1,
      name: 'Chris Kringle',
      job: 'Ux Designer',
      img: './assets/images/users/undraw_male_avatar_g98d.svg',
      text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequatur quasi atque hic accusantium est doloremque dignissimos error similique aut.'
  },
  {
      id: 2,
      name: 'Joe Diggs',
      job: 'web developer',
      img: './assets/images/users/undraw_female_avatar_efig.svg',
      text: 'Vivamus sed odio ipsum. Donec hendrerit augue laoreet sem interdum interdum. Fusce maximus imperdiet dolor, at rutrum libero aliquam at. Fusce in odio ac ante volutpat feugiat. Curabitur lectus tortor, euismod et sagittis nec, condimentum.'
  },
  {
      id: 3,
      name: 'Diego Lopez',
      job: 'SEO',
      img: './assets/images/users/undraw_female_avatar_efig.svg',
      text: 'Nam convallis, magna sit amet fermentum aliquam, mauris turpis tincidunt mi, sit amet iaculis sem tellus.'
  },
  {
      id: 4,
      name: 'Julia Wong',
      job: 'web designer',
      img: './assets/images/users/undraw_male_avatar_g98d.svg',
      text: 'Eiusmod est officia commodo laborum magna exercitation laboris anim laboris qui deserunt ea. Ipsum sunt anim sit duis culpa veniam commodo incididunt duis id occaecat sunt aute. Aliqua esse consequat ea minim minim ad eiusmod commodo excepteur nulla ex amet cillum. Cupidatat consectetur aute aliquip magna anim occaecat sit do sint deserunt Lorem officia.'
  },
  {
      id: 5,
      name: 'Jess McDerm',
      job: 'Ux Designer',
      img: './assets/images/users/undraw_female_avatar_efig.svg',
      text: 'Deserunt consectetur dolore nulla dolore veniam adipisicing consectetur est reprehenderit pariatur occaecat voluptate consectetur. Aute proident commodo proident reprehenderit elit. Dolore fugiat exercitation quis enim irure tempor est sunt.'
  },
  {
      id: 6,
      name: 'Lizzy Shefield',
      job: 'Intern',
      img: './assets/images/users/undraw_female_avatar_efig.svg',
      text: 'Consectetur anim Lorem nulla elit dolore velit reprehenderit sunt proident. Aute reprehenderit ullamco est deserunt eu. Ex do aliquip sunt nostrud non ea. Sint commodo non laboris duis dolor exercitation exercitation ipsum anim eu enim velit. Reprehenderit non dolor adipisicing laborum duis in enim ut anim aute sint amet ut.'
  },
  {
      id: 7,
      name: 'Sofía Lock',
      job: 'Graphic designer',
      img: './assets/images/users/undraw_male_avatar_g98d.svg',
      text: 'In id culpa laboris laborum laborum occaecat cupidatat culpa. Est tempor officia occaecat sit ad dolor in esse est nulla. Tempor cupidatat sit ex qui. Dolore esse eiusmod sint do proident amet velit nulla deserunt.'
  },

]

// Calling the elements
const avatar = document.querySelector('.rd-img');
const author = document.querySelector('.author');
const job = document.querySelector('.job');
const info = document.querySelector('.info');

// Carousel elements
const prevBtn = document.getElementById('left');
const nextBtn = document.getElementById('right');
const randomBtn = document.querySelector('.surpriseBtn');

// Review counter start item go through
let counterItem = 0;

window.addEventListener('DOMContentLoaded', () => {
  personReview(counterItem)
})

// Review Function 
personReview = (person) => {
  const item = reviews[person];
  // the images go with .src
  avatar.src = item.img; 
  // I´m going to change the textContent, thats why I put .textContent
  author.textContent = item.name; 
  job.textContent = item.job;
  info.textContent = item.text;
}

// show NEXT review
nextBtn.addEventListener('click', () => {
  counterItem++;
  if(counterItem > reviews.length - 1) {
      counterItem = 0;
  }
  personReview(counterItem);
})

// show PREVIOUS review
prevBtn.addEventListener('click', () => {
  counterItem--;
  if(counterItem < 0) {
      counterItem = reviews.length - 1
  }
  personReview(counterItem);
})

// show RANDOM review
// const randReview = () => {
//     return Math.floor( Math.random() * reviews.length)
// }
randomBtn.addEventListener('click', () => {
  counterItem = Math.floor( Math.random() * reviews.length);
  personReview(counterItem);
})


// MODAL FORM ENGINE
console.log(inputs)
let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes); 

let username = id('id_username'),
  //  email = id('email'),
   password = id('id_password1'),
   errorMsg = classes('alert'),
   successIcon = classes('success'),
   failureIcon = classes('failure');

   form.addEventListener('submit', (e) => {
    e.preventDefault();
  
    newEngine();
  })

cancel.addEventListener("click", () => {
    for(let i = 0; i < errorMsg.length; i++) {
       errorMsg[i].textContent = ''
    }
    for(let i = 0; i < failureIcon.length; i++) {
       failureIcon[i].style.opacity = '0'
    }
    for(let i = 0; i < successIcon.length; i++) {
       successIcon[i].style.opacity = '0'
    }
});

let engine = (id, serial, message) => {
  if(id.value.trim() === '') {
    errorMsg[serial].textContent = message;
    failureIcon[serial].style.opacity ='1';
    successIcon[serial].style.opacity = '0';
  }else{
    errorMsg[serial].textContent = '';
    failureIcon[serial].style.opacity = "0";
    successIcon[serial].style.opacity = "1";
  }
}

function newEngine() {
  inputs.forEach(item => {
        if (item.id === "id_username") {
       engine(username, 0, 'You forgot or wrong username');

     }
        if(item.id === "id_password1") {
          engine(password, 2, 'You forgot or wrong password');
          let passValue = item.value;
          validatePasswordModerate(passValue)

     }
  })
}

// Email Regex validation
const validateEmail = (emailValue) => {
	const emailRegex =
		/^(([^<>()\[\]\\.,:\s@"]+(\.[^<>()\[\]\\.,:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

	if (emailRegex.test(emailValue)) {
      console.log("email válido");
      errorMsg[1].textContent = "";
      failureIcon[1].style.opacity = "0";
		  successIcon[1].style.opacity = "1";
   } else {
      errorMsg[1].textContent = "You forgot or wrong email";
      failureIcon[1].style.opacity = "1";
		  successIcon[1].style.opacity = "0";
      console.log("email incorrecto");
   } 
};

// Password Regex Validation
const validatePasswordModerate = (passValue) => {
	//Should have 1 lowercase letter, 1 uppercase letter, 1 number, and be at least 8 characters long
	const passwordRegex =
		/(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.{8,}$/;

	if (passwordRegex.test(passValue)) {
      console.log("password válido");
   } else {
      console.log("password incorrecto");
   }
};