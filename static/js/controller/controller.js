angular.module("starter")
.controller('languageCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.languages = [];

    $http.get("/api/languages").then(function(data){
        $scope.languages = data.data;
    });



}])
.controller('testCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
    $scope.tests = [];

    $http.get("/api/languages/"+$routeParams.languageSlug).then(function(data){
        $scope.tests = data.data;
    });

}]).controller('questionCtrl', ['$scope', '$routeParams', '$http', '$splash',function ($scope, $routeParams, $http, $splash) {

    $scope.questions = [];
    $scope.submitButton = false;
    $scope.name = "";

    $http.get("/api/languages/"+$routeParams.languageSlug+"/"+$routeParams.testSlug).then(function(data){
        $scope.questions = data.data;
        $scope.submitButton = true;
    });

    $scope.submit = function(){
        $splash.open({
            // title: '',
            message: "Are you sure you want to submit the test?"
        });
    }

     $scope.aceLoaded = function(_editor){
        // Editor part
        var _session = _editor.getSession();
        var _renderer = _editor.renderer;

        // Options
        _session.setUndoManager(new ace.UndoManager());
        _editor.getSession().setUseWorker(false);
        // _renderer.setShowGutter(false);

        // Events
        // _editor.on("changeSession", function(){ ... });
        // _session.on("change", function(){ ... });
      };

   
}]).controller('testListCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
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

    $http.get("api/candidate/list/?ordering=" + $routeParams.ordering).then(function(data){
        $scope.candidates = data.data;
        $scope.submitButton = true;
    });

}]).controller('testCandidatesTestRetrieveCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
    //$($(".ace_identifier")[0]).html()
    var url = ""
    $scope.data = [];

    var url = "api/candidate/answers/?candidate=" + $routeParams.candidate + "&test=" + $routeParams.test

    $http.get(url).then(function(data){
        $scope.data = data.data;
    });

    $scope.aceLoaded = function(_editor){
        // Editor part
        var _session = _editor.getSession();
        var _renderer = _editor.renderer;

        // Options
        _editor.setReadOnly(true);
        _session.setUndoManager(new ace.UndoManager());
        _editor.getSession().setUseWorker(false);
        // _renderer.setShowGutter(false);

        // Events
        // _editor.on("changeSession", function(){ ... });
        // _session.on("change", function(){ ... });
      };
}]).controller('testCandidatesTestRetrievePDFCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
    //$($(".ace_identifier")[0]).html()
    var url = ""
    $scope.data = [];

    var url = "api/candidate/answers/?candidate=" + $routeParams.candidate + "&test=" + $routeParams.test

    $http.get(url).then(function(data){
        $scope.data = data.data;
    });
}]);
