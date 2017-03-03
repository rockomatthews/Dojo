$(document).ready(function(){
    var poke;
    for (var i = 1; i <= 151; i++){
        poke = "<img id='" + i + "' src='http://pokeapi.co/media/img/" + i + ".png'>";
        $(".left-side").append(poke);
    }
    $('img').click(function(res){
        $(".right-side").append(poke);
    })
})
