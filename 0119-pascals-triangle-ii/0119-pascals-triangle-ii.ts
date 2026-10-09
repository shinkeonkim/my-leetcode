function getRow(rowIndex: number): number[] {
    let current = [1];
    if(rowIndex == 0) return current;

    for(let i = 1; i <= rowIndex; i++) {
        let tmp = [1];

        for(let i = 1; i < current.length; i++) {
            tmp.push(current[i - 1] + current[i]);
        }
        tmp.push(1);

        current = tmp;
    }
    return current;
};