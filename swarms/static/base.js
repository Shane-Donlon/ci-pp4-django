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

const primaryHeader = document.querySelector("header");
const scrollWatcher = document.createElement("div");

scrollWatcher.setAttribute("data-scroll-watcher", "");
primaryHeader.before(scrollWatcher);

const navObserver = new IntersectionObserver(
  (entries) => {
    primaryHeader.classList.toggle(
      "box-shadow-show",
      !entries[0].isIntersecting
    );
  },
  { rootMargin: "50px 0px 0px 0px" }
);

navObserver.observe(scrollWatcher);
