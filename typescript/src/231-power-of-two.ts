function isPowerOfTwo(n: number): boolean {
  let exponent = 0;
  let base = 1;

  while (base <= n) {
    if (base == n) {
      return true;
    } else {
      exponent += 1;
      base = 2 ** exponent;
    }
  }

  return false;
}

console.log(isPowerOfTwo(2))