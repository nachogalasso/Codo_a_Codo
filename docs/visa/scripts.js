/* VISA modal */
const modal = document.getElementById('myModal');
const openModal = document.getElementById('openModal');
const closeModal = document.querySelector('.close');

console.log(modal);
console.log(openModal);
console.log(closeModal);

openModal.addEventListener('click', () => {
  modal.classList.add('show')
})

closeModal.addEventListener('click', () => {
  modal.classList.remove('show')
})