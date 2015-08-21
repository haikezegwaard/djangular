var appleControllers = angular.module('appleControllers', []);

/*
 * Controller for listing all apples, working.
 */
appleControllers.controller('AppleListCtrl', ['$scope', 'Apple', function($scope, Apple) {
  $scope.apples = Apple.query();
  $scope.orderProp = 'color';
}]);

/*
 * Controller for specific apple, test this
 */
appleControllers.controller('AppleDetailCtrl', ['$scope', '$routeParams', 'Apple', function($scope, $routeParams, Apple) {
  $scope.phone = Apple.get({appleId: $routeParams.appleId}, function(apple) {
    
  });
}]);