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

}])



.directive('ngEnter', function () {
    return {
        restrict:"A",
        link:function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    if (scope.nameText.trim()) 
                    {
                        $(".write-name-group").removeClass("animated").fadeOut(600,function(){
                            scope.nameInserted = true;
                            $(".exam-container").addClass("animated fadeInUpBig");                          
                        });
                    }
                });
                event.preventDefault();
            }
        });
    }
}
}).directive('submit', ['$http', function ($http) {
    return {
        restrict:"A",
        link:function (scope, element, attrs) {
        element.bind("click", function (event) {
            var aceCount = $("[ui-ace]");
            var aceText = aceCount.find(".ace_identifier");
             if (aceCount.length === aceText.length) {
                var text = [];
                aceText.each(function(i){
                    text.push($(aceText[i]).html());
                })
                // $http.post("/insert", {'answers[]': text}, function(data){
                //     console.log(data);
                // });
            };
        });
    }
}
}]);