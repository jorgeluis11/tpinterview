angular.module('starter', ['ngRoute', 'ui.ace', 'angularSpinners', 'ui.splash'])
.config(function($routeProvider, $interpolateProvider, $httpProvider) {
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
  .when('/test/', {
    templateUrl: '/test/test_list.html',
    controller: 'testCtrl',
  })
  .when('/test/candidates/', {
    templateUrl: '/test/test_candidates_list.html',
    controller: 'testCandidatesCtrl',
  })

  .otherwise({ redirectTo: '/language' });

  // configure html5 to get links working on jsfiddle
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');


  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

});