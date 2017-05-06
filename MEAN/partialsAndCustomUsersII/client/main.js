console.log("string")
var app = angular.module("app", ["ngRoute"])
app.config(function($routeProvider) {
    $routeProvider
        .when('/users',{
            // templateUrl: 'static/partials/customizeUsers.html',
        })
        .otherwise({
        redirectTo: '/'
        });
});

app.factory("userFactory",[function(){
    var factory = {};

    //Initialize our list of users
    var users = [
      {firstName: "Yukihiro", lastName: "Matsumoto", language: "Ruby"},
      {firstName: "Ryan", lastName: "Dahl", language: "Javascript"},
      {firstName: "Brendan", lastName: "Eich", language: "Javascript"}
    ];

    factory.index = function(callback) {
       callback(users);
    }

    factory.create = function(user){
      users.push(user);
    }


   factory.delete = function($index) {
       users.splice($index, 1);
   }
   return factory;
}]) 

app.controller("CustomizeUsersController", ['$scope', 'userFactory', "$location",   function($scope, userFactory, $location){
    function setUsers(data) {
        $scope.users = data;
        $scope.newUser = {};
    }
    $scope.users = []

    userFactory.index(setUsers);

    $scope.create = function(){
      userFactory.create($scope.newUser)
      $scope.newUser = {}; //Reset our form
      $location.url("/list");
    }
    
   

    $scope.delete = function($index) {
        userFactory.delete($index);
    }

}])

app.controller("UserListsController", ['$scope', 'userFactory', function($scope, userFactory){
console.log("hi")
    function setUsers(data) {
        $scope.users = data
    }
    userFactory.index(setUsers);
}])