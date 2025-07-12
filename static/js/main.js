var updateBtns = document.getElementsByClassName("update-cart");
var store_redirect = '{% url "bun_store" %}'

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


// CART COOKIE 
function getCookieCart(name){
  var cookieArr = document.cookie.split(';')

  for(var i = 0; i < cookieArr.length; i++) {
    var cookiePair = cookieArr[i].split('=')

    if (name == cookiePair[0].trim()){
      return decodeURIComponent(cookiePair[1])
    }
  }
  return null;
}
var cart = JSON.parse(getCookieCart('cart'))

if(cart == undefined){
  cart = {}
  console.log('Cart was created')
  document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
}

console.log("cart:", cart)

// CART/STORE
for (let i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "Action:", action);
    console.log("USER:", user);

    if (user == "AnonymousUser") {
      addCookieItem()
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function addCookieItem(productId, action){
  console.log("User is not authenticated");

  if(action == 'add'){
    if(cart[productId] == undefined){
      cart[productId] = {'quantity':1}
    } else{
      cart[productId]['quantity'] += 1
    }
  }
  if (action == 'remove') {
    cart[productId]['quantity'] -= 1
    if (cart[productId]['quantity'] <= 0) {
      console.log('Remove Item')
      delete cart[productId]
    }
  }
  console.log('Cart', cart)
  document.cookie = 'cart=' + JSON.stringify(cart) + ";domain;path="
  location.reload()
}

function updateUserOrder(productId, action) {
  console.log("User is authenticated, sending data...");
  var url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ "productId": productId, "action": action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("Data:", data);
      location.reload();
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
}

// SHIPPING/CHECKOUT
if (shipping == "False") {
  document.getElementById("shipping-info").innerHTML = " ";
}

if (user != 'AnonymousUser'){
  document.getElementById('user-info').innerHTML = ''
}

if (shipping == "False" && user != "AnonymousUser") {
  // Hide the form if the user is logged and shipping is false
  document.getElementById("form-wrapper").classList.add("hidden");
  document.getElementById("payment-info").classList.remove("hidden");
}

// FORM/CHECKOUT
var form = document.getElementById("form");
form.addEventListener("submit", function (e) {
  e.preventDefault();
  console.log("Form submitted");
  document.getElementById("form-button").classList.add("hidden");
  document.getElementById("make-payment").classList.remove("hidden");
});

document.getElementById("make-payment").addEventListener("click", function (e) {
  submitFormData();
});

function submitFormData() {
  console.log("Payment button clicked");
  var userFormData = {
    "name": null,
    "email": null,
    "total": total,
  }

  var shippingInfo = {
    "address": null,
    "city": null,
    "state": null,
    "zipcode": null,
  }

  if (shipping != 'False') {
    shippingInfo.address = form.address.value
    shippingInfo.city = form.city.value
    shippingInfo.state = form.state.value
    shippingInfo.zipcode = form.zipcode.value
  }

  if (user == 'AnonymousUser') {
    userFormData.name = form.name.value
    userFormData.email = form.email.value
  }

  console.log('Shipping info:', shippingInfo)
  console.log('User info:', userFormData)

  var url = '/process_order/'
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ "form": userFormData, "shipping": shippingInfo }),
  })
  .then((response) => response.json())
  .then((data) => {
    console.log('Success:', data)
    alert('Transaction completed')

    cart = {}
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain;path="
    window.location.href = '{% url "bun_store" %}'
  })
  .catch((error) => {
    console.error('Error', error)
  })
}

