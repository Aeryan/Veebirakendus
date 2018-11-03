// IP ja IP järgi riik Ajaxi abil
var uus = document.getElementById('uus');
$.get("https://ipinfo.io", function(response) {
    uus.innerHTML += "<p>Sinu IP: " +  response.ip + "</p>Sinu Riik: " + response.country + "</p>";
}, "jsonp");