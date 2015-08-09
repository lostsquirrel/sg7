var controllers = angular.module('controllers', []);

var countPage = function(tag, data) {
    page = data ? data.page : 1;
    pages = data ? data.pages : 0;
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

        $scope.load_more = function(tag) {

            page = countPage(tag, $scope.data)
    //        console.log('--------------------' + page)
            $http.get("/cities?page=" + page).success(function(response) {
                $scope.data = response;
    //            console.log('--------------------' + response.page)
            });
        }
//        console.debug("----------")
        $scope.load_more(0);
    }]);

controllers.controller('itemCtrl', ['$scope', '$http',
    function($scope, $http) {
        $scope.load_more = function(tag) {
            page = countPage(tag, $scope.data)
            $http.get("/items?page=" + page).success(function(response) {
                $scope.data = response;
    //        $scope.phoneId = $routeParams.phoneId;
            });
        };
        $scope.load_more(0);
    }]);

controllers.controller('mapCtrl', ['$scope', '$http',
    function($scope, $http) {

    }]);
controllers.controller('aboutUsCtrl', ['$scope', '$http',
    function($scope, $http) {

    }]);
controllers.controller('baseCtrl', ['$scope', '$http',
    function($scope, $http) {
        $scope.welcome = "欢迎访问本站，请点击左菜单查看相关内容"
    }]);


