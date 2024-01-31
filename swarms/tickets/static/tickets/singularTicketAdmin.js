let allFields = document.querySelectorAll(".form-div :not(label)");
let submitBtnAdmin = document.querySelector(".submit-description");
let checkboxAllFields = document.querySelector("#checkboxAllFields");
let deleteBtnPersonalInfo = document.querySelector(".delete-ppi-btn");
let deleteTicketBtn = document.querySelector(".delete-ticket-btn");
checkboxAllFields.addEventListener("change", (e) => {
  if (checkboxAllFields.checked) {
    allFields.forEach((field) => {
      if (field.hasAttribute("disabled")) {
        field.removeAttribute("disabled");
        submitBtnAdmin.classList.remove("display-none");

        deleteBtnPersonalInfo.classList.remove("display-none");
        deleteTicketBtn.classList.remove("display-none");
      }
    });
  } else {
    allFields.forEach((field) => {
      field.setAttribute("disabled", "");
      submitBtnAdmin.classList.add("display-none");
      deleteBtnPersonalInfo.classList.add("display-none");
      deleteTicketBtn.classList.add("display-none");
    });
  }
});

deleteBtnPersonalInfo.addEventListener("click", (e) => {
  displayConfirmationDeletePersonalInfo();
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

const displayConfirmationDeletePersonalInfo = () => {
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

deleteTicketBtn.addEventListener("click", (e) => {
  deleteTicketWithConfirmation();
});
const deleteTicket = async (link) => {
  let data = await makeRequest(link, "delete");
  return data;
};

const deleteTicketWithConfirmation = () => {
  let response = confirm("You will delete this ticket, this cannot be undone");

  if (response) {
    deleteTicket(link).then((message) => {
      let responseMessage = Object.values(message)[0];
      if (responseMessage.toLowerCase() === "delete") {
        redirect();
      }
    });
  }
};
