  $(document).ready(function () {
    $("#loaderDiv").hide();
        // Reaction of the application after a click of the user on the "S'il te plaît GrandPy" button.
        $("#button-granpy").click(function (event) {

          // Repeating the user input in the dialog box.
          var userEntry = 'Vous : ' + $("#userRequest").val();
          // Creating a "div" element and assigning a "userQuestion" class.
          var div = document.createElement('div');
          div.setAttribute("class", "userQuestion");
          // Adding the question to the following dialog box.
          div.append(userEntry);
          $(".answer").append(div);

            // Send the request of the user with Ajax.
            $.ajax({
                url: "/userRequest",
                type: "POST",
                dataType: "json",
                data: {userRequest: userEntry },
                beforeSend: function() {
                  //$("#loaderDiv").show();
                  $(".answer").append($("#loaderDiv").show());
                  $(".answer").scrollTop($(".answer")[0].scrollHeight);
                },
                success: function (userRequest) {
                  $("#loaderDiv").hide();

                  // Retrieving the user's request after analysis.
                  // Convert the returned object to JSON.
                  var analysisUserRequest = JSON.stringify(userRequest);
                  // JSON Analysis.
                  analysisUserRequest = JSON.parse(analysisUserRequest);
                  // Retrieving the "coordinate" part of the JSON file.
                  coord = analysisUserRequest.coordinate
                  
                  // Initialization of the GoogleMap with setting the coordinates of the request.
                  initMap(coord);
                  
                  // Retrieving the "description" part of the JSON file.
                  descript = analysisUserRequest.description
                  // Added the answer of grandPy-Bot.                  
                  var userRequest = "GrandPy : " + descript;
                  // Creating a "div" element and assigning a "grandPyAnswer" class.                  
                  var div = document.createElement('div');
                  div.setAttribute("class", "grandPyAnswer");
        /*div.focus();*/
                  // Adding the answer to the following dialog box.
                  div.append(userRequest);
                  $(".answer").append(div);
                  // Method .scrollTop() makes it possible to keep the last exchanges visible in the dialog box.
                  $(".answer").scrollTop($(".answer")[0].scrollHeight);

                  

                }

            });
        });
    });

    //Definition of the initMap function of GoogleMap.
    function initMap(coord) {
      var uluru = {'lat': coord.lat, 'lng': coord.lng};
      var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: uluru
      });
      var marker = new google.maps.Marker({
        position: uluru,
        map: map
      });
    };
