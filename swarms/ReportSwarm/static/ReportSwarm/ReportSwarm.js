// form input css selector for all input in form
let AllInputs = document.querySelectorAll("form input");
let confirmationCheckbox = document.querySelector("#checkbox");

AllInputs.forEach((input) => {
  input.disabled = true;
});

confirmationCheckbox.addEventListener("input", (e) => {
  let value = true;
  if (confirmationCheckbox.checked) {
    value = !value;
  }
  AllInputs.forEach((input) => {
    input.disabled = value;
  });
});
