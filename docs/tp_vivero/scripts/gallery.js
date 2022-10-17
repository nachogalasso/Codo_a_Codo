/* Let´s bring the elements */
/* NAVBAR ELEMENTS */
const navList = document.getElementById("nav-list");
const iconMenu = document.getElementById("toggle-menu");
const mainLogo = document.getElementById("main-logo");

/* NEW ELEMENTS */
const cartBtn = document.querySelector(".cart-btn");
const closeCartBtn = document.querySelector(".close-cart");
const clearCartBtn = document.querySelector(".clear-cart");
const cartDOM = document.querySelector(".cart");
const cartOverlay = document.querySelector(".cart-overlay");
const cartItems = document.querySelector(".cart-items");
const cartTotal = document.querySelector(".cart-total");
const cartContent = document.querySelector(".cart-content");
const productsDOM = document.querySelector(".gallery__products");
const category = [...document.querySelectorAll(".aside-listitem")];

/* Navbar EVENT */
iconMenu.addEventListener("click", () => {
  mainLogo.classList.toggle("logo-nav");
  navList.classList.toggle("nav-list-show");
});

/* Gallery display 
viewSeeds.addEventListener('click', () => {
    seeds.classList.remove('hidden');
    seedlings.classList.add('hidden');
    subtrates.classList.add('hidden');
    utensils.classList.add('hidden');
})

viewSeedlings.addEventListener('click', () => {
    seedlings.classList.remove('hidden');
    seeds.classList.add('hidden');
    subtrates.classList.add('hidden');
    utensils.classList.add('hidden');
})

viewSubtrates.addEventListener('click', () => {
    subtrates.classList.remove('hidden');
    seedlings.classList.add('hidden');
    seeds.classList.add('hidden');
    utensils.classList.add('hidden');
})

viewUtensils.addEventListener('click', () => {
    utensils.classList.remove('hidden');
    subtrates.classList.add('hidden');
    seeds.classList.add('hidden');
    seedlings.classList.add('hidden');
})

viewAll.addEventListener('click', () => {
    seeds.classList.remove('hidden');
    seedlings.classList.remove('hidden');    
    subtrates.classList.remove('hidden');
    utensils.classList.remove('hidden');
}) */

// Variables to collect information
let cart = [];
let buttonDOM = [];

// Get products

class Products {
  async getProducts() {
    try {
      let result = await fetch("products.json");
      let data = await result.json();
      let products = data.items;
      products = products.map((item) => {
        const { title, price, category } = item.fields;
        const { id } = item.sys;
        const image = item.fields.image.fields.file.url;
        return { title, price, category, id, image };
      });
      return products;
    } catch (error) {
      console.log(error);
    }
  }
}
// UI - Display products
class UI {
  // displayProducts(products) {
  //   let result = "";
  //   let x = products.map(x => x.category)

  //   products.forEach((product) => {
  //     result += `
  //           <article class="product" data-title=${product.category}>
  //               <figure class="card-container">
  //                   <img src=${product.image} alt=${product.title} class="product-img">
  //                   <button class="bag-btn" data-id=${product.id}>
  //                       <i class="fa-solid fa-cart-shopping"></i>add to cart
  //                   </button>
  //               </figure>
  //               <h3>${product.title}</h3>
  //               <p>$${product.price}</p>
  //           </article>`;

  //       });

  //   productsDOM.innerHTML = result;

  //    category.forEach((itemCat) => {
  //      itemCat.addEventListener("click", (e) => {
  //        let catItem = e.target.classList[1];
  //      });
  //    });

  // }

  displayProducts(products) {
    let result = "";
    

    products.forEach((product) => {
      result += `
            <article class="product" data-filter=${product.category}>
                <figure class="card-container">
                    <img src=${product.image} alt=${product.title} class="product-img">
                    <button class="bag-btn" data-id=${product.id}>
                        <i class="fa-solid fa-cart-shopping"></i>add to cart
                    </button>
                </figure>
                <h3>${product.title}</h3>
                <p>$${product.price}</p>
            </article>`;
    });
    
    productsDOM.innerHTML = result;

    console.log(result[1])


    category.forEach((itemCat) => {
      itemCat.addEventListener("click", (e) => {
        let catItem = e.target.classList[1];
        let x = products.map((x) => x.category);
        if(catItem === result.getAttribute('data-category')){
          console.log(v)
        }

        })
    });
    
  }

  getBagButtons() {
    const bagBtn = [...document.querySelectorAll(".bag-btn")];
    buttonDOM = bagBtn;

    bagBtn.forEach((button) => {
      let id = button.dataset.id;
      let inCart = cart.find((item) => item.id === id);
      if (inCart) {
        button.textContent = "In Cart";
        button.disabled = true;
      }

      button.addEventListener("click", (e) => {
        e.target.textContent = "In Cart";
        e.target.disabled = true;

        let cartItem = { ...Storage.getProducts(id), amount: 1 };
        cart = [...cart, cartItem];

        Storage.saveCart(cart);

        this.setCartValues(cart);
        this.addCartItem(cartItem);
        this.showCart();
      });
    });
  }

  setCartValues(cart) {
    let tempTotal = 0;
    let itemsTotal = 0;
    cart.map((item) => {
      tempTotal += item.price * item.amount;
      itemsTotal += item.amount;
    });
    cartTotal.textContent = parseFloat(tempTotal.toFixed(2));
    cartItems.textContent = itemsTotal;
  }

  addCartItem(item) {
    const div = document.createElement("div");
    div.classList.add("cart-item");
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
            </div>`;
    cartContent.appendChild(div);
  }

  showCart() {
    cartOverlay.classList.add("transparentBgc");
    cartDOM.classList.add("showCart");
  }

  setupAPP() {
    cart = Storage.getCart();
    this.setCartValues(cart);
    this.populateCart(cart);
    cartBtn.addEventListener("click", this.showCart);
    closeCartBtn.addEventListener("click", this.hideCart);
  }

  populateCart(cart) {
    cart.forEach((item) => this.addCartItem(cart));
  }

  hideCart() {
    cartOverlay.classList.remove("transparentBgc");
    cartDOM.classList.remove("showCart");
  }

  cartLogic() {
    clearCartBtn.addEventListener("click", () => {
      this.clearCart();
    });
    cartContent.addEventListener("click", (e) => {
      if (e.target.classList.contains("fa-trash")) {
        let removeItem = e.target;
        let id = removeItem.dataset.id;
        cartContent.removeChild(
          removeItem.parentElement.parentElement.parentElement
        );
        this.removeItems(id);
      } else if (e.target.classList.contains("fa-chevron-up")) {
        let addAmount = e.target;
        let id = addAmount.dataset.id;
        let tempItem = cart.find((item) => item.id === id);
        tempItem.amount = tempItem.amount + 1;
        Storage.saveCart(cart);
        this.setCartValues(cart);
        addAmount.nextElementSibling.textContent = tempItem.amount;
      } else if (e.target.classList.contains("fa-chevron-down")) {
        let subAmount = e.target;
        let id = subAmount.dataset.id;
        let tempItem = cart.find((item) => item.id === id);
        tempItem.amount = tempItem.amount - 1;
        if (tempItem.amount > 0) {
          Storage.saveCart(cart);
          this.setCartValues(cart);
          subAmount.previousElementSibling.textContent = tempItem.amount;
        } else {
          cartContent.removeChild(subAmount.parentElement.parentElement);
          this.removeItems(id);
        }
      }
    });
  }

  clearCart() {
    let cartItems = cart.map((item) => item.id);
    cartItems.forEach((id) => this.removeItems(id));
    while (cartContent.children.length > 0) {
      cartContent.removeChild(cartContent.children[0]);
    }
    this.hideCart();
  }

  removeItems(id) {
    cart = cart.filter((item) => item.id !== id);
    this.setCartValues(cart);
    Storage.saveCart(cart);
    let button = this.getSingleButton(id);
    button.disabled = false;
    button.innerHTML = `<i class="fa-solid fa-cart-shopping"></i>add to cart`;
  }

  getSingleButton(id) {
    return buttonDOM.find((button) => button.dataset.id === id);
  }
}

// localStorage Items
class Storage {
  // products from JSON to localStorage
  static saveProducts(products) {
    localStorage.setItem("products", JSON.stringify(products));
  }
  // get Products from localStorage, use id
  static getProducts(id) {
    let products = JSON.parse(localStorage.getItem("products"));
    return products.find((product) => product.id === id);
  }
  // new DB for the cart
  static saveCart(cart) {
    localStorage.setItem("cart", JSON.stringify(cart));
  }
  // check the cart for items
  static getCart() {
    return localStorage.getItem("cart")
      ? JSON.parse(localStorage.getItem("cart"))
      : [];
  }
}

// Load elements with page load
document.addEventListener("DOMContentLoaded", () => {
  const ui = new UI();
  const products = new Products();

  ui.setupAPP();

  products
    .getProducts()
    .then((products) => {
      ui.displayProducts(products);
      Storage.saveProducts(products);
    })
    .then(() => {
      ui.getBagButtons();
      ui.cartLogic();
    });
});
