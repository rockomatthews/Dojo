var express = require('express');

var app = express();


var bodyParser = require('body-parser');
var session = require('express-session');


app.get('/', function(request, response) {
    response.send('<h1>Hello Express</h1>');
})
app.use(bodyParser.urlencoded({extended: true}));


// var app = express();

app.use(session({secret: 'codingdojorocks'}));

app.use(express.static(__dirname + "/static"));

app.set('views', __dirname + '/views'); 

app.set('view engine', 'ejs');

app.get('/users', function (request, response) {
    var users_array = [
        {name: "Michael", email: "michael@codingdojo.com"}, 
        {name: "Jay", email: "jay@codingdojo.com"}, 
        {name: "Brendan", email: "brendan@codingdojo.com"}, 
        {name: "Andrew", email: "andrew@codingdojo.com"}
    ];
    response.render('users', {users: users_array});
})

app.get('/index', function (req, res){
  res.render('index', {title: "my Express project"});
});
// route to process new user form data:

app.post('/users', function (req, res){
    console.log("POST DATA \n\n", req.body)
    var users_array = [
        {name: "Michaels", email: "michael@codingdojo.com"}, 
        {name: "Jay", email: "jay@codingdojo.com"}, 
        {name: "Brendan", email: "brendan@codingdojo.com"}, 
        {name: "Andrew", email: "andrew@codingdojo.com"}
    ];
    res.redirect('/users')
});

app.get("/users/:id", function (req, res){
    console.log("The user id requested is:", req.params.id);

    // res.send("You requested the user with id: " + req.params.id);
    var users_array = [
        {name: "Michaels", email: "michael@codingdojo.com"}, 
        {name: "Jay", email: "jay@codingdojo.com"}, 
        {name: "Brendan", email: "brendan@codingdojo.com"}, 
        {name: "Andrew", email: "andrew@codingdojo.com"}
    ];
    res.redirect('/users/id')
});

app.listen(8000, function() {
  console.log("listening on port 8000");
})