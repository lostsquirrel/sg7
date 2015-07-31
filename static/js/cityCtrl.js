 app.controller('cityCtrl', function($scope, $http) {
            $http.get(host + "/cities")
        .success(function(response) {
            $scope.cities = response;
        });
 });