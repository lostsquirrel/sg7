app.controller('CalendarDayController', ['$scope', 'events', function($scope, events) {
    events.success(function(data){
        $scope.day = data;
    });
}]);