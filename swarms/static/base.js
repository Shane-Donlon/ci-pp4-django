let hamburgerMenu = document.querySelector(".menu-icon");
document.querySelector(".copyright-year").textContent =
  new Date().getFullYear();

hamburgerMenu.addEventListener("click", (e) => {
  let nav = document.querySelector(".nav");
  let body = document.querySelector("body");
  nav.classList.toggle("menu-open");
  if (nav.classList.contains("menu-open")) {
    body.style.overflow = "hidden";
  } else {
    body.style.removeProperty("overflow");
  }
});
