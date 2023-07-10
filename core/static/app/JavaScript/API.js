function iniciarMap(){
    var coord = {lat:-33.4654618 , lng:-70.6306715};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 15,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}