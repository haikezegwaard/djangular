var appleServices = angular.module('appleServices', ['ngResource']);

appleServices.factory('Apple', ['$resource',
  function($resource){
    return $resource('/:appleId.json', {}, {
      query: {method:'GET', params:{appleId:'apples'}, isArray:true}
    });
  }]);