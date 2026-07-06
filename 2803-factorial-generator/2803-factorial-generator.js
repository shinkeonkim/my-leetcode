/**
 * @param {number} n
 * @yields {number}
 */
function* factorial(n) {
    if(n == 0) {
        yield 1;
        return;
    }


    let i = 1;
    let ret = 1;

    while (i <= n) {
        yield ret;
        i += 1;
        ret *= i;
    }
};

/**
 * const gen = factorial(2);
 * gen.next().value; // 1
 * gen.next().value; // 2
 */