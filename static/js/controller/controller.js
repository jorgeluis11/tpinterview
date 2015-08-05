angular.module("starter")
.controller('languageCtrl', ['$scope', '$http', function ($scope, $http) {
	console.log("otra");
	$scope.languages = [];
	$scope.exams = "sdfdsfds";
	$scope.test = "sdf";
	$scope.language = function(name){
	 console.log("SDf");
	 $scope.test = "sdfsdfdsfdsffsdfsdfds";
	}


	$http.get("/api/languages").then(function(data){
		$scope.languages = data.data;
		console.log($scope.languages);
		$scope.test = "testing worksss";
	});



}])
.controller('examCtrl', ['$scope', '$routeParams', function ($scope, $routeParams) {
	console.log($routeParams);
}]);