var app = angular.module('app', ['ngRoute']);
app.config(function ($routeProvider) {
    $routeProvider
        .when('/players', {
            templateUrl: 'static/partials/players.html',
            controller: "PlayersController" 
        })
        .when('/teams', {
            templateUrl: 'static/partials/teams.html',
            controller: "TeamsController" 
        })
        .when('/associations', {
            templateUrl: 'static/partials/associations.html',
            controller: "AssociationsController" 
        })
        .otherwise( {
            redirectTo: '/players'
        });
});

app.factory("playerFactory", [function() {
    var factory = {};

    var players = [
        {name: "Yukihiro"},
        {name: "Ryan"},
        {name: "Brendan"}
    ];

    factory.index = function(callback) {
        callback(players);
    }

    factory.create = function(player){
        players.push(player);
    }

    factory.delete = function($index) {
        players.splice($index, 1);
    }
    return factory;
}])

app.factory("teamFactory", [function() {
    var factory = {};

    var players = [
        {name: "Yukihiro Team"},
        {name: "Team Ryan"},
        {name: "Brendan The Team"}
    ];
    
    factory.index = function(callback) {
        callback(teams);
    }

    factory.create = function(player){
        players.push(team);
    }

    factory.delete = function($index) {
        teams.splice($index, 1);
    }
    return factory;
}])

app.controller("PlayersController", ['$scope', 'playerFactory', "$location", function($scope, playerFactory, $location) {
    function setPlayers(data) {
        $scope.players = data;
        $scope.newPlayer = {};
    }
    $scope.players = []

    playerFactory.index(setPlayers);

    $scope.create = function() {
        playerFactory.create($scope.newPlayer)
        $scope.newPlayer = {};
    }
    console.log("This is players")

    $scope.delete = function($index) {
        playerFactory.delete($index);   
    }
}])

app.controller("TeamsController", [function() {
    console.log("This is teams")
}])

app.controller("AssociationsController", [function() {
    console.log("This is assoc")
}])


