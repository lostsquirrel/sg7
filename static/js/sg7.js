var app = angular.module('sg7', ['ngRoute', 'controllers']);
app.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/cities', {
        templateUrl: '/static/pages/cities.html',
        controller: 'cityCtrl'
      }).
      when('/items', {
        templateUrl: '/static/pages/items.html',
        controller: 'itemCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);

app.directive('pagination', function() {
  return {
    restrict: 'E',
    template: '/static/pages/pagination.html'
  };
});