app.directive('skillDesc', function(){
  return {
    restrict: 'E',

    template: function(elem, attr){
        return (attr.formatter).replace('{0}', attr.level + 2)
    },

  }
});