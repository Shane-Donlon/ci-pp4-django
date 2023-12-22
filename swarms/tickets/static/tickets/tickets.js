let form = document.querySelector(".filterForm");
let filterFormInputs = document.querySelectorAll(
  ".filterForm > *:not(label):not(button)"
);

filterFormInputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    /**
     * Reduce need for pressing search button
     * form will submit on input, but with a debounce function with delay
     */
    updateRequest(form);
  });
});

function delayedFn(cb, delay = 750) {
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
