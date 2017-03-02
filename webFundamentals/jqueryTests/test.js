$(document).ready(function(){
    // $("h1").click(function(){
    //     alert("this is a hotshot popup");
    // })
    // $("h2").click(function(){
    //     $(this).hide("slow");
    // })
    // $(".boxes img").click(function(){
    //     $( "h2" ).show("fast");
    // })
    // $(".main-content img").hide();
    // $(".footer").click(function(){
    //     $(".main-content img").slideDown( 1000 ); 
    // })
    // $(".main-content img").hide();
    // $(".box button").click(function(){
    //     $(".main-content img").slideUp(1000);
    // })
    // $(".header li").click(function(){
    //     $(".boxes img").slideToggle(2000);
    // })
    // $(".bottom-box img").click(function(){
    //     $(".bottom-box img").fadeOut(1000);
    //     $(".bottom-box img").fadeIn(4000);
    // })
    // $(".box").click(function(){
    //    $( ".box" ).removeClass( "box" ).addClass( "box-dark" );
    // }) 
    // $(".box").click(function(){
    // $( "h2" ).before( "<h1>OMG HI!!!</h1>" );
    // })
    // $(".bottom-box button").click(function(){
    // $( ".bottom-box button" ).after( "<h1>about you!!!</h1>" );
    // })
    // $(".box").click(function(){
    // $( ".bottom-box button" ).append( "<h1>!!!</h1>" );
    // })
    $(".container box1").click(function(){
        $(this).hide("slow");
    })
    
    
    $("h2:first").text("Don't click here");
    $("h2:first").click(function(){
        $( ".header" ).html( "<img src='images/baneWeb.jpg' alt='BANE'>" );
        $(".main-content img").hide();
        $(".boxes").hide();
        alert("ugh you let Bane take the site.  Idiot.");
    })
});
