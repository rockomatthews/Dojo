$(document).ready(function(){
    $(".dropdown" ).css('visibility','hidden');
    $(".dropdown2" ).css('visibility','hidden');
    $(".game-window" ).css('visibility','hidden');
    $(".arena-button1").hover(function(){
    $(".game-window" ).css('visibility','visible');
    })
    $(".arena-button1").mouseout(function(){
        $(".game-window" ).css('visibility','hidden');
    })
    $(".game-window2" ).css('visibility','hidden');
        $(".arena-button2").hover(function(){
        $(".game-window2" ).css('visibility','visible');
    })
    $(".arena-button2").mouseout(function(){
        $(".game-window2" ).css('visibility','hidden');
    })
    $(".game-window3" ).css('visibility','hidden');
        $(".arena-button3").hover(function(){
        $(".game-window3" ).css('visibility','visible');
    })
    $(".arena-button3").mouseout(function(){
        $(".game-window3" ).css('visibility','hidden');
    })
    $(".game-window4" ).css('visibility','hidden');
        $(".arena-button4").hover(function(){
        $(".game-window4" ).css('visibility','visible');
    })
    $(".arena-button4").mouseout(function(){
        $(".game-window4" ).css('visibility','hidden');
    })
    $(".game-window5" ).css('visibility','hidden');
        $(".arena-button5").hover(function(){
        $(".game-window5" ).css('visibility','visible');
    })
    $(".arena-button5").mouseout(function(){
        $(".game-window5" ).css('visibility','hidden');
    })
    $(".game-window6" ).css('visibility','hidden');
        $(".arena-button6").hover(function(){
        $(".game-window6" ).css('visibility','visible');
    })
    $(".arena-button6").mouseout(function(){
        $(".game-window6" ).css('visibility','hidden');
    })
    $(".arena-button1" ).click(function(){
        $(".select-arena-module").css('visibility','hidden');
        $('.container').css('background-image', "url('images/beachFight.jpg')");
        $(".game-window").css('visibility','hidden');
        $(".game-window" ).css('visibility','hidden');
        $(".dropdown" ).css('visibility','visible');
    })
    $(".dropdown-content a.leo").click(function(){
        $(".dropdown").css('visibility','hidden');
        $(".dropdown2").css('visibility','visible');
    })

})