document.addEventListener('DOMContentLoaded', () => {
  console.log('app.js is loaded');

  const wrapper = document.querySelector(".sliderWrapper");
  const menuItems = document.querySelectorAll(".menuItem");

  const products = [
    // Product objects
  ];

  let choosenProduct = products[0];

  const currentProductImg = document.querySelector(".productImg");
  const currentProductTitle = document.querySelector(".productTitle");
  const currentProductPrice = document.querySelector(".productPrice");
  const currentProductColors = document.querySelectorAll(".color");
  const currentProductSizes = document.querySelectorAll(".size");

  menuItems.forEach((item, index) => {
    item.addEventListener("click", () => {
      console.log("Menu item clicked:", index);
      wrapper.style.transform = `translateX(${-100 * index}vw)`;
      choosenProduct = products[index];
      currentProductTitle.textContent = choosenProduct.title;
      currentProductPrice.textContent = "Ghc" + choosenProduct.price;
      currentProductImg.src = choosenProduct.colors[0].img;
      currentProductColors.forEach((color, index) => {
        color.style.backgroundColor = choosenProduct.colors[index].code;
      });
    });
  });

  currentProductColors.forEach((color, index) => {
    color.addEventListener("click", () => {
      console.log("Color clicked:", index);
      currentProductImg.src = choosenProduct.colors[index].img;
    });
  });

  currentProductSizes.forEach((size, index) => {
    size.addEventListener("click", () => {
      console.log("Size clicked:", index);
      currentProductSizes.forEach((size) => {
        size.style.backgroundColor = "white";
        size.style.color = "black";
      });
      size.style.backgroundColor = "black";
      size.style.color = "white";
    });
  });

  const productButton = document.querySelector(".productButton");
  const payment = document.querySelector(".payment");
  const close = document.querySelector(".close");

  productButton.addEventListener("click", () => {
    console.log("Product button clicked");
    payment.style.display = "flex";
  });

  close.addEventListener("click", () => {
    console.log("Close button clicked");
    payment.style.display = "none";
  });
});