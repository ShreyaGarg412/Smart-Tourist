function login() {
  fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      email: document.getElementById("email").value,
      password: document.getElementById("password").value
    })
  })
  .then(res => res.json())
  .then(data => {
    alert(data.message);
    if (data.message === "Login Success") {
      window.location.href = "dashboard.html";
    }
  });
}

function getPlaces() {
  let city = document.getElementById("city").value;
  fetch(`http://127.0.0.1:5000/places?city=${city}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerHTML =
        data.places.map(p => `<p>${p}</p>`).join("");
    });
}

function getWeather() {
  fetch("http://127.0.0.1:5000/weather")
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerHTML =
        `Temp: ${data.temp} <br> Condition: ${data.condition}`;
    });
}

function getBudget() {
  let amount = document.getElementById("budget").value;
  fetch(`http://127.0.0.1:5000/budget?amount=${amount}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerHTML = data.plan;
    });
}

