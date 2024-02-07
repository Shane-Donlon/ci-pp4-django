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

window.addEventListener("DOMContentLoaded", (e) => {
  if (document.body.contains(document.querySelector("table"))) {
    let table = document.querySelector("table");
    if (!table.children[1].children.length) {
      // if table does not have children remove the element and replace with h2
      table.remove();
      let main = document.querySelector("main");
      let h2 = document.createElement("h2");
      h2.innerText = "There are no tickets to show";
      h2.className = "no-tickets-h2";
      main.append(h2);
    }
  }

  if (document.body.contains(document.querySelector("#id_assignee"))) {
    // due to field loading for admins only for now adding if statement to not break file
    let assigneeField = document.querySelector("#id_assignee");

    /**
On page load if the first field in the assignee is selected show "------"
else (ie the filter has been used) show "clear filter"
   */
    if (!assigneeField.children[0].hasAttribute("selected")) {
      assigneeField.children[0].innerText = "Clear Filter";
    }
  }
});
