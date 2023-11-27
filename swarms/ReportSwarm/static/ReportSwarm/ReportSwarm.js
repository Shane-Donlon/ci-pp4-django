// form input css selector for all input in form
let AllInputs = document.querySelectorAll("form input");
let confirmationCheckbox = document.querySelector("#checkbox");
let formWrapper = document.querySelector(".form-wrapper").children;

AllInputs.forEach((input) => {
  /**  on page load disable all the input fields for the form, this will be toggled with an event listener
   *as an image is required in Step2 of the form, I am seeking confirmation that the user understands this before proceeding, 
   and that this image upload will not be a surprise for the user when reaching step2
   */
  input.disabled = true;
});

confirmationCheckbox.addEventListener("input", (e) => {
  /**  toggle the disabled attribute on and off when the checkbox is checked or unchecked
   */
  let value = true;
  if (confirmationCheckbox.checked) {
    value = !value;
  }
  AllInputs.forEach((input) => {
    input.disabled = value;
  });
});

addRequiredAsterisksToLabels();

function addRequiredAsterisksToLabels() {
  /** 
 The form will have 3 sections in each section loop through the children (label and inputs)
    if the current input has the attribute required then the preceding label will have class added for labelRequiredAsterisk
    this will be used for the CSS pseudo element to add "*" to the labels of the inputs that are required and saves hardcoding this
 */

  for (let index = 0; index < formWrapper.length; index++) {
    const child = formWrapper[index];
    for (let index = 0; index < child.children.length; index++) {
      const childEl = child.children[index];
      if (childEl.hasAttribute("required")) {
        child.children[index - 1].classList.add("labelRequiredAsterisk");
      }
    }
  }
}
