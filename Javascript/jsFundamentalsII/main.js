// function addr(x, y){
//     var sum = 0;
//     for(var i = x; i <= y; i++){
//         sum += i
//     }
//     return sum;
// }

// // console.log(addr(10, 12));

// function minInArray(arr){
    
//     for (var i = 1; i < arr.length; i++){
//         var small = arr[0];
//         if (arr[i] < small){
//             small = arr[i];
//         }
//     } 
//     return small; 
// }

// // console.log(minInArray([20,80,8,10,4,1]));

// function daAvg(arr){
//     var sum = 0;
//     for (var i = 0; i < arr.length; i++){
//         sum += arr[i];
//         avg = sum / arr.length;
//     }
//     return avg;
// }

// console.log(daAvg([20,80,8,10,4,1]))


///////////////////////////////////////////////////////////////////////

var person = {
  name: "Rob",
  distance_traveled: 0,
  say_name: function(){
    console.log(person.name);
  },
  say_something: function(phrase){
    console.log(`${person.name} says: ${phrase}`);
    return person;
  },
  walk: function(){
    console.log(`${person.name} is walking!`);
    person.distance_traveled += 3;
    return person;
  },
  run: function(){
    console.log('${person.name} is running!');
    person.distance_traveled += 10;
    return person;
  }
  
}

person.walk().run().say_something('fuck');
console.log(person.distance_traveled);
