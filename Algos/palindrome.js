// Write a function that takes a string, and returns a boolean based on 
// whether or not the string is a palindrome.

// EXAMPLE: "tacocat" is a palindrome because it is the same backwards and forwards.

// Challenge: ignore spaces, so "taco cat" would still return true






// function isPalindrome(string) {
//     var count = 0;
//     console.log(string.length)
//     for (var i=0; i<string.length/2;i++){
//         if (string[i]==string[string.length-i-1]){
//             console.log(string[i] == string[string.length-i-1],":",count)
//             count ++
//         };
//         if (count >= string.length/2){
//             console.log('This is a palindrom!!!')
//         };
//     };
//     console.log(count)
// }

// isPalindrome("tacocat")


// function isPalindrome2(string) {
    // var newstr = '';
    // for (i = 0;i<string.length;i++) {
    //     if (string[i] !== ' ') {
    //         newstr+=string[i];
    //     }
    // }
    
//     var strcheck = false;
//     var j = 0;
//     var k = 0;
//     for (var i=0;i<string.length/2;i++) {
//         console.log("i: ",i)
//         if (string[i] == " "){
//             j ++
//             console.log("j: ",j)
//         }
//         if (string[string.length-i-1] == " "){
//             k ++
//             console.log("k: ",k)
//         }
//         console.log(string[i+j],"  ",string[string.length-i-k-1])
//         if (string[i+j] == string[string.length-i-k-1]) {
//             strcheck = true;
//             console.log("strcheck: ", i, " ", strcheck)
//         } else {
//             return false;
//         }
//     }
//     if (strcheck = true) {
//         return true;
//     } else {
//         return false;
//     }
// }

function isPalindrome2(string){
    var i = 0;
    var j = string.length-1;
    while (i<j){
        if (string[i]==" "){
            i ++;
        }
        else {
            firstIsLetter = true
        }

        if (string[j]==" "){
            j --;
        }
        else {
            lastIsLetter = true
        }
        if (firstIsLetter == true && lastIsLetter ==true){
            if(string[i]!=string[j]){
                return console.log("This is not a Palindrome!!")
            }
        }
    }
    console.log("This is a Palindrome!!!")
}

console.log(isPalindrome2("tac               o cat"));

// CHALLENGE ALGORITHM: Write a function that will find and return the longest palindrome within a string
// EXAMPLE: "the man ate a banana with his tacocat at dinner the other day" would return "tacocat"
function longestPalindrome(string) {

}