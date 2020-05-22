// Write a function that accepts a number representing a number of cents, and 
// prints a representation of that monetary amount with the smallest number of 
// coins.

// EXAMPLE: coinChange(137) should print something like:
// Quarters: 5
// Dimes: 1
// Nickels: 0
// Pennies: 2
function coinChange(cents) {
    var quarter = 25;
    var dime = 10;
    var nickel = 5;
    var penny = 1;
    var numQ = Math.floor(cents/quarter);
    console.log("Quarters: " + numQ);
    cents -= numQ*quarter;
    var numD = Math.floor(cents/dime);
    console.log("Dimes: " + numD);
    cents -= numD*dime;
    var numN = Math.floor(cents/nickel);
    cents -= numN*nickel
    console.log("Nickels " + numN)
    var numP = Math.floor(cents/penny);
    cents -= numP*penny;
    console.log("Pennies " + numP)
    
}

coinChange(137);