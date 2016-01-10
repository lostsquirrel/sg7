app.factory('soldiers', ['$http', function($http){

    return function(soldier_id) {
        $http.get('/api/king/soldier/ak?soldier_id='+soldier_id,)
        .then(function(response){
            return response;
        }, function(response){
            return response;
        });
    }
}]);

