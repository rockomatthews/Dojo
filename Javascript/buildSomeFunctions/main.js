function runningLogger(){
    console.log('I am running')
}
runningLogger();

function multiplyByTen(x){
    var multiplied = x * 10;
    console.log(multiplied);
}
multiplyByTen(5);

function stringReturn1(){
    console.log("This is string one");
}
stringReturn1();

function stringReturn2(){
    console.log("Tihs is string two");
}
stringReturn2();

function caller(param){
    if (typeof(param)=='function'){
        param();
    }
}
caller(stringReturn1);

function myDoubleConsoleLog(param1, param2){
    if(typeof(param1)=='function'){
        param1();
    }
    if (typeof(param2)=='function'){
        param2();
    }
}
myDoubleConsoleLog(stringReturn1, stringReturn2);

function caller2(param){
    console.log('starting');
    var x = setTimeout(function(){
        if (typeof(param)=='function');
            param(stringReturn1, stringReturn2);
    }, 2000);
    console.log('ending');
    return 'interesting';
}
caller2(myDoubleConsoleLog);