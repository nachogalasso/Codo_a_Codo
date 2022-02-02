/* PROJECTS SCRIPTS SHEET */

/* TOGGLE NAVBAR */
const navToggle = document.querySelector('.toggle-menu');
const links = document.querySelector('.links');


navToggle.addEventListener('click', () => {
    links.classList.toggle('show-links');
})



/* TIP GENERATOR */
// Calling the elements
const money = document.getElementById('money');
const tip = document.getElementById('tip');
const diners = document.getElementById('diners');
const enterBtn = document.querySelector('.enter-btn');
const amout = document.getElementById('amout');
const tipValue = document.getElementById('tip-value');
const total = document.getElementById('total');
const pay = document.getElementById('pay');


enterBtn.addEventListener('click', () => {
    
    amout.textContent = `Ticket: ${money.value}`;
    // amout.classList.toggle('show');
    
    let totalTip = (money.value * tip.value) / 100;
    tipValue.textContent = `Tip: ${totalTip}`;
    // tipValue.classList.toggle('show');
    
    let totalEach = parseInt(totalTip) + parseInt(money.value);
    total.textContent = `Ticket + Tip: ${totalEach}`;
    // total.classList.toggle('show');
    
    let totalPay =  totalEach / diners.value;
    pay.textContent = `Total Each: ${totalPay}`;
    // pay.classList.toggle('show');

    money.value = '';
    tip.value = '';
    diners.value = '';
})

