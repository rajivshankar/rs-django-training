//site_static/js/location.js
function show_best_images(){
    $('img.image-full-width').each(function() {
        var $img = $(this);
        if ($img.width() > 800) {
            $img.attr('src', $img.data('large-src'));
        } else if ($img.width() > 400) {
            $img.attr('src', $img.data('medium-src'));
        } else {
            $img.attr('src', $img.data('small-src'));
        }
    });
}

function show_map() {
    var $map = $('#map');
    var latitude = parseFloat($map.data('latitude'));
    var longitude = parseFloat($map.data('longitude'));
    //var latlng = new google.maps.LatLng(latitude, longitude);
    var latlng = {lat: latitude, lng: longitude};
    
    var map = new google.maps.Map($map.get(0), {
        center: latlng,
        zoom: 15
    });
/*
    var map = new google.maps.Map($map.get(0), {
        zoom: 15,
        center: latlng
    });
*/  
    var marker = new google.maps.Marker({
        position: latlng,
        map: map
    });
}

$(document).ready(function() {
    show_best_images();
    show_map();
})

$(window).on('resize', show_best_images);
