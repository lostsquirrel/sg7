app.controller('OutboxController', ['$scope', 'emails', function($scope, emails) {
    emails.success(function(data){
        $scope.emails = data;
    });
}]);