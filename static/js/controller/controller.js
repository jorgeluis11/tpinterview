angular.module("starter")
.controller('languageCtrl', ['$scope', '$http', function ($scope, $http) {
	$scope.languages = [];

	$http.get("/api/languages").then(function(data){
		$scope.languages = data.data;
	});



}])
.controller('examCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
	$scope.exams = [];

	$http.get("/api/languages/"+$routeParams.languageSlug).then(function(data){
		$scope.exams = data.data;
	});

}]).controller('questionCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
	$scope.questions = [];
	$scope.submitButton = false;

	$http.get("/api/languages/"+$routeParams.languageSlug+"/"+$routeParams.examSlug).then(function(data){
		$scope.questions = data.data;
		$scope.submitButton = true;
	});

}]);