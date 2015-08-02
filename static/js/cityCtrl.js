 app.controller('cityCtrl', function($scope, $http) {


    $scope.load_cities = function(tag) {
        page = $scope.cities ? $scope.cities.page : 1;
        if (Math.abs(tag) == 1) {
            page += tag;
        } else if (tag > 1) {
            page = $scope.cities.pages;
        } else {
            page = 1;
        }
//        console.log('--------------------' + page)
        $http.get("/cities?page=" + page).success(function(response) {
            $scope.cities = response;
//            console.log('--------------------' + response.page)
        });
    }


 });