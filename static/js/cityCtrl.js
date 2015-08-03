var controllers = angular.module('controllers', []);

var countPage = function(tag, page, pages) {
    if (Math.abs(tag) == 1) {
        page += tag;
    } else if (tag > 1) {
        page = pages;
    } else {
        page = 1;
    }

    return page;
}

controllers.controller('cityCtrl', ['$scope', '$http',
    function($scope, $http) {

        $scope.load_cities = function(tag) {
            page = $scope.cities ? $scope.cities.page : 1;
            pages = $scope.cities ? $scope.cities.pages : 0;
            page = countPage(tag, page, pages)
    //        console.log('--------------------' + page)
            $http.get("/cities?page=" + page).success(function(response) {
                $scope.cities = response;
    //            console.log('--------------------' + response.page)
            });
        }
        console.debug("----------")
        $scope.load_cities(0);
    }]);

controllers.controller('itemCtrl', ['$scope', '$http',
    function($scope, $http) {
        $http.get("/items").success(function(response) {
            $scope.items = response;
//        $scope.phoneId = $routeParams.phoneId;
    })}]);



