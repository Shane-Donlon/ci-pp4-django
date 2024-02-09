const btn = document.querySelector("button");
let phoneError = "Please enter phone number in 353121234567 format";
btn.addEventListener("click", (e) => {
  e.preventDefault();

  let inputs = document.querySelectorAll(".form-group input");
  let countyValue = document.querySelector("#id_county");

  validateRequredInputPersonalDetails(inputs);
  validateCounty(countyValue.value);

  if (
    validateRequredInputPersonalDetails(inputs) &&
    validateCounty(countyValue.value)
  ) {
    let form = document.querySelector("form");
    form.submit();
    alert("form has been updated");
  }
});

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
function validateRequredInputPersonalDetails(listOfInputs) {
  let valid = [];
  let correct = false;
  listOfInputs.forEach((input) => {
    if (!input.validity.valid) {
      valid.push(false);

      if (input.id === "id_phone") {
        input.setCustomValidity(`${phoneError}`);
      }
      input.nextElementSibling.classList.remove("display-none");
      input.nextElementSibling.classList.add("errors");

      input.nextElementSibling.innerText = `${input.validationMessage}`;
      input.setCustomValidity("");
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
