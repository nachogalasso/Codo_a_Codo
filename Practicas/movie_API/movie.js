// API key: bcb15a10e5eb9c38eb1ee8b524063500
// API link: https://api.themoviedb.org/3/movie/550?api_key=(here goes the key)
// API token: eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiY2IxNWExMGU1ZWI5YzM4ZWIxZWU4YjUyNDA2MzUwMCIsInN1YiI6IjYzNmQ0NWFhMDQ5OWYyMDBhNjYyNzBlOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7i3bFaAUix4CZQHKXES-58y-7dDjy-i1S3ALcIxaSik

// HTML elements
const cardsDisplay = document.querySelector(".cards-display");
const searchForm = document.querySelector(".search-form");
const getSearch = document.getElementById("search");

// Control Variables
const linkAPI = "https://localhost:8000/";
// const imgPath = "https://image.tmdb.org/t/p/w1280";
// const searchAPI =
//    "https://api.themoviedb.org/3/search/movie?&api_key=bcb15a10e5eb9c38eb1ee8b524063500&query=";

// App functionality

//get Movies
getMovies(linkAPI);
async function getMovies(url) {
   try {
      let result = await fetch(url);
      let data = await result.json();
      let movies = await data.results;
      movies = movies.map((item) => {
         const title = item.title;
         const id = item.id;
         const overview = item.overview;
         const image = imgPath + item.poster_path;
         const genre = item.genre_ids;
         const date = item.release_date;
         return { title, id, overview, image, genre, date };
      });

      let getDisplay = "";
      movies.forEach((movie) => {
         getDisplay += `
          <div class="card-container" data-id=${movie.id}>
            <figure class="card">
               <img src="${movie.image}" alt="${movie.title}" loading="lazy">
            </figure>
            <h3 class="card-title">${movie.title}</h3>
            <p>${movie.genre}</p>
            <p>${movie.overview}</p>
            <p>${movie.date}</p>
         </div> `;
      });
      cardsDisplay.innerHTML = getDisplay;
   } catch (error) {
      console.log(error);
   }
}

// document.addEventListener('DOMContentLoaded', () => {

//    getMovies()
// })
searchForm.addEventListener("submit", (e) => {
   e.preventDefault();
   cardsDisplay.innerHTML = "";
   const searchItem = getSearch.value;
   if (searchItem) {
      getMovies(searchAPI + searchItem);
      getSearch.value = "";
   }
});
