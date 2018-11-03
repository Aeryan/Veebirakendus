// Google Map
function initMap() {
    //var tekst = "BOOKWORM, Juhan Liivi 2.";
    var liivi = {lat: 58.37824850000001, lng: 26.71467329999996};
    var map = new google.maps.Map(document.getElementById('map'), {zoom: 17, center: liivi});
    //var infowindow = new google.maps.InfoWindow({content: tekst});
    var marker = new google.maps.Marker({position: liivi, map: map});
    // marker.addListener(function() {infowindow.open(map, marker);});
}

// Lehe alla kerimisel laetakse veel üks pilt
function yHandler() {
    var wrap = document.getElementById('wrap');
    var contentHeight = wrap.offsetHeight; // Gets page content height
    var yOffset = window.pageYOffset; // Gets the vertical scroll position
    var y = yOffset + window.innerHeight;
    if (y >= contentHeight) {
        wrap.innerHTML = '<img src="https://www.incimages.com/uploaded_files/image/970x450/getty_598063032_349381.jpg" alt="Raamatud1">' +'<br>'
            + '<img src="https://cdn-images-1.medium.com/max/1024/1*YLlZ96J3p8GFkIh1USVMzg.jpeg" alt="Raamatud2">';
        // Ajax call to get more dynamic data
    }
}
window.onscroll = yHandler;