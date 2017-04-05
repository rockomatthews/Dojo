x = [3,5,"Dojo", "rocks", "Michael", "Sensei"]

for (var i = 0; i < x.length; i++) {
    console.log(x[i]);
}

x.push(100);

console.log(x);

newarray = ["hello", "world", "JavaScript is Fun"]
var newarray = x;

console.log(newarray);


the_sum = 0
for (var i = 1; i < 501; i++){
    the_sum += i;
    console.log(the_sum);
}

var rayray = [1, 5, 90, 25, -3, 0];

minimum = 30;
for (var i = 0; i < rayray.length; i++){
    if (rayray[i] < minimum){
        minimum = rayray[i];
        
    }
 
}    console.log(minimum);


var adder = 0;
this_array = [1, 5, 90, 25, -3, 0]

for (var i = 0; i < this_array.length; i++){
    adder += this_array[i];
} avger = adder / this_array.length;

console.log(avger);

var newNinja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
}


for (var key in newNinja){
    console.log(key, newNinja[key])
}