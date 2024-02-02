const dialog = document.querySelector("dialog");
const showButton = document.querySelector("dialog + button");
const closeButton = document.querySelector("dialog button");
const link = window.location.href;
showButton.addEventListener("click", () => {
  dialog.showModal();
});

closeButton.addEventListener("click", () => {
  dialog.close();
});

let ticketStatus = document.querySelector("#status");
let assigneeBox = document.querySelector("#assignee");
let editLabel = document.querySelector(".edit-label");
let editCheckbox = document.querySelector("#edit");
let submitBtn = document.querySelector(".submit-description");
let descriptionBox = document.querySelector("#description");
let allInputs = document.querySelectorAll(".form-div  > input");
let allSelects = document.querySelectorAll(".form-div select");
let allTextAreas = document.querySelectorAll(".form-div textarea");
if (ticketStatus.value === "Open") {
  editCheckbox.classList.remove("display-none");
  editLabel.classList.remove("display-none");
  editCheckbox.addEventListener("click", (e) => {
    if (editCheckbox.checked) {
      descriptionBox.removeAttribute("disabled");
      ticketStatus.removeAttribute("disabled");
      assigneeBox.removeAttribute("disabled");
    } else {
      descriptionBox.setAttribute("disabled", "");
      ticketStatus.setAttribute("disabled", "");
      assigneeBox.setAttribute("disabled", "");
    }
    submitBtn.classList.toggle("display-none");
  });
}

let saveBtnDescription = document.querySelector(".submit-description");
saveBtnDescription.addEventListener("click", (e) => {
  postTicket(generateTicketData()).then((message) => {
    let responseMessage = Object.values(message)[0];
    displayMessage(responseMessage);
  });
});

const getTicket = async (link) => {
  let data = await makeRequest(link, "get");

  return data;
};

async function makeRequest(url, requestType, body) {
  let headersObj = {
    "X-Requested-With": "XMLHttpRequest",
    "Content-type": "application/json",
  };
  if (requestType.toLowerCase() != "get") {
    // != get covers post and delete requests
    let csrfValue = document.querySelector("[name=csrfmiddlewaretoken").value;
    headersObj["X-CSRFToken"] = csrfValue;
  }
  let response = await fetch(url, {
    method: requestType,
    headers: headersObj,
    body: body,
  });
  let data = await response.json();

  return data;
}

const postTicket = async (ticketBodyObject) => {
  let data = await makeRequest(link, "post", (body = ticketBodyObject));
  return data;
};

function generateTicketData() {
  let ticketbody = new Object();
  let allLabels = document.querySelectorAll("label");
  allLabels.forEach((element) => {
    if (element.className != "edit-label") {
      let labelValue = element.getAttribute("for");
      let value = element.nextElementSibling.value;
      if (labelValue === "image") {
        let img = document.querySelector(".image-preview");
        ticketbody[labelValue] = img.getAttribute("src");
      } else {
        ticketbody[labelValue] = value;
      }
    }
  });

  let bodyJson = JSON.stringify({ ticket: ticketbody });
  return bodyJson;
}

function displayMessage(responseMessage) {
  let newDiv = document.createElement("div");
  let contentWrapper = document.querySelector(".content-wrapper");
  if (responseMessage === "saved") {
    // if ticket has been saved

    newDiv.className = "message";
    newDiv.innerHTML = `    <p class="valid">Your ticket has been successfully saved</p>`;
    contentWrapper.appendChild(newDiv);

    setTimeout(() => {
      newDiv.remove();
    }, 1500);
  } else {
    newDiv.className = "message";
    newDiv.innerHTML = `<p class="invalid">Your ticket has not been saved</p>`;

    contentWrapper.appendChild(newDiv);
    setTimeout(() => {
      newDiv.remove();
    }, 1500);
  }
}
