var app = angular.module('kingApp', ['ngRoute']);
app.config(['$routeProvider', '$locationProvider',
  function($routeProvider, $locationProvider) {
    $routeProvider
      .when('/king/soldiers', {
        templateUrl: '/static/js/views/king/soldiers.html',
        controller: 'SoldiersController'
      })
      .when('/king/soldier/:id', {
        templateUrl: '/static/js/views/king/soldier_ak.html',
        controller: 'SoldiersAKController'
      })
      .when('/king/generals', {
        templateUrl: '/static/js/views/king/generals.html',
        controller: 'GeneralsController'
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

