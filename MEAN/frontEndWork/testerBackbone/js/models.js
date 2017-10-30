var UserModel = Backbone.Model.extend({
    defaults: {
        name: null,
        age: null,
    }
})

var user1 = new UserModel({name: "Johnny", age: 21})

console.log(user1);