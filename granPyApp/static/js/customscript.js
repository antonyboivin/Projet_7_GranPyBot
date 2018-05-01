  $(document).ready(function () {
        $("#button-granpy").click(function (event) {
          var userEntry = 'Vous : ' + $("#userRequest").val();

          var div = document.createElement('div');
          div.style.border = "5px outset green"
          div.style.marginBottom = "10px";
          div.style.fontSize = "large";

          div.append(userEntry);
          $(".answer").append(div);

            $.ajax({
                url: "/userRequest",
                type: "POST",
                dataType: "json",
                data: {userRequest: userEntry },
                success: function (userRequest) {

                  var div = document.createElement('div');
                  var userRequest = "GrandPy : " + userRequest;
                  div.style.color = 'yellow';
                  div.style.textAlign = 'right';
                  div.style.border = "5px outset white";
                  div.style.marginBottom = "10px";
                  div.style.fontSize = "large";
                  div.focus();

                  div.append(userRequest);
                  $(".answer").append(div);

                  $(".answer").scrollTop($(".answer")[0].scrollHeight);


                }

            });
        });
    });


    function initMap() {
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: {lat: -34.397, lng: 150.644}
      });
      var geocoder = new google.maps.Geocoder();

      document.getElementById('submit').addEventListener('click', function() {
        geocodeAddress(geocoder, map);
      });
    }

    function geocodeAddress(geocoder, resultsMap) {
      var address = document.getElementById('address').value;
      geocoder.geocode({'address': address}, function(results, status) {
        if (status === 'OK') {
          resultsMap.setCenter(results[0].geometry.location);
          var marker = new google.maps.Marker({
            map: resultsMap,
            position: results[0].geometry.location
          });
        } else {
          alert('Geocode was not successful for the following reason: ' + status);
        }
      });
    }

