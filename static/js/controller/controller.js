angular.module("starter")
.controller('languageCtrl', ['$scope', '$http', function ($scope, $http) {
	
	$scope.languages = [];
	$scope.exams = [];

	$scope.language = function(name){

	}

	console.log("SDf")

	$http.get("/languages").success(function(data){
		console.log(data[0]);
		// $scope.languages.push(data.fields);
		// console.log($scope.languages);
	});

}]);