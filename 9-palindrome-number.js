/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0){
        return false
    }

    x = x.toString()

    for(i = 0; i < (x.length/2).toFixed(0); i++){
        if (x[i] != x[x.length-i-1]){
            return false
        }
    }
    
    return true
};

console.log(isPalindrome(10))