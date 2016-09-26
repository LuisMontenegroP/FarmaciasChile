$(function(){

	if(navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(getCoords, getError);
	} else {
		initialize(13.30272, -87.194107);
	}

	function getCoords(position) {

		var lat = position.coords.latitude;
		var lng = position.coords.longitude;

		initialize(lat, lng);
	}

	function getError(err) {

		initialize(13.30272, -87.194107);
	}

	function initialize(lat, lng) {

		var latlng = new google.maps.LatLng(lat, lng);
		var mapSettings = {
			center : latlng,
			zoom : 15,
			mapTypeId : google.maps.MapTypeId.ROADMAP
		}

		map = new google.maps.Map($('#mapa').get(0), mapSettings);

		var marker = new google.maps.Marker({
			position : latlng,
			map : map,
			draggable : true,
			title : 'Arrastrame!',
		});

		var image = 'https://cdn1.iconfinder.com/data/icons/medicine-20/48/Hospital-32.png';

		var farmacia = new google.maps.Marker({
			position: {lat: -33.58093611478459, lng: -71.61264272236116},
			map : map,
			icon : image,
			title: 'FARMACIAS CRUZ VERDE'

		});

		var farmacia_2 = new google.maps.Marker({
			position: {lat: -33.58519061711135, lng: -71.60710664295442},
			map : map,
			icon : image,
		});

		var contentString = '<div id="content">'+
            							'<div id="siteNotice">'+
            							'</div>'+
	            						'<h1 id="firstHeading" class="firstHeading">FARMACIAS CRUZ VERDE</h1>'+
	            						'<div id="bodyContent">'+
	            							'<p style="text-align: justify;"><b>FARMACIAS CRUZ VERDE</b>, also referred to as <b>Ayers Rock</b>, is a large ' +
	            									'sandstone rock formation in the southern part of the '+
										            'Northern Territory, central Australia. It lies 335&#160;km (208&#160;mi) '+
										            'south west of the nearest large town, Alice Springs; 450&#160;km '+
										            '(280&#160;mi) by road. Kata Tjuta and Uluru are the two major '+
										            'features of the Uluru - Kata Tjuta National Park. Uluru is '+
										            'sacred to the Pitjantjatjara and Yankunytjatjara, the '+
										            'Aboriginal people of the area. It has many springs, waterholes, '+
										            'rock caves and ancient paintings. Uluru is listed as a World '+
										            'Heritage Site.'+
														'+</p>'+
							            '</div>'+
						            '</div>';

    var infowindow = new google.maps.InfoWindow({
      content: contentString,
			maxWidth: 220
    });

    farmacia.addListener('click', function() {
      infowindow.open(map, farmacia);
    });

		/*function loadMarkers(){
			{% for punto in farmacias %}
				var point = new google.maps.LatLng({{punto.lat}},{{punto.lng}});
						var marker = new google.maps.Marker({
							position: point,
							map: map
						});
			{% endfor %}
		}

		loadMarkers();*/
	}
});
