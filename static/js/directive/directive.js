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
}).directive('submit', ['$http','spinnerService','$splashCongrats', function ($http, spinnerService, $splashCongrats) {
    return {
        restrict:"A",
        link:function (scope, element, attrs) {
        element.bind("click", function (event) {
            var aceCount = $("[ui-ace]");
            var aceText = aceCount.find(".ace_text-layer");
             if (aceCount.length === aceText.length) {
                var text = [];

                var that = this;
                // var empty = false;

                // aceCount.each(function(i){
                //   var text = ace.edit(aceCount[i]).getValue();
                  // if (!text)
                  //   {
                  //     empty = true;
                  //     return;
                  //   }
                // });

                // if (empty) 
                //   return;
                spinnerService.show('postSpinner');
                $http({
                   method: 'POST',
                   url: '/api/candidate/insert/',
                   data: {exam: parseInt($("#submit-answers").data("test")) , name: $("#submit-answers").data("name")},
                   async:false,
                    headers: {
                        'Content-Type': 'application/json'
               }}).success(function(data){
                var counter = 0;

                 aceCount.each(function(i){
                    // text.push($(aceText[i]).html());
                        var aceElem = $(aceCount[i]);
                        var text = ace.edit(aceCount[i]).getValue()
                        $http({
                       method: 'POST',
                       url: '/api/answer/insert/',
                       async:false,
                       data: {answer: text ,order: parseInt(aceElem.data("order")),
                              question: aceElem.data("id"), candidate: data.id},
                        headers: {
                            'Content-Type': 'application/json'
                       }}).success(function(data2){
                        counter++;
                        if(aceCount.length === counter){
                          spinnerService.hide('postSpinner');
                            $splashCongrats.open({
                              // title: '',
                              message: "Thanks for your time!"
                            });
                        }
                       })
                    });
               })
            };
        });
    }
}
}]).directive('finish', ['$location', function ($location) {
  return {
    restrict: 'A',
    link: function (scope, element, attrs) {
      element.bind('click', function(event) {
        $location.path("/language");

      });

    }
  };
}]);