angular.module('starter', ['ngRoute'])
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
  .when('/language/:languageId', {
    templateUrl: '/language/language_list.html',
    controller: 'examCtrl',
  })
  .otherwise({ redirectTo: '/language' });

  // configure html5 to get links working on jsfiddle
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
})