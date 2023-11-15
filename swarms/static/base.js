console.log("base.js working");
let beekeeperMenu = document.querySelector(".beekeeper-expanding");
let beekeeperUL = document.querySelector(".beekeeper-ul");
beekeeperMenu.addEventListener("click", (e) => {
  beekeeperUL.classList.toggle("opened");
  console.log(e);
});

document.querySelector(".copyright-year").textContent =
  new Date().getFullYear();
