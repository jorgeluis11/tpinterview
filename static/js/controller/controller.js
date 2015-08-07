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

	$scope.nameInserted = true;
	$scope.name = "";

	$http.get("/api/languages/"+$routeParams.languageSlug+"/"+$routeParams.examSlug).then(function(data){
		$scope.questions = data.data;
		$scope.submitButton = true;
	});

}])
.directive('ngEnter', function () {
    return {
    	restrict:"A",
    	link:function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
        	console.log(element);
            if(event.which === 13) {
                scope.$apply(function (){
                	if (scope.nameText.trim()) 
                	{
                		$(".write-name-group").removeClass("animated").fadeOut(500,function(){
                			scope.nameInserted = true;
                			$(".exam-container").show().addClass("animated fadeInUp");                			
                		});
                	}
                });
                event.preventDefault();
            }
        });
    }
}
});