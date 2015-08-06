angular.module('starter', ['ngRoute', 'ui.ace'])
.config(function($routeProvider, $interpolateProvider) {
  $routeProvider
   .when('/language', {
    templateUrl: '/language/language_list.html',
    controller: 'languageCtrl',
    // resolve: {
    //   // I will cause a 1 second delay
    //   delay: function($q, $timeout) {
    //     var delay = $q.defer();
    //     $timeout(delay.resolve, 1000);
    //     return delay.promise;
    //   }
    // }
  })
   
  .when('/language/:languageSlug', {
    templateUrl: '/language/language_detail.html',
    controller: 'examCtrl',
  })
  .when('/language/:languageSlug/:examSlug', {
    templateUrl: '/language/language_question.html',
    controller: 'questionCtrl',
  })
  
  .otherwise({ redirectTo: '/language' });

  // configure html5 to get links working on jsfiddle
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})