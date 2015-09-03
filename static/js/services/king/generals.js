app.factory('generals', ['$http', function($http){
    return $http.get('/api/king/generals')
    .success(function(data){
        return data;
    })
    .error(function(err){
        return err;
    });
}]);