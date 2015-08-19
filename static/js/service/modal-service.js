angular.module('ui.splash', ['ui.bootstrap'])
.service('$splash', [
  '$modal',
  '$rootScope',
  function($modal, $rootScope) {
    return {
      open: function (attrs, opts) {
        // Create a new scope so we can pass custom
        // variables into the splash modal
        var scope = $rootScope.$new();
        angular.extend(scope, attrs);
        opts = angular.extend(opts || {}, {
          backdrop: false,
          scope: scope,
          templateUrl: 'splash/content.html',
          windowTemplateUrl: 'splash/index.html'
        });
        return $modal.open(opts);
      }
    };
  }
]).service('$splashCongrats', [
  '$modal',
  '$rootScope',
  function($modal, $rootScope) {
    return {
      open: function (attrs, opts) {
        // Create a new scope so we can pass custom
        // variables into the splash modal
        var scope = $rootScope.$new();
        angular.extend(scope, attrs);
        opts = angular.extend(opts || {}, {
          backdrop: false,
          scope: scope,
          templateUrl: 'splash/content-congrats.html',
          windowTemplateUrl: 'splash/index-congrats.html'
        });
        return $modal.open(opts);
      }
    };
  }
]).run([
  '$templateCache',
  function ($templateCache) {
    $templateCache.put('splash/index.html',
      '<section class="splash" ng-class="{\'splash-open\': animate}" ng-style="{\'z-index\': 1000, display: \'block\'}" ng-click="close($event)">' +
      '  <div class="splash-inner" ng-transclude></div>' +
      '</section>'
    );
   $templateCache.put('splash/content.html',
      '<div class="splash-content text-center">' +
      '  <h1><i class="fa fa-hand-paper-o"></i></h1>' +
      '  <p class="lead" ng-bind="message"></p>' +
      '  <div class="btn btn-lg btn-success outline" submit ng-click="$close()"><i class="fa fa-check"></i> Submit</div>' +
      '  <div class="btn btn-lg btn-warning outline" ng-click="$close()"><i class="fa fa-ban"></i> Cancel</div>' +
      '</div>'
    );
    $templateCache.put('splash/index-congrats.html',
      '<section class="splash" ng-class="{\'splash-open\': animate}" ng-style="{\'z-index\': 1000, display: \'block\'}" ng-click="close($event)">' +
      '  <div class="splash-inner" ng-transclude></div>' +
      '</section>'
    );
   $templateCache.put('splash/content-congrats.html',
      '<div class="splash-content text-center">' +
      '  <h1><i class="fa fa-thumbs-o-up"></i></h1>' +
      '  <p class="lead" ng-bind="message"></p>' +
      '  <div class="btn btn-lg btn-primary outline" ng-click="$close();" finish>Done</div>' +
      '</div>'
    );
  }
]);