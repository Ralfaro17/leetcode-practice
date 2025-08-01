// numRows is the argument LeetCode uses
let numRows: number = 5;

let result: number[][] = [];

for (let row = 1; row < numRows + 1; row++) {
  let temp: number[] = [];
  for (let column = 0; column < row; column++) {
    if (row <= 2) {
      temp.push(1);
    }
    else{
      if ((column - 1 < 0) || (column > row - 2)){
        temp.push(1)
      }
      else{
        temp.push(result[row - 2][column - 1] + result[row - 2][column])
      }
    }
  }
  result.push(temp)
}

console.log(result)
// return result