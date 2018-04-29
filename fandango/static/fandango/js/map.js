function initMap() {
        var uluru = {lat: 35.9940, lng: -78.8986};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 11,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
        var stadium = {lat:36.0192, lng:-78.9078};
        var classic = {lat:35.9594, lng:-78.9572};
        var amc = {lat:35.9051, lng:-78.9457};
        var silver = {lat:35.913200, lng:-79.055847};
        var regal = {lat:35.9042, lng:-78.7842};
        var tim = {lat:35.9620, lng:-79.0557};
        var frank = {lat:35.8489, lng:-78.8890};
        var carolina = {lat:35.9978, lng:-78.9027};
        var chelsea = {lat:35.9978, lng:-78.9027};
        var varsity = {lat:35.913200, lng:-79.055847};


        var label = "";
        var popUp = new google.maps.InfoWindow({
          content: label
        });
        var marker = new google.maps.Marker({
          position: stadium,
          map: map
        });
        marker.addListener('click', function(){
          popUp.open(map, marker);
        });

        var label2 = "";
        var popUp2 = new google.maps.InfoWindow({
          content: label2
        });
        var marker2 = new google.maps.Marker({
          position: classic,
          map: map
        });
        marker2.addListener('click', function(){
          popUp2.open(map, marker2);
        });

        var label3 = "";
        var popUp3 = new google.maps.InfoWindow({
          content: label3
        });
        var marker3 = new google.maps.Marker({
          position: amc,
          map: map
        });
        marker3.addListener('click', function(){
          popUp3.open(map, marker3);
        });

        var label4 = "";
        var popUp4 = new google.maps.InfoWindow({
          content: label4
        });
        var marker4 = new google.maps.Marker({
          position: silver,
          map: map
        });
        marker4.addListener('click', function(){
          popUp4.open(map, marker4);
        });

        var label5 = "";
        var popUp5 = new google.maps.InfoWindow({
          content: label5
        });
        var marker5 = new google.maps.Marker({
          position: regal,
          map: map
        });
        marker5.addListener('click', function(){
          popUp5.open(map, marker5);
        });

        var label6 = "";
        var popUp6 = new google.maps.InfoWindow({
          content: label6
        });
        var marker6 = new google.maps.Marker({
          position: tim,
          map: map
        });
        marker6.addListener('click', function(){
          popUp6.open(map, marker6);
        });

        var label7 = "";
        var popUp7 = new google.maps.InfoWindow({
          content: label7
        });
        var marker7 = new google.maps.Marker({
          position: frank,
          map: map
        });
        marker7.addListener('click', function(){
          popUp7.open(map, marker7);
        });

        var label8 = "";
        var popUp8 = new google.maps.InfoWindow({
          content: label8
        });
        var marker8 = new google.maps.Marker({
          position: carolina,
          map: map
        });
        marker8.addListener('click', function(){
          popUp8.open(map, marker8);
        });

        var label9 = "";
        var popUp9 = new google.maps.InfoWindow({
          content: label9
        });
        var marker9 = new google.maps.Marker({
          position: chelsea,
          map: map
        });
        marker9.addListener('click', function(){
          popUp9.open(map, marker9);
        });

        var label10 = "";
        var popUp10 = new google.maps.InfoWindow({
          content: label10
        });
        var marker10 = new google.maps.Marker({
          position: varisty,
          map: map
        });
      }
