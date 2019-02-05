var DesinationDoc = angular.module('DesinationDoc', []);
  DesinationDoc.controller('DesinationDoc', function($scope, $http) {
    $scope.count = 0;
    $scope.dog = "wagwan shordy"

    $scope.myFunc = function() {

      $scope.count++;
    	var textArray = $scope.text.split(" ");
      console.log($scope.count);
      console.log($scope.text);
      console.log(textArray);


      for(i=0; i < textArray.length; i++) {
      	if (textArray[i] == "headache" || textArray[i] == "Doctor" || textArray[i] == "doctor" || textArray[i] == "pain" || textArray[i] == "nausea" || textArray[i] == "neauseaus" || textArray[i] == "hurt") {
      		$scope.reply = "Looks like you may need to see a doctor";
      		document.getElementById("NearestDoctor").innerHTML = "Here's the Doctor which is closest to you";
      	}

        if (textArray[i] == "toothache" || textArray[i] == "dentist" || textArray[i] == "Dentist"){
      		$scope.reply = "You have a toothache? Looks like you may need to see a dentist";
      		document.getElementById("NearestDentist").innerHTML = "Here's the Dentist which is closest to you";

      	}
      	if (textArray[i] == "depression" || textArray[i] == "anxiety" || textArray[i] == "sad" || textArray[i] == "overthinking" || textArray[i] == "motivation"){
      		$scope.reply = "You're not feeling well? Looks like you may need to see a Psychiatrist";
      		document.getElementById("NearestPsych").innerHTML = "Here's the Psychiatrist which is closest to you";

      	}
      	if (textArray[i] == "muscle" || textArray[i] == "sore" || textArray[i] == "muscles" || textArray[i] == "move" || textArray[i] == "back" || textArray[i] == "shoulder"){
      		$scope.reply = "Looks like you may need to see a Physiotherapist";
      		document.getElementById("NearestPhysio").innerHTML = "Here's the Physiotherapist which is closest to you";
      	}
      }

  };
    $http.get("jsonstore")
  .then(function(response) {
    $scope.data1 = response.data.result;
    console.log($scope.data1);
  });

   $http.get("jsonstore2")
  .then(function(response) {
    $scope.data2 = response.data;
    console.log($scope.data2);
  });


  });
