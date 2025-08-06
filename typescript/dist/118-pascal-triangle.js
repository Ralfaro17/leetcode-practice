"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// numRows is the argument LeetCode uses
let numRows = 5;
let result = [];
for (let row = 1; row < numRows + 1; row++) {
    let temp = [];
    for (let column = 0; column < row; column++) {
        if (row <= 2) {
            temp.push(1);
        }
        else {
            if ((column - 1 < 0) || (column > row - 2)) {
                temp.push(1);
            }
            else {
                temp.push((result[row - 2]?.[column - 1] ?? 0) + (result[row - 2]?.[column] ?? 0));
            }
        }
    }
    result.push(temp);
}
console.log(result);
// return result
//# sourceMappingURL=118-pascal-triangle.js.map