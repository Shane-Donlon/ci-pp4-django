let allFields = document.querySelectorAll(".form-div :not(label)");
let submitBtnAdmin = document.querySelector(".submit-description");
let checkboxAllFields = document.querySelector("#checkboxAllFields");
let deleteBtn = document.querySelector(".delete-ppi-btn");
checkboxAllFields.addEventListener("change", (e) => {
  if (checkboxAllFields.checked) {
    allFields.forEach((field) => {
      if (field.hasAttribute("disabled")) {
        field.removeAttribute("disabled");
        submitBtnAdmin.classList.remove("display-none");

        deleteBtn.classList.remove("display-none");
      }
    });
  } else {
    allFields.forEach((field) => {
      field.setAttribute("disabled", "");
      submitBtnAdmin.classList.add("display-none");
      deleteBtn.classList.add("display-none");
    });
  }
});

deleteBtn.addEventListener("click", (e) => {
  displayConfirmation();
});

function deleteInfo() {
  let userDetailsLabels = document.querySelectorAll(
    ".user-details-fieldset label"
  );
  userDetailsLabels.forEach((label) => {
    if (label.innerText.toLowerCase() != "county") {
      label.nextElementSibling.value = "";
    }
  });
}

const displayConfirmation = () => {
  let response = confirm(
    "You will delete all user personal info. This cannot be undone"
  );

  if (response) {
    deleteInfo();
    postTicket(generateTicketData()).then((message) => {
      let responseMessage = Object.values(message)[0];
      displayMessage(responseMessage);
    });
  }
};
