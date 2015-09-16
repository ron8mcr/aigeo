$(document).ready(function() {
	var map = L.map('map');
	var marker = L.marker();
	var popup = L.popup();

	var initMap = function() {
		map.setView([56.000, 92.8657339], 12);
		L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
			attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
			maxZoom: 18,
			id: 'ron8mcr.ciem8kzr10005txm1h3ctcgxu',
			accessToken: 'pk.eyJ1Ijoicm9uOG1jciIsImEiOiJjaWVtOGwxd2owMDA0c2draXpmYzB4ZXVlIn0.QN8OXtwX2KdDS6PPebyYSA'
		}).addTo(map);
		map.locate({'setView': true, 'maxZoom': 15});
	};

	var processResponse = function(response){
		if (response.is_success == false) {
			$("#in_progress").fadeOut(function(){ $("#error_msg").fadeIn(); });
			return;
		}
		$("#in_progress").fadeOut('fast');
		var html = '<b>' + response.service + '</b><br>' + response.address
		map.panTo(response.latlng);
		marker.setLatLng(response.latlng)
		      .addTo(map)
		      .bindPopup(html)
		      .openPopup();
	};

	var init = (function(){
		initMap();

		$("#search_form").submit(function (event) {
			event.preventDefault();
			var $form = $(this);
			var postData = $form.serialize();
			var formURL = $form.attr('action');

			var ajax = {url: formURL , type: 'POST', data: postData, dataType: "json"};
			$("#error_msg").fadeOut(function(){
				$("#in_progress").fadeIn('fast');
				$.ajax(ajax).then(processResponse);																																																														
			});
		});
	});

	init();
});
																																																			