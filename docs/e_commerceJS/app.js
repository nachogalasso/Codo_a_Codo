/* Calling the HTML elements */
const cartBtn = document.querySelector('.cart-btn'); // cart upright
const closeCartBtn = document.querySelector('.close-cart'); // close aside
const clearCartBtn = document.querySelector('.clear-cart'); // clear cart
const cartDOM = document.querySelector('.cart'); // we select the cart container
const cartOverlay = document.querySelector('.cart-overlay'); // to change the class container
const cartItems = document.querySelector('.cart-items'); // cart counter
const cartTotal = document.querySelector('.cart-total'); // total spended
const cartContent = document.querySelector('.cart-content'); // display the content of the cart
const productsDOM = document.querySelector('.products-center'); // fetch the products

// item where we place the information from the localStorage. Is the CART
let cartLocalStorage = []
// create a variable to collect all the buttons so we can use them later
let buttonDOM = []

// class responsible for getting the products. Remember this classes uses a method named constructor(). First we put the name and then the constructor() =>
// class Name {
  // constructor()
// } this is used to create and initialize JS objects

// Getting the products, we call them from products.json
class Products {
  // we use this to await for an answer, and to verify is there is any error
 async getProducts() {
  try {
    let result = await fetch('products.json')
    // so we want the data in products.json, to do that, we create an other variable awaiting for the result
    let data = await result.json()
    // destructuring the object will help us to manage the data better, we put them in a variable
    let products = data.items;
    // now that we have an array, let´s use map to locate our data
    products = products.map(item => {
      const {title,price} = item.fields; // for the title and price
      const {id} = item.sys // to get the item id
      const image = item.fields.image.fields.file.url // to get the item image
      return {title,price,id,image}
    })
    return products
    // return data
  } catch (error) {
    console.log(error)
  }
 }
}

// UI - Display products 
// responsible for manipulating the elements
class UI {
  // don´t forget to pass the variable 'products'
  displayProducts(products) {
    // we create a new variable and then a loop with forEach, so we can pick the elements from our object.
    // gonna take the object properties and put them in out HTML // can I do it with fragment?
    let result = ''
    products.forEach(product => {
      // we want to add with every loop
      result += `
         <!-- First single product -->
        <article class="product">
          <figure class="img-container">
            <img src=${product.image} alt=${product.title} class="product-img">
            <button class="bag-btn" data-id=${product.id}>
              <i class="fa-solid fa-cart-shopping"></i>
              add to cart
            </button>
          </figure>
          <h3>${product.title}</h3>
          <h4>€${product.price}</h4>
        </article>
        <!-- First single product -->
      `;
    })
    productsDOM.innerHTML = result;
    // console.log(products)
  }
  getBagButtons() { // by the moment we don´t pass any variable or arguments
    // because we don´t want the nodelist, we use the spread operator to have an array so [...]
    const bagBtn = [...document.querySelectorAll('.bag-btn')];
    buttonDOM = bagBtn;
    // remeber we access our data using the 'id' we asing to every button
    bagBtn.forEach(button => {
      let id = button.dataset.id; // with this we got the btn id
      // now we create a variable in which we want the program to search in cart for equals id
      let inCart = cartLocalStorage.find(item => item.id === id) // remember by this time we have an empty array in 'cart'
      // we check if the item is in 'cart' so we can disable the button
      if (inCart) { 
        button.textContent = 'In Cart';
        button.disabled = true;
        // this done nothing is we don´t put the eventListener to the button
      }
      
      button.addEventListener('click', (e) => {
        e.target.textContent = "In Cart";
        e.target.disabled = true;
        // console.log(inCart)
        // we are gonna want to get the item from our localStorage
        // 1. GET THE PRODUCTS (put them in a variable)
        // let cartItem = Storage.getProducts(id) // now we sent the items to our empty cart array, again we use a destructor
        let cartItem = {...Storage.getProducts(id), amount:1} // we add a new property amout is for the overlay
        // console.log(cartItem)
        // 2. ADD THE PRODUCTS TO THE CART. instaed of using the pop() method, again we use the deconstructor
        cartLocalStorage = [...cartLocalStorage,cartItem];
        // console.log(cartLocalStorage)
        // 3. SAVE CART IN LOCALSTORAGE
        // we do this, so if the pages refresh or the window is close, the user can access again to the cart
        // we put the function at the storage class
        Storage.saveCart(cartLocalStorage)
        // 4. SET CART VALUES
        this.setCartValues(cartLocalStorage)
        // 5. DISPLAY CART ITEMS IN THE ASIDE
        this.addCartItem(cartItem)
        // 6. SHOW OVERLAY WHEN THE ITEM IS ADDED
        this.showCart()

      })
    
    })
    // console.log(bagBtn)
    // console.log(buttonDOM)
  }
  // this allow us to get the sum of the cart
  setCartValues(cartLocalStorage) {
    // we set the variables for total
    let tempTotal = 0;
    let itemsTotal = 0;
    // we use the map() method to create a new array from the cart
    cartLocalStorage.map(item => {
      // multiply the amount item value
      tempTotal += item.price * item.amount;
      // display total items
      itemsTotal += item.amount;
    })
    // we display the values
    cartTotal.textContent = parseFloat(tempTotal.toFixed(2));
    cartItems.textContent = itemsTotal;
    // console.log(cartTotal,cartItems)
  }

  // now let´s add the items to the cart. We are gonna pass as argument... 'item'
  // but when we call the method, we are gonna pass cartItem either of item, because is gonna have all the information from the storage
  addCartItem(item) {
    // here we create all the cart item from the overlay
    const div = document.createElement('div');
    div.classList.add('cart-item');
    // remember we need the 'id' to update the cart, so we pass it in the span and the two arrows
    div.innerHTML = `
            <img src=${item.image} alt=${item.title}>
            <div class="cart-description">
              <h4>${item.title}</h4>
              <h5>$${item.price}</h5>
              <span class="remove-item">
                <i class="fa-sharp fa-solid fa-trash" data-id=${item.id}></i>
              </span>
            </div>
            <div class="cart-quantity">
              <i class="fa-sharp fa-solid fa-chevron-up" data-id=${item.id}></i>
              <p class="item-amount">${item.amount}</p>
              <i class="fa-sharp fa-solid fa-chevron-down" data-id=${item.id}></i>
    `;
    // don´t forget to append all the content
    cartContent.appendChild(div);
    // console.log(cartContent)
  }

  showCart() {
    cartOverlay.classList.add("transparentBgc");
    cartDOM.classList.add('showCart');
  }

  // we know the products are loaded dinamically when the page opens, but know we need to access our selected items when we leave
  // the page or we reload, that´s why we create the setup, because we already have the cart, we need to access to its values
  setupAPP() {
    // what happens here is that it checks for items in the localStorage and if it finds them, they are displayed in our
    // cartLocalStorage variable
    cartLocalStorage = Storage.getCart();
    // if there are items in the cart so then we execute the method cartValues. Remember to use 'this' to access the method
    // and to pass our cartLocalStorage as a parameter
    this.setCartValues(cartLocalStorage)
    this.populateCart(cartLocalStorage) // we use this to add the items to the cart
    cartBtn.addEventListener('click', this.showCart);
    closeCartBtn.addEventListener('click', this.hideCart)
  }

  populateCart(cartLocalStorage) {
    // because we want to iterate through all the items we use a forEach()
    cartLocalStorage.forEach(item => this.addCartItem(cartLocalStorage))
  }

  hideCart() {
    cartOverlay.classList.remove('transparentBgc');
    cartDOM.classList.remove('showCart');
  }

  cartLogic() {
    // 1. we select the 'remove all' cart button
    clearCartBtn.addEventListener('click', () => {
      this.clearCart() 
    })
    // 2. functionality of the remove and increase or decrease btns from our cart content. We access to them using the e.target
    cartContent.addEventListener('click', (e) => {
      // console.log(e.target) // we use this to see where we clicked
      if (e.target.classList.contains("fa-trash")) {
        let removeItem = e.target;
        let id = removeItem.dataset.id;
        // remember we need to go up to remove all the element from the DOM
        cartContent.removeChild(
          removeItem.parentElement.parentElement.parentElement
        );
        this.removeItems(id);
      } else if (e.target.classList.contains("fa-chevron-up")) {
        let addAmount = e.target;
        let id = addAmount.dataset.id;
        let tempItem = cartLocalStorage.find(item => item.id === id);
        tempItem.amount = tempItem.amount + 1;
        // now we need to update the values from our cart
        Storage.saveCart(cartLocalStorage);
        this.setCartValues(cartLocalStorage);
        addAmount.nextElementSibling.textContent = tempItem.amount;
      }else if(e.target.classList.contains("fa-chevron-down")) {
        let subAmount = e.target;
        let id = subAmount.dataset.id;
        let tempItem = cartLocalStorage.find(item => item.id === id);
        tempItem.amount = tempItem.amount - 1;
        if(tempItem.amount > 0) {
          Storage.saveCart(cartLocalStorage);
          this.setCartValues(cartLocalStorage);
          subAmount.previousElementSibling.textContent = tempItem.amount;
        }else{
          cartContent.removeChild(subAmount.parentElement.parentElement);
          this.removeItems(id)
        }
      }
      
    })
        
      
  }
  

  // here we setup the method to clear the cart
  clearCart() {
    // console.log(this) we can see that this reference to the 'remove all cart button'. It´s important where 'this' is pointing
    // so be careful. Here again we are gonna be looking for the id, so we use map() method again
    let cartItems = cartLocalStorage.map(item => item.id);
    // we loop trough the array to get the id and remove the items
    cartItems.forEach(id => this.removeItems(id))
    // now lets remove all the items from the div, we use the while loop
    while(cartContent.children.length > 0) {
      cartContent.removeChild(cartContent.children[0])
    }
    // don´t forget to hide the cart once all the items are removed
    this.hideCart()
  }

  // we use this method because we want to use it later with an other functionality
  removeItems(id) {
    cartLocalStorage = cartLocalStorage.filter(item => item.id !== id);
    // we update the cart value
    this.setCartValues(cartLocalStorage);
    // to give us the last value of the cart
    Storage.saveCart(cartLocalStorage)
    // and we want to access the buttons so we can add again items to the cart, so we create an other method, we use the id from the
    // removed item
    let button = this.getSingleButton(id);
    button.disabled = false;
    button.innerHTML = `<i class="fa-solid fa-cart-shopping"></i>add to cart`;  
  }

  // to get again the buttons usen the id getting them from the array buttonDOM
  getSingleButton(id) {
    return buttonDOM.find(button => button.dataset.id === id)
  }
}

// LocalStorage
// the information for the cart we are gonna take it from the localStorage
class Storage {
  // we are gonna store using a static method
  static saveProducts(products) {
    localStorage.setItem('products', JSON.stringify(products))
  }
  // now we get the products from the localStorage
  // remember now we use 'id' as the argument to search in the localStorage
  static getProducts(id) {
    // when we get items don´t forget to use parse. Our argument is gonna be again our DB products. This is gonna return an array
    let products = JSON.parse(localStorage.getItem('products'))
    // We use the 'id' to return the product we want. Remember to use the find() method
    return products.find(product => product.id === id)
    // once we get this, we go back to our btn functionallity
  }
  // here goes the new DB with the added cart items
  static saveCart(cartLocalStorage) {
    localStorage.setItem('cart', JSON.stringify(cartLocalStorage))
  }
  // Know we need to check the localStorage to check if there are elements in the cart, we can use an if/else or the ternary operator
  static getCart() {
    return localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []
  }

}


// EventListener from where we are gonna take all the elements
// what we want to happend when the page is loaded. The elements are loaded dinamically
document.addEventListener('DOMContentLoaded', () => {
  // instance we want to be called, those are the class Products and class UI
  const ui = new UI();
  const products = new Products();

  // setup the items to be called if the user left the page
  ui.setupAPP()
  
  // a way to see if our constructor is calling all products
  // products.getProducts().then(products => console.log(products))
  // here comes the ui to display our products
  products.getProducts().then(products => {
   // here is where we call and storage all the products in the localStorage
   ui.displayProducts(products);
   Storage.saveProducts(products) // remember... to get back the information we need to use JSON.Parse
  }).then(() => { // we use an other then so it will deploy after all our products are display. At the ui class we configure the function
    ui.getBagButtons()
    // we ad a new logic for the cart to add more items or remove them all
    ui.cartLogic()
  })
})