app.directive('game', function(){
  return {
    restrict: 'E',
    scope: {
      info: '='
    },
    templateUrl: '/static/js/directives/game.html'
  }
});