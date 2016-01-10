app.factory('soldier_ak', ['$http', function($http){
    return $http.get('/api/king/soldier')
    .success(function(data){
        return data;
    })
    .error(function(err){
        return err;
    });
}]);