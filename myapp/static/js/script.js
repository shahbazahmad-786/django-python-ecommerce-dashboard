/* -------- Sidebar -------- */
let open = document.getElementById("open");
let close = document.getElementById("close");
let aside = document.getElementById("aside");

open.addEventListener("click", () => {
  open.style.display = "none";
  close.style.display = "block";
  aside.style.display = "block";
});

close.addEventListener("click", () => {
  open.style.display = "block";
  close.style.display = "none";
  aside.style.display = "none";
});

/* -------- Dropdown -------- */
let dropdown = document.getElementById("dropdown");
let list = document.getElementById("list");

dropdown.addEventListener("click", () => {
  list.classList.toggle("list");
});

/* -------- Form Validation -------- */
function companyForm() {
  let name = document.forms["company"]["name"].value;
  let contact = document.forms["company"]["contact"].value;
  let address = document.forms["company"]["address"].value;
  if (name == "") {
    alert("Name must be filled out");
    return false;
  } else if (contact == "") {
    alert("Contact must be filled out");
    return false;
  } else if (address == "") {
    alert("Address must be filled out");
    return false;
  } else if (isNaN(contact)) {
    alert("Please enter Numeric value in Contact No");
    return false;
  }
}

function productForm() {
  let name = document.forms["product"]["name"].value;
  let details = document.forms["product"]["details"].value;
  if (name == "") {
    alert("Name must be filled out");
    return false;
  } else if (details == "") {
    alert("Details must be filled out");
    return false;
  }
}

function categoryForm() {
  let name = document.forms["category"]["name"].value;
  if (name == "") {
    alert("Name must be filled out");
    return false;
  }
}

function distributorForm() {
  let name = document.forms["distributor"]["name"].value;
  let contact = document.forms["distributor"]["contact"].value;
  let email = document.forms["distributor"]["email"].value;
  if (name == "" || !isNaN(name)) {
    if (name == "") {
      alert("Name must be filled out");
      return false;
    } else if (!isNaN(name)) {
      alert("Please enter String value in Name field");
      return false;
    }
  } else if (contact == "") {
    alert("Contact must be filled out");
    return false;
  } else if (email == "") {
    alert("Email must be filled out");
    return false;
  } else if (isNaN(contact)) {
    alert("Please enter Numeric value in Contact No");
    return false;
  }
}
