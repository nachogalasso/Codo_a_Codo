/* COUNTER */
const dspValue = document.getElementById('ctr');
const btn = document.querySelectorAll('.btn');

let count = 0;

btn.forEach(function (btns) {
    // console.log(btns);
    btns.addEventListener('click', (e) => {
        // console.log(e.currentTarget)
        const styles = e.currentTarget.classList;
        if(styles.contains('decrease')){
            count--;
        }else if(styles.contains('increase')) {
            count++;
        }else{
            count = 0;
        }
        if(count > 0) {
            dspValue.style.color = 'green';
        }else if(count < 0) {
            dspValue.style.color = 'red';
        }else{ //tambien puedo usar if(count === 0)
            dspValue.style.color = 'black';
        }

        dspValue.textContent = count;
    })
})