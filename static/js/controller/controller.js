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

}]).controller('questionCtrl', ['$scope', '$routeParams', '$http', '$splash',function ($scope, $routeParams, $http, $splash) {

    $scope.questions = [];
    $scope.submitButton = false;

    $scope.nameInserted = false;
    $scope.name = "";

    $http.get("/api/languages/"+$routeParams.languageSlug+"/"+$routeParams.examSlug).then(function(data){
        $scope.questions = data.data;
        $scope.submitButton = true;
    });

    $scope.submit = function(){
        $splash.open({
            // title: '',
            message: "Are you sure you want to submit the test?"
        });
    }

   
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

}]).controller('testCandidatesTestRetrieveCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
    //$($(".ace_identifier")[0]).html()
    var url = ""
    $scope.data = [];

    var url = "api/candidate/answers/?candidate=" + $routeParams.candidate + "&exam=" + $routeParams.exam

    $http.get(url).then(function(data){
        $scope.data = data.data;
    });    
    console.log("SDf");

     $scope.aceLoaded = function(_editor){
        // Editor part
        var _session = _editor.getSession();
        var _renderer = _editor.renderer;

        // Options
        _editor.setReadOnly(true);
        _session.setUndoManager(new ace.UndoManager());
        // _renderer.setShowGutter(false);

        // Events
        // _editor.on("changeSession", function(){ ... });
        // _session.on("change", function(){ ... });
      };
}]);
