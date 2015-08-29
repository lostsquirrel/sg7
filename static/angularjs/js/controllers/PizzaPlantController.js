app.controller('MainController', ['$scope', function($scope) {
  $scope.today = new Date();

  $scope.appetizers = [
    {
      name: 'Caprese',
      description: 'Mozzarella, tomatoes, basil, balsmaic glaze.',
      price: 4.95
    },
    {
      name: 'Mozzarella Sticks',
      description: 'Served with marinara sauce.',
      price: 3.95
    }
  ];

  $scope.mains = [

    {
      name: 'MARGHERITA',
      description: 'Marinara sauce, mozzarella, fresh basil.',
      price: 6.95
    },
    {
      name: 'PEPPERONI',
      description: 'Pepperoni, marinara sauce, mozzarella, fresh oregano.',
      price: 7.95
    },
    {
      name: 'RUSTICA',
      description: 'Marinara sauce, kalamata olives, roasted garlic, fresh oregano.',
      price: 8.95
    }
  ];

  $scope.extras = [

    {
      name: 'BREADSTICKS',
      description: 'Served with marinara sauce.',
      price: 3.95
    },
    {
      name: 'SOUP OF THE DAY',
      description: 'Take a chance.',
      price: 3.95
    },
    {
      name: 'BUFFALO WINGS',
      description: 'Feel the power of wings.',
      price: 5.95
    }
  ];

}]);