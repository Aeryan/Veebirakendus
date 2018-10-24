var login = document.getElementById('login');
var signup = document.getElementById('signup');

window.onclick = function (event) {
    if (event.target == login) {
        login.style.display = "none";
    }
    if (event.target == signup) {
        signup.style.display = "none";
    }
};

document.addEventListener("DOMContentLoaded", function () {
    var elements = document.getElementsByClassName('loginfield');
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function (e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                e.target.setCustomValidity("Palun täida see lünk.");
            }
        };
        elements[i].oninput = function (e) {
            e.target.setCustomValidity("");
        }
    }
});

document.addEventListener("DOMContentLoaded", function () {
    var elements = document.getElementsByClassName('signupfield');
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function (e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                e.target.setCustomValidity("Palun täida see lünk.");
            }
        };
        elements[i].oninput = function (e) {
            e.target.setCustomValidity("");
        }
    }
});

document.addEventListener("DOMContentLoaded", function () {
    var elements = document.getElementsByClassName('searchfield');
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function (e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                e.target.setCustomValidity("Palun täida see lünk.");
            }
        };
        elements[i].oninput = function (e) {
            e.target.setCustomValidity("");
        }
    }
});

signupButton.onclick = function (event) {
    var a = document.getElementsByTagName("INPUT");
    for (var i = 0; i < a.length; i++) {
        if (a[i].value.length == 0) {
            return;
        }
    }
    signup.style.display = "none";
};

function initMap() {
    //var tekst = "BOOKWORM, Juhan Liivi 2.";
    var liivi = {lat: 58.37824850000001, lng: 26.71467329999996};
    var map = new google.maps.Map(document.getElementById('map'), {zoom: 17, center: liivi});
    //var infowindow = new google.maps.InfoWindow({content: tekst});
    var marker = new google.maps.Marker({position: liivi, map: map});
    // marker.addListener(function() {infowindow.open(map, marker);});
};
