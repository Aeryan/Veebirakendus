// IP ja IP järgi riik Ajaxi abil
var uus = document.getElementById('uus');
$.get("https://ipinfo.io", function(response) {
    uus.innerHTML += "<p>IP: " +  response.ip + "</p><p>Riik: " + response.country + "</p>";
}, "jsonp").fail(function () {
    uus.innerHTML += "<p>IP: viga, ei õnnestunud leida!</p><p>Riik: viga, ei õnnestunud leida!</p>";
});