/* COLOR FLIPPER */
const colors = ["#1abc9c", "#2ecc71", "#e67e22", "#f1c40f", "#8e44ad", "#34495e", "#c0392b", "#7f8c8d", "#bdc3c7"]
const hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'];
const container = document.querySelector('.container');
const colorBtn = document.getElementById('flipper-btn');
const textColor = document.getElementById('flipper-text');

/* Pick a random number from "hex" array */
const getRandomColor = () => {
    return Math.floor( Math.random() * hex.length);
}

// colorBtn.addEventListener('click', () => {
//     let randomNumber = getRandomColor();
//     console.log(randomNumber);
    
//     container.style.backgroundColor = colors[randomNumber];
//     textColor.textContent = colors[randomNumber];
// })

/* Button event */
colorBtn.addEventListener('click', () => {
    let hexColor = '#';
    for(let i = 0; i < 6; i++) {
        hexColor += hex[getRandomColor()]
    }

    container.style.backgroundColor = hexColor;
    textColor.textContent = hexColor.toLocaleLowerCase();
})