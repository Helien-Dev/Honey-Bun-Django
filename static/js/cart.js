var updateBtns = document.getElementsByClassName("update-cart");

// CSRFTOKEN
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

// CART 
for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "Action:", action);
    console.log("USER:", user);

    if (user == "AnonymousUser") {
      console.log("User is not authenticated");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("User is authenticated, sending data...");
  var url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      'X-CSRFToken':csrftoken,
    },
    body: JSON.stringify({ "productId": productId, "action": action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("Data:", data);
      location.reload()
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
}

// SHIPPING
if (shipping == 'False'){
  document.getElementById('shipping-info').innerHTML = ''
}

// FORM
var form = document.getElementById('form')
form.addEventListener('submit', function(e) {
  e.preventDefault()
  console.log('Form submitted')
  document.getElementById('form-button').classList.add('hidden')
  document.getElementById('form-button').classList.remove('hidden')
})
