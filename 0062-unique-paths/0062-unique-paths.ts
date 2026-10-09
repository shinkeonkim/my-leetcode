function uniquePaths(m: number, n: number): number {
    m -= 1;
    n -= 1;

    let k = 1;

    let mn = Math.min(n, m);
    let mx = Math.max(n, m);

    for(let i = mx + 1; i <= m + n; i++) {
        k *= i;
    }

    for(let i = 2; i <= mn; i++) {
        k = k / i;
    }

    return k;
};