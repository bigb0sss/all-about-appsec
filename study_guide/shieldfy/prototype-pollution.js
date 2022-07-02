var test_obj = {};

console.log(test_obj.toString());

// You can call the constructor of any variable using variable_name.constructor and you can get the prototype of a variable
console.log(test_obj.constructor);

// Calling main object prototype
console.log(test_obj.constructor.prototype);

// Prototype pollution Example
// ------------------------------------------------------------------------------------------
var test1 = 1; 
var test2 = 2;

console.log(test1.constructor); // 1
console.log(test2.constructor); // 2

console.log(test2.toString());  // 2
// Exploiting prototype pollution to update "toString" to a function to return "bigb0ss"
test1.constructor.prototype.toString = function(){return "bigb0ss"}
console.log(test2.toString());  // bigb0ss

// ------------------------------------------------------------------------------------------

// Exploiting prototype pollution - ** What we are basically doing to bypass the auth using prototype pollution is that we are overwriting the existing function to whatever we want to bypass the validation. In this case we are overwriting the isAdmin() function to anything to bypass the === 0 validation.
var test = {"a":1}

console.log(test["a"] === test.a)   // true

// Authentication bypass 1
vulnFunc[year][term][subject] = grade;

if(user.isAdmin() === 0){
    console.log("Hi user");
} else {
    showAdmin();
}

// if year, term, subject and grade are user controllable an authentication bypass can be performed by setting year to constructor, term to prototype, subject to isAdmin and grade to any value you'd like to except 0, so when the user,isAdmin() check is performed it'll return the value of grade parameter which is not 0 so the check will pass and showAdmin() will be executed.

// Authentication bypass 2
// __proto__ (This is magic property) === constructor.prototype

info[name][first] = firstName;
if(user.isAdmin() === 0){
    console.log("Hi user");
} else {
    showAdmin();
}

// In this case we set the value of name to __proto__, the value of first to isAdmin and the value of firstName to whatever we want except 0 
