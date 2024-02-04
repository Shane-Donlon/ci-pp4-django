// form input css selector for all input in form
let PersonalDetailsInputs = document.querySelectorAll(
  ".personal-details-fieldset input"
);
// All inputs includes select and text area not just input fields
let allInputs = document.querySelectorAll(".form-group >*:not(label):not(p)");

let confirmationCheckbox = document.querySelector("#checkbox");
let formWrapper = document.querySelectorAll(".form-group");
let NextBtn = document.querySelector("#next");
let allBtns = document.querySelectorAll(".btn");

// I could just index allBtns to the correct btn, but for readability of code I'll declare them independently
let NextBtn2 = document.querySelector("#nextBtn2");
let PrevBtn2 = document.querySelector("#prevBtn2");
let resetBtn = document.querySelector(".reset-btn");
let eircodeField = document.querySelector("#id_eircode");
let progressCircles = document.querySelectorAll(".circle");
let progressBar = document.querySelector("#progress");
let PersonalDetailsFieldset = document.querySelector(
  ".personal-details-fieldset"
);
let honeyBeeDetailsFieldset = document.querySelector(".honeyBee-fieldset");
let backBtn = document.querySelector("#prev");
const submitBtn = document.querySelector(".submit-btn");
allInputs.forEach((input) => {
  /**  on page load disable all the input fields for the form, this will be toggled with an event listener
   *as an image is required in Step2 of the form, I am seeking confirmation that the user understands this before proceeding, 
   and that this image upload will not be a surprise for the user when reaching step2
   */
  input.disabled = true;
  allBtns.forEach((btn) => {
    btn.disabled = true;
  });
});

confirmationCheckbox.addEventListener("input", (e) => {
  /**  toggle the disabled attribute on and off when the checkbox is checked or unchecked
   */
  let value = true;
  if (confirmationCheckbox.checked) {
    value = !value;
  }
  allInputs.forEach((input) => {
    input.disabled = value;
  });
  allBtns.forEach((btn) => {
    if (!btn.classList.contains("btn-disabled")) {
      btn.disabled = value;
    }
  });
});

addRequiredAsterisksToLabels();

function addRequiredAsterisksToLabels() {
  /** 
 The form will have 3 sections in each section loop through the children (label and inputs)
    if the current input has the attribute required then the preceding label will have class added for labelRequiredAsterisk
    this will be used for the CSS pseudo element to add "*" to the labels of the inputs that are required and saves hardcoding this
 */

  formWrapper.forEach((fieldset) => {
    for (let index = 0; index < fieldset.children.length; index++) {
      const childEl = fieldset.children[index];
      if (childEl.hasAttribute("required")) {
        fieldset.children[index - 1].classList.add("labelRequiredAsterisk");
      }
    }
  });
}

PersonalDetailsInputs.forEach((input) => {
  input.addEventListener("change", (event) => {
    /** 
     * 
First if checks if the field is blank, then raises error if so using the labels inner text
EG. if First Name label then error, "First Name: is required" will be the error
Then if the current input is invalid raise the standard HTML validation error in the paragraph below the input.
then wait for 3 seconds and remove the error message.

 */
    let textValue = input.value.trim().length;
    generalValidation(event, textValue, input, 3000);
  });
});

NextBtn.addEventListener("click", (e) => {
  let countyValue = document.querySelector("#id_county").value;

  validateCounty(countyValue);
  checkEircode(eircodeField.value, eircodeField);
  validateRequredInputPersonalDetails(PersonalDetailsInputs);

  if (
    validateCounty(countyValue) &&
    checkEircode(eircodeField.value, eircodeField) &&
    validateRequredInputPersonalDetails(PersonalDetailsInputs)
  ) {
    // all form fields passed validation
    // open the next section of the form
    // set the 1st circle to green
    // set the 2nd circle to yellow
    // set progress bar value to 50%

    progressCircles[0].classList.add("completed");
    progressBar.value = 50;
    progressCircles[0].classList.remove("active");
    progressCircles[1].classList.add("active");
    let currentPanel = document.querySelector("#personalDetailsTab");
    let nextPanel = document.querySelector("#honeyBeeDetailsTab");
    currentPanel.setAttribute("hidden", "true");

    nextPanel.removeAttribute("hidden");
  }
});
NextBtn2.addEventListener("click", (e) => {
  // some inputs are TextArea some are Select, css selector below selects everything that is not a label or error message
  let inputs = document.querySelectorAll(
    ".honeyBee-fieldset > .form-group > *:not(label):not(p)"
  );

  if (validateRequredInputPersonalDetails(inputs)) {
    let currentPanel = document.querySelector("#honeyBeeDetailsTab");
    let nextPanel = document.querySelector("#confirmationTab");
    currentPanel.setAttribute("hidden", "true");

    nextPanel.removeAttribute("hidden");
    progressCircles[1].classList.add("completed");
    progressBar.value = 100;
    progressCircles[1].classList.remove("active");
    progressCircles[2].classList.add("active");
  }
});

backBtn.addEventListener("click", (e) => {
  // this is step 3 of the form go back to step 2
  let currentPanel = document.querySelector("#confirmationTab");
  let lastPanel = document.querySelector("#honeyBeeDetailsTab");

  currentPanel.setAttribute("hidden", "true");
  lastPanel.removeAttribute("hidden");
  progressCircles[1].classList.add("active");
  progressBar.value = 50;
  progressCircles[2].classList.remove("completed");
  progressCircles[2].classList.remove("active");
});

PrevBtn2.addEventListener("click", (e) => {
  // this is step 2 of the form go back to step 1
  let currentPanel = document.querySelector("#honeyBeeDetailsTab");
  let lastPanel = document.querySelector("#personalDetailsTab");

  currentPanel.setAttribute("hidden", "true");
  lastPanel.removeAttribute("hidden");
  progressCircles[0].classList.add("active");
  progressBar.value = 50;
  progressCircles[1].classList.remove("completed");
  progressCircles[1].classList.remove("active");
  progressBar.value = 0;
});

resetBtn.addEventListener("click", (e) => {
  let currentPanel = document.querySelector("#confirmationTab");
  let lastPanel = document.querySelector("#personalDetailsTab");

  currentPanel.setAttribute("hidden", "true");
  lastPanel.removeAttribute("hidden");
  progressCircles[0].classList.add("active");

  progressCircles[1].classList.remove("completed");
  progressCircles[2].classList.remove("completed");
  progressCircles[2].classList.remove("active");
  progressBar.value = 0;
});
function checkEircode(eircode, eircodeSelector) {
  /** 
Eircode format should be 3 characters space 4 characters
eg
E98 PO89
if E98PO89 convert to E98 PO89
OR if not uppercase convert to uppercase
 */
  let correct = false;
  if (eircode.length < 7) {
    // if less than 7 characters do nothing
    return;
  }
  let wordArray = eircode.split("");

  if (wordArray[3] != " ") {
    let correctCode = [
      wordArray[0],
      wordArray[1],
      wordArray[2],
      " ",
      wordArray[3],
      wordArray[4],
      wordArray[5],
      wordArray[6],
    ];
    let codeAsString = correctCode.toString();
    codeAsString = codeAsString.replaceAll(",", "");
    codeAsString = codeAsString.toUpperCase();
    eircodeSelector.value = codeAsString;
    correct = true;
  } else {
    eircodeSelector.value = eircodeField.value.toUpperCase();
    correct = true;
  }
  return correct;
}

function validateCounty(countyValue) {
  countyValue = countyValue.trim();
  let inList = false;
  let allCounties = [
    "Antrim",
    "Armagh",
    "Carlow",
    "Cavan",
    "Clare",
    "Cork",
    "Derry",
    "Donegal",
    "Down",
    "Dublin",
    "Fermanagh",
    "Galway",
    "Kerry",
    "Kildare",
    "Kilkenny",
    "Laois",
    "Leitrim",
    "Limerick",
    "Longford",
    "Louth",
    "Mayo",
    "Meath",
    "Monaghan",
    "Offaly",
    "Roscommon",
    "Sligo",
    "Tipperary",
    "Tyrone",
    "Waterford",
    "Westmeath",
    "Wexford",
    "Wicklow",
  ];

  allCounties.forEach((current) => {
    if (current.toLowerCase() === countyValue.toLowerCase()) {
      return (inList = true);
    }
  });

  if (!inList) {
    let countiesErrors = document.querySelector(".countiesErrors");
    countiesErrors.classList.remove("display-none");
    countiesErrors.classList.add("errors");
    countiesErrors.innerText = "Please select a valid county from the list";
    setTimeout(() => {
      countiesErrors.innerText = "";
      countiesErrors.classList.remove("errors");
      countiesErrors.classList.add("display-none");
    }, 3000);
  }
  return inList;
}

function generalValidation(event, textValue, input, timeOutInMs) {
  if (!textValue && input.hasAttribute("required")) {
    event.target.nextElementSibling.classList.remove("display-none");
    event.target.nextElementSibling.classList.add("errors");
    if (event.target.id === "id_phone" && event.target.value.length >= 1) {
      event.target.setCustomValidity(
        "Please enter phone number in 353121234567 format"
      );
    }
    event.target.nextElementSibling.innerText = `${event.target.labels[0].innerText} is required`;
    setTimeout(() => {
      event.target.nextElementSibling.innerText = "";
      event.target.nextElementSibling.classList.remove("errors");
      event.target.nextElementSibling.classList.add("display-none");
    }, timeOutInMs);
  } else if (
    !event.target.validity.valid &&
    event.target.nextElementSibling.classList.contains("display-none")
  ) {
    event.target.nextElementSibling.classList.remove("display-none");
    event.target.nextElementSibling.classList.add("errors");
    event.target.nextElementSibling.innerText = `${event.target.validationMessage}`;
    setTimeout(() => {
      event.target.nextElementSibling.innerText = "";
      event.target.nextElementSibling.classList.remove("errors");
      event.target.nextElementSibling.classList.add("display-none");
    }, timeOutInMs);
  }
}

function validateRequredInputPersonalDetails(listOfInputs) {
  let valid = [];
  let correct = false;
  listOfInputs.forEach((input) => {
    if (!input.validity.valid) {
      valid.push(false);
      if (input.id === "id_phone" && input.value.length >= 1) {
        input.setCustomValidity(
          "Please enter phone number in 353121234567 format"
        );
      }
      input.nextElementSibling.classList.remove("display-none");
      input.nextElementSibling.classList.add("errors");

      input.nextElementSibling.innerText = `${input.validationMessage}`;
      setTimeout(() => {
        input.nextElementSibling.innerText = "";
        input.nextElementSibling.classList.remove("errors");
        input.nextElementSibling.classList.add("display-none");
      }, 3000);
    } else {
      // the field is required and so a blank space fills the requirement, checking if empty string in field
      let inputValue = input.value.trim();
      if (input.hasAttribute("required") && inputValue.length === 0) {
        input.nextElementSibling.classList.remove("display-none");
        input.nextElementSibling.classList.add("errors");
        input.nextElementSibling.innerText = `${input.previousElementSibling.innerText} is required`;
        valid.push(false);
        setTimeout(() => {
          input.nextElementSibling.innerText = "";
          input.nextElementSibling.classList.remove("errors");
          input.nextElementSibling.classList.add("display-none");
        }, 3000);
      }
    }
  });
  if (valid.length === 0) {
    correct = true;
    listOfInputs.forEach((input) => {
      if (input.type != "file") {
        // file types have a length of 0 but are valid once a file is added
        input.value = input.value.trim();
      }
    });
  }

  return correct;
}

allInputs.forEach((input, ind) => {
  input.addEventListener("input", (e) => {
    let confirmationArea = document.querySelectorAll(".label-value");
    confirmationArea[ind].innerText = input.value;
  });
});

let tabPanels = document.querySelectorAll(".tab-panel");

tabPanels.forEach((tab, index) => {
  if (!index) {
    // console.log(0);
  } else {
    tab.setAttribute("hidden", "");
  }
});

submitBtn.addEventListener("click", (e) => {
  let form = document.querySelector("form");
  e.preventDefault();
  const newDiv = document.createElement("div");
  const innerDiv = `<div class="loader-div"></div>`;
  newDiv.className = "loader-bg";
  newDiv.innerHTML = innerDiv;

  document.body.append(newDiv);
  document.body.style.overflow = "hidden";
  form.submit();
});

let imgInput = document.querySelector("#id_image");
imgInput.setAttribute("capture", "user");
