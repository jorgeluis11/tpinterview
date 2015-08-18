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
    //$($(".ace_identifier")[0]).html()

    $scope.questions = [];
    $scope.submitButton = false;

    $scope.nameInserted = false;
    $scope.name = "";

    $http.get("/api/languages/"+$routeParams.languageSlug+"/"+$routeParams.examSlug).then(function(data){
        $scope.questions = data.data;
        $scope.submitButton = true;
    });



}]).controller('testCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
    //$($(".ace_identifier")[0]).html()

    $scope.tests = [];
    $scope.submitButton = false;

    $scope.nameInserted = false;
    $scope.name = "";

    $http.get("/api/test/").then(function(data){
        $scope.tests = data.data;
        $scope.submitButton = true;
    });

}]).controller('testCandidatesCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
    //$($(".ace_identifier")[0]).html()

    $scope.candidates = [];
    $scope.submitButton = false;

    $scope.nameInserted = false;
    $scope.name = "";

    $http.get("api/candidate/list/").then(function(data){
        $scope.candidates = data.data;
        $scope.submitButton = true;
    });

}]);