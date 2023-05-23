const modal = document.querySelector('.modal');
const modalBtn = document.querySelectorAll('.modal-btn');
const navBtn = document.querySelector('.display-nav');
const closeModalBtn = document.querySelector('.close-modal');
const navList = document.querySelector('.nav__header-linkslist');
const sliderContainer = document.querySelector('.slide_container');
// firstSlide = sliderContainer.querySelectorAll('.slide')[0];
const arrowIcons = document.querySelectorAll('.slider-btn i');

let isDragStart = false, prevPageX, prevScrollLeft;


document.addEventListener('DOMContentLoaded', getHouses)

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




// Get images from JSON
async function getHouses() {
    try {
        let result = await fetch('./assets/houses.json');
        let data = await result.json();
        let houses = await data.houses;
        // console.log(houses)
        houses = houses.map(item => {
            const title = item.title;
            const description = item.description;
            const image = item.image;
            const price = item.price;
            const rooms = item.bedrooms;
            const toilet = item.toilet;
            return {title, description, image, price, rooms, toilet};
        })

        let card = houses
        displayHouses(card)

    } catch (err){
        console.log(err)
    }
}

function displayHouses(card) {
    const dragging = (e) => {
        carrouselSlider.scrollLeft = e.pageX;
        console.log(e.pageX)
    }

    let fragment = "";
    card.forEach(item => {
        fragment += `
        <section class="slide">
            <div class="slide_card_container">
                <figure class="img-cont">
                    <img src=${item.image} alt=${item.title} loading="lazy">
                </figure>
                <ul class="slide-description">
                    <li class="list-desc">
                        <h4 class="slide_title">${item.title}</h4>
                        <p class="slide_price">€${item.price}</p>
                        <p>${item.description}</p>
                    </li>
                    <li class="list-icons">
                        <p><i class="fa-solid fa-bath"></i> ${item.toilet}</p>
                        <p><i class="fa-solid fa-bed"></i> ${item.rooms}</p>
                    </li>
                    <li>
                        <a href="" class="">visit</a>
                    </li>
                </ul>
            </div>    
        </section>
        `
    })
    sliderContainer.innerHTML = fragment
    
    
}
firstSlide = sliderContainer.querySelectorAll('.slide')[0];

let firstSlideWidth = firstSlide.clientWidth + 1.4;


// Carrousel drag
const dragStart = (e) => {
    // update the values with movedown event
    isDragStart = true;
    prevPageX = e.pageX;
    prevScrollLeft = sliderContainer.scrollLeft;
}

const dragging = (e) => {
    // scroll the images to left according to mouse pointer
    if(!isDragStart) return;
    e.preventDefault();
    let positionDiff = e.pageX - prevPageX;
    sliderContainer.scrollLeft = prevScrollLeft - positionDiff;
}

const dragStop = () => {
    isDragStart = false
}

sliderContainer.addEventListener('mousedown', dragStart);
sliderContainer.addEventListener('mousemove', dragging);
sliderContainer.addEventListener('mouseup', dragStop);

arrowIcons.forEach(icon => {
    icon.addEventListener('click', () => {
        sliderContainer.scrollLeft += icon.id == 'left' ? -firstSlideWidth : firstSlideWidth;
    })

})