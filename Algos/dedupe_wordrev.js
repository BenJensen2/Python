// Write a function that will remove duplicate characters (case-sensitive)
// including punctuation. Keep only the LAST instance of each character

// EXAMPLE: Given "Snaps! crackles! pops!", return "Snrackle ops!"
// dictionary = {!:1,s:1,p:1,o:1}



function dedupe(string){
    var dictionary = {};
    var new_string =""
    for(var i=string.length-1;i>=0;i--){
        if(!(string[i] in dictionary)){
            new_string = string[i]+new_string;
            dictionary[string[i]]=1;
        }
    }
    return new_string
}

console.log(dedupe("Snaps! crackles! pops!"))
// Write a function that, given a string, will maintain the order of each word,
// but reverse each word individually.

// EXAMPLE: Given "hello world my name is Cody", return
// "olleh dlrow ym eman si ydoC"
function reverseWords(string){
    console.log(string);

    var array = string.split(" ");
    console.log(array);
    
    var new_string = "";
    console.log(new_string)
    
    for(var i=0;i<array.length;i++){
        console.log(array[i])        
    
        for(var j = array[i].length; j>=0;j--){
    
            new_string = new_string + string[i]
        };
    
        console.log(new_string)
    };
};

// reverseWords("hello world my name is Cody")