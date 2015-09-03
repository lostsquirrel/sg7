app.factory('soldiers', ['$http', function($http){
    return $http.get('/api/king/soldiers')
    .success(function(data){
        return data;
    })
    .error(function(err){
        return err;
    });
}]);

