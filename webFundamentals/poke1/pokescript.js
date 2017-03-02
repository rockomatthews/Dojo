$(document).ready(function(){
    var poke;
    for (var i = 1; i <= 151; i++){
        poke = "<img src='http://pokeapi.co/media/img/" + i + ".png'>";
        $(".container").append(poke);
    } 
})