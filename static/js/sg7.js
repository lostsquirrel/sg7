var app = angular.module('sg7', ['ngRoute', 'controllers']);
app.config(['$routeProvider', '$locationProvider',
  function($routeProvider, $locationProvider) {
    $routeProvider.
      when('/cities', {
        templateUrl: '/static/pages/cities.html',
        controller: 'cityCtrl'
      }).
      when('/items', {
        templateUrl: '/static/pages/items.html',
        controller: 'itemCtrl'
      }).
      when('/map', {
        templateUrl: '/static/pages/map.html',
        controller: 'mapCtrl'
      }).
      when('/about_us', {
        templateUrl: '/static/pages/about_us.html',
        controller: 'aboutUsCtrl'
      }).
      when('/', {
        templateUrl: '/static/pages/welcome.html',
        controller: 'baseCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });

      $locationProvider.html5Mode(true);
  }]);

app.directive('pagination', function() {
  return {
    restrict: 'E',
    templateUrl: '/static/pages/pagination.html'
  };
});