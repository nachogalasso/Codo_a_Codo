/* REVIEWS */
// Array Object containing the peoples id
const reviews = [
    {
        id: 1,
        name: 'Chris Kringle',
        job: 'Ux Designer',
        img: './assets/images/reviews/avatar.webp',
        text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt consequatur quasi atque hic accusantium est doloremque dignissimos error similique aut.'
    },
    {
        id: 2,
        name: 'Joe Diggs',
        job: 'web developer',
        img: './assets/images/reviews/avatar2.webp',
        text: 'Vivamus sed odio ipsum. Donec hendrerit augue laoreet sem interdum interdum. Fusce maximus imperdiet dolor, at rutrum libero aliquam at. Fusce in odio ac ante volutpat feugiat. Curabitur lectus tortor, euismod et sagittis nec, condimentum.'
    },
    {
        id: 3,
        name: 'Diego Lopez',
        job: 'SEO',
        img: './assets/images/reviews/avatar3.webp',
        text: 'Nam convallis, magna sit amet fermentum aliquam, mauris turpis tincidunt mi, sit amet iaculis sem tellus.'
    },
    {
        id: 4,
        name: 'Julia Wong',
        job: 'web designer',
        img: './assets/images/reviews/avatar4.webp',
        text: 'Eiusmod est officia commodo laborum magna exercitation laboris anim laboris qui deserunt ea. Ipsum sunt anim sit duis culpa veniam commodo incididunt duis id occaecat sunt aute. Aliqua esse consequat ea minim minim ad eiusmod commodo excepteur nulla ex amet cillum. Cupidatat consectetur aute aliquip magna anim occaecat sit do sint deserunt Lorem officia.'
    },
    {
        id: 5,
        name: 'Jess McDerm',
        job: 'Ux Designer',
        img: './assets/images/reviews/avatar5.webp',
        text: 'Deserunt consectetur dolore nulla dolore veniam adipisicing consectetur est reprehenderit pariatur occaecat voluptate consectetur. Aute proident commodo proident reprehenderit elit. Dolore fugiat exercitation quis enim irure tempor est sunt.'
    },
    {
        id: 6,
        name: 'Lizzy Shefield',
        job: 'Intern',
        img: './assets/images/reviews/avatar6.webp',
        text: 'Consectetur anim Lorem nulla elit dolore velit reprehenderit sunt proident. Aute reprehenderit ullamco est deserunt eu. Ex do aliquip sunt nostrud non ea. Sint commodo non laboris duis dolor exercitation exercitation ipsum anim eu enim velit. Reprehenderit non dolor adipisicing laborum duis in enim ut anim aute sint amet ut.'
    },
    {
        id: 7,
        name: 'Sofía Lock',
        job: 'Graphic designer',
        img: './assets/images/reviews/avatar7.webp',
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
