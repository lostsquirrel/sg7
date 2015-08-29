var app = angular.module('CalendarApp', ['ngRoute']);

app.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider
    .when('/', {
        controller: 'CalendarDayController',
        templateUrl: 'js/views/calendar_day.html'
    })
    .when('/:id', {
        controller: 'EventController',
        templateUrl: 'js/views/calendar_event.html'
    })
    .otherwise({
        redirectTo: '/'
    });
  }]);