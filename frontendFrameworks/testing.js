var ironman = {
    name: "Tony Stark",
    alias: "Iron Man"
   };
   var avengers_array = [
    {name: "Tony Stark", alias: "Iron Man", ability: "flight"},
    {name: "Bruce Banner", alias: "The Incredible Hulk", ability: "superhuman strength"},
    {name: "Steve Rogers", alias: "Captain America", ability: "superhuman strength"},
    {name: "Clint Barton", alias: "Hawkeye", ability: "superior hand-eye coordination"},
    {name: "Thor Odinson", alias: "Thor", ability: "teleportation"},
    {name: "Natasha Romanova", alias: "Black Widow", ability: "espionage"}
   ];

   var firstAvenger = first(avengers_array);

   console.log(firstAvenger);