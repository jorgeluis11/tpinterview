angular.module("starter")
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
}).directive('submit', ['$http','spinnerService', function ($http, spinnerService) {
    return {
        restrict:"A",
        link:function (scope, element, attrs) {
        
        
        element.bind("click", function (event) {

            var aceCount = $("[ui-ace]");
            var aceText = aceCount.find(".ace_text-layer");
             if (aceCount.length === aceText.length) {
                spinnerService.show('postSpinner');
                var text = [];

                $http({
                   method: 'POST',
                   url: '/api/candidate/insert/',
                   data: {"exam": attrs.id ,"name": scope.nameText},
                    headers: {
                        'Content-Type': 'application/json'
               }}).success(function(data){

                 aceCount.each(function(i){
                    // text.push($(aceText[i]).html());
                        var aceElem = $(aceCount[i]);
                        var text = ace.edit(aceCount[i]).getValue()
                        $http({
                       method: 'POST',
                       url: '/api/answer/insert/',
                       data: {answer: text ,order: parseInt(aceElem.data("order")),
                              question: aceElem.data("id"), candidate: data.id},
                        headers: {
                            'Content-Type': 'application/json'
                       }}).success(function(data2){
                        setTimeout(
                        function() 
                        {
                            spinnerService.hide('postSpinner');
                        }, 250);
                       })
                    });
               })
            };
        });
    }
}
}]);