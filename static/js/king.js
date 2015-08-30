var app = angular.module('kingApp', ['ngRoute']);
app.config(['$routeProvider', '$locationProvider',
  function($routeProvider, $locationProvider) {
    $routeProvider
      .when('/king/soldiers', {
        templateUrl: '/static/js/views/king/soldier.html',
        controller: 'SoldiersController'
      })
      .when('/king', {
        templateUrl: '/static/js/views/king/welcome.html',
        controller: 'HomeController'
      })
      .when('/king/about_us', {
        templateUrl: '/static/js/views/king/about_us.html',
        controller: 'AboutController'
      })
      .otherwise({
        redirectTo: '/king'
      });

      $locationProvider.html5Mode(true);
  }]);

