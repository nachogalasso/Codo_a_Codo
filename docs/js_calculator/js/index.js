// Display elements for numbers and operations
const displayCount = document.getElementById('count');
const displayResult = document.getElementById('result');
// Buttons for numbers and operators
const btnNumber = document.querySelectorAll('.get');
const operatorBtn = document.querySelectorAll('.operator');
const deleteNum = document.querySelector('.delete');
const resetBtn = document.getElementById('restart');

// Don´t forget to call the class display
const display = new Display(displayCount, displayResult);

// This function allows us to bring the values from the buttons
btnNumber.forEach(button => {
    button.addEventListener('click', () => {
        display.addNumber(button.innerHTML); 
        // console.log(button)
    });
});

deleteNum.addEventListener('click', () => {
    display.delete();
});

resetBtn.addEventListener('click', () => {
    display.reset();
});

operatorBtn.forEach(opbtn => {
    opbtn.addEventListener('click', () => {
        // display.addNumber(opbtn.innerHTML);
        display.calculate(opbtn.value);
    })
});


// Console.log to check y the elements are correctly called
// console.log(operator);
// console.log(btnNumber);
// console.log(deleteNum);
// Now we check if our constructor functions work correctly. For a better execution is recomended to use an other js where we put all our display functions.
// const calculator = new Calculator();
// console.log(calculator.sum(2, 3));
// console.log(calculator.sub(2, 3));
// console.log(calculator.multiply(2, 3));
// console.log(calculator.divide(2, 3));