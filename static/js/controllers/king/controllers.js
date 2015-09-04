app.controller('SoldiersController', ['$sce', '$scope', 'formulas', 'soldiers',
function($sce, $scope, formulas, soldiers) {
    $scope.range_type = ['近战', '远程'];
    $scope.soldier_type = ['步兵', '骑兵'];
    $scope.armor_type = ['轻甲', '重甲'];
    $scope.formulas = formulas;
    $scope.level = 1;


    $scope.affect = function() {
//        console.debug($scope.level)
//        console.debug($scope.soldiers)
        for (sd in $scope.soldiers) {
            sd = $scope.soldiers[sd]
            for (sk in sd.skills) {
                sk = sd.skills[sk]
                sk.skill_desc_x = sk.skill_desc.replace('{0}', "<span class=\"level\">" + ($scope.level + 2) + "</span>");
                if (sk.formula) {
                    sk.skill_desc_x = sk.skill_desc_x.replace('{1}', "<span class=\"affect\">" + $scope.formulas[sk.formula]($scope.level) + "</span>");
                }
                sk.skill_desc_x = $sce.trustAsHtml(sk.skill_desc_x);
            }
        }
    };
    soldiers.success(function(data) {
        $scope.soldiers = data;
        $scope.affect();
    });

}])
.controller('GeneralsController', ['$scope','generals', 'soldiers',
function($scope, generals, soldiers){
    generals.success(function(data) {
        $scope.generals = data;
    });
    soldiers.success(function(data) {
        $scope.soldiers = data;
    });
}])
.controller('HomeController', ['$scope',
function($scope){
    $scope.welcome = "欢迎访问本站，请点击左菜单查看相关内容!"
}])
.controller('AboutController', [])
;