var app = angular.module('controllerApp', []);

 app.controller('FirstContr',  function($scope, $window) {
   $scope.testFunc = function() {
     $window.alert("Service not provided yet");
   }
 }); 
