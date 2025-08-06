"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function isValid(word) {
    let hasVowel = false;
    let hasConsonant = false;
    if (word.length < 3) {
        return false;
    }
    for (let i = 0; i < word.length; i++) {
        if (!hasVowel &&
            ['a', 'e', 'i', 'o', 'u'].includes(word.charAt(i).toLowerCase())) {
            hasVowel = true;
        }
        if (!hasConsonant &&
            /[A-Za-z]/.test(word.charAt(i)) &&
            !['a', 'e', 'i', 'o', 'u'].includes(word.charAt(i).toLocaleLowerCase())) {
            hasConsonant = true;
        }
        if (!/^[a-zA-Z0-9]+$/.test(word.charAt(i))) {
            return false;
        }
    }
    if (hasConsonant && hasVowel) {
        return true;
    }
    return false;
}
console.log(isValid("UuE6"));
//# sourceMappingURL=3136-valid-word.js.map