// RICK & MORTY API JS APP
const cardContainer = document.querySelector(".container-cards");

let cardDOM

document.addEventListener('DOMContentLoaded', () => {
  if(window.fetch != undefined) {
    console.log('Fetch funciona guachin')
    
  }else{
    console.log('No soporta al Fetch')
  }

  getCardsInfo();
  displayCardData();


})


// res = response = respuesta
function getCardsInfo() {
  // after using the fetch remember the next step is to use then to see the result
  fetch("https://rickandmortyapi.com/api/character")
  // console.log(cards) with this the promise is fullfiled
  // here we can see the result how is working and all of the data, we need to check that the petition is correct. So OK, has to
  // be true and status has to be 200, if the link is wrong the result is gonna be false and status 404. We use an other then
  // so first we ask if res is ok and with the ternary we display two ways of action, 1 to resolve res and the other to reject
  .then(res=>res.ok ? Promise.resolve(res): Promise.reject(res)) // <= never forget this line
  //.then(res=>console.log(res)) // here we see the package but we need to convert it into a JSON using .json()
  .then(data=> data.json())
  // .then(res=> res.json())
  .then(data => {
    cardData = data.results  
    // console.log(cardData)
    cardData = cardData.map(item => {
      const id = item.id;
      const name = item.name;
      const status = item.status;
      const species = item.species;
      const image = item.image;
      return {id,name,status,species,image}
    })
    let card = cardData;
    this.displayCardData(card)
  })
  
}

function displayCardData(card) {
  let fragment = "";
  card.forEach(item => {
    fragment += `
        <!-- Cards Start -->
        <section class="cards">
          
          <figure class="img-container">
            <img src=${item.image} alt=${item.name} class="product-img">
          </figure>
          <section class="card-info">
            <div class="info">
              <h3>${item.name}</h3>
              <h4>${item.species}</h4>
              <h4>${item.status}</h4>
            </div>  
            <span>
              <p>${item.id}</p>
            </span>
          </section>  
        </section>
        <!-- Cards End -->`;
  });
  cardContainer.innerHTML = fragment;
}

