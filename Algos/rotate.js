// Write a function that is given a string and a number, and returns the string rotated to the 
// right that many times

// EXAMPLE: rotate("hello world", 3) would return "rldhello wo", because you've essentially
// shifted the string to the right 3 times, and the text at the end "wrapped around" for the
// rotation
function rotate(string, num){
    newstr = ""
    for (var i=string.length-num;i<string.length;i++){
        newstr = newstr + string[i]
    }
    for (var i=0;i<string.length-num;i++){
        newstr = newstr + string[i]
    }
    return newstr
}

// oString = "hello wo    rld This is me and myy frie   ndssss"
// oString = "-- ?"
// console.log(rotate(oString,11))
// tString = rotate(oString,11)
// Write a function that will take 2 strings (oString and tString, for original string and test string),
// and return a boolean based on whether or not tString is a rotated version of oString

// EXAMPLE: isRotation("hello world", "rldhello wo") would return true, because, as we saw in the previous
// algorithm, "hello world", rotate right 3 spots, returns "rldhello wo"
function isRotation(oString, tString){
    if (oString.length == tString.length){
        for (var i=1;i<oString.length;i++){
            rotate(oString,i)
            console.log(newstr)
            if (newstr == tString){
                return true
            };
        };
        return false
    }
    else{
        return false
    };
};

console.log(isRotation("hello world", "rldhello wo"))
// console.log(isRotation(oString,tString))