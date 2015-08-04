angular.module("starter")
.controller('testCtrl', ['$scope', '$http', function ($scope, $http) {
	
	$scope.languages = [];
	$scope.exams = "sdfdsfds";
	$scope.test = "sdf";
	$scope.language = function(name){
	 console.log("SDf");
	 $scope.test = "sdfsdfdsfdsffsdfsdfds";
	}


	$http.get("/languages").then(function(data){
		$scope.languages = data.data;
		console.log($scope.languages);
		$scope.test = "testing worksss";
	});

}]);