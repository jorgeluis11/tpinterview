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
}]).controller('testCandidatesTestRetrievePDFCtrl', ['$scope', '$routeParams', '$http', function ($scope, $routeParams, $http) {
    //$($(".ace_identifier")[0]).html()
    var url = ""
    $scope.data = [];

    var url = "api/candidate/answers/?candidate=" + $routeParams.candidate + "&exam=" + $routeParams.exam

    $http.get(url).then(function(data){
        $scope.data = data.data;
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
}]).directive('textAreaDirective', [function () {
      return {
        restrict: 'A',
        link: function (scope, element, attrs) {
            element.click(function(){
                $(this).height($(this).prop('scrollHeight'))
            });
        }
    }
}]);