app.factory('formulas', [ function(){
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
    }
    ];

    return formulas;
}]);