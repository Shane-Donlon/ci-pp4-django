let form = document.querySelector(".filterForm");
let filterFormInputs = document.querySelectorAll(
  ".filterForm > *:not(label):not(button)"
);

const modal = document.querySelector("dialog");
const modalOpenBtn = document.querySelector(".helpBtn");
const modalCloseBtn = document.querySelector(".dialogCloseBtn");

modalOpenBtn.addEventListener("click", (e) => {
  modal.showModal();
});

modalCloseBtn.addEventListener("click", (e) => {
  modal.close();
});

filterFormInputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    /**
     * Reduce need for pressing search button
     * form will submit on input, but with a debounce function with delay
     */
    updateRequest(form);
  });
});

function delayedFn(cb, delay = 1000) {
  let timeout;

  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      cb(...args);
    }, delay);
  };
}

const updateRequest = delayedFn((searchForm) => {
  searchForm.submit();
});
