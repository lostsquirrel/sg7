var app = angular.module('CalendarApp', ['ngRoute']);

app.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider
    .when('/', {
        controller: 'CalendarDayController',
        templateUrl: '/static/js/views/calendar_day.html'
    })
    .when('/:id', {
        controller: 'EventController',
        templateUrl: '/static/js/views/calendar_event.html'
    })
    .otherwise({
        redirectTo: '/'
    });
  }]);