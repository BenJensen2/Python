// Write a function that will take an array of numbers, and return the
// sum of all unique numbers in that array. Hint: Use a frequency table!

// A frequency table is a dictionary where, in each key-value pair, 
// the key is the item in the array, and the value is the number of times
// that thing appears

// EXAMPLE: [1,3,3,6,6,7,8,10] will return 26 because 1+7+8+10 = 26

function sumUniques(arr){
    dictionary = {};
    for (var i = 0;i<arr.length;i++){
        console.log()
        dictionary[arr[i]] = i;
    }
}



// function sumUniques(arr){
//     var new_arr = [];
//     for(var i=0;i<arr.length;i++){
//         double = false;
//         for(var j= i+1;j<arr.length-1;j++){
//             if (arr[i] == arr[j]){
//                 double = true;
//             };
//         console.log(arr[i]," : ", arr[j], " : ",double)
//         };
//         if (double == false){
//             console.log("push")
//             new_arr.push(arr[i])
//         };
//     };
//     console.log(new_arr)
// };

// sumUniques([1,3,3,6,6,7,8,10])


// function sumUniques(array) {
//     // var dict = {};
//     var new_array = {};
//     for (var i = 0; i<array.length; i++){
//         double = false
//         for (var j=1+i; j<array.length-1;j++){
//             console.log("i: ",i,"array[i]: ",array[i], " : ","j: ",j, "array[j]: ", array[j])
//             if (array[i]=array[j]){
//                 double = true
//             };
//         };
//         // if(double = false) {
//         //     new_array.push(array[i])
//         // };
//         // dict[array[i]] = 0;
//     };
//     // console.log(dict)
//     console.log(new_array)
// };

// sumUniques([1,3,3,6,6,7,8,10])

// Write a function that will take a string, and return a new string that contains
// the same words, but in reverse.

// EXAMPLE: "hello world my name is Cody" will return "Cody is name my world hello"
function reverseWordOrder(string) {
    
}