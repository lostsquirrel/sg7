app.factory('formulas', ['$http', function($http){
    var formulas = [
    function(level) {
        return level + 2;
    },
    function(level) {
        return 17 * level - Math.floor(level/3) - 1;
    },
    function(level) {
        return (19.7 + (level - 1) * 0.3 - Math.floor(level/7)/100).toFixed(2);
    },
    function(level) {
        return 18 * level + Math.floor((level - 1) / 3);
    },
    function(level) {
        var x = 0;
        var temp = level;
        while(temp) {
            if (temp <= 10) {
                if (temp % 3 == 0) {
                    x += 0.01
                }
            } else {
                var y = temp % 10;
                if (y == 0 || y == 3 || y == 6) {
                    x += 0.01;
                }
            }
            temp--;
        }
        var z = 25.93 + 0.39 * (level - 1) + x
        return z.toFixed(2);
    }
    ];

    return formulas;
}]);