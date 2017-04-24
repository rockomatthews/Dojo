var thisApp = angular.module('thisApp',[]);
thisApp.factory("productFactory", ["http", function($http) {

}])

app.controller('productsController', ['$scope','productFactory', function($scope, productFactory) {
  // callback, but not as an anonymous function, rather a named function!
  function setProducts(data){
    $scope.products = data;
    $scope.product = {};
  }

  $scope.product = {};
  $scope.products = {};

  $scope.index = function(){
    productFactory.index(setProducts);
  }

  $scope.index();
  $scope.create = function(){
    productFactory.create($scope.product, setProducts);
  }
  $scope.delete = function(id){
    productFactory.delete(id,setProducts);
  }

}]);

app.controller('productsController', [
    '$scope',
    'productFactory',
    function($scope, productFactory) {
        $scope.products = data;
        $scope.product = {};
    
    function setProducts(data){
        $scope.products = data;
        $scope.product = {};
    }

        $scope.product = {};
        $scope.products = {};

    $scope.index = function(){
        productFactory.index(setProducts);
    }

    $scope.index();
    $scope.create = function(){
        productFactory.create($scope.product, setProducts);
    }
    $scope. = function(id){
        productFactory.delete(id,setProducts);
    }
}])

