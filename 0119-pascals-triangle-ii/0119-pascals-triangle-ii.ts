function getRow(rowIndex: number): number[] {
    let row = [1];
    if(rowIndex == 0) return row;

    for(let i = 1; i <= rowIndex; i++) {
        const nextRow = [1];

        for (let j = 1; j < row.length; j++) {
            nextRow.push(row[j - 1] + row[j]);
        }

        nextRow.push(1);
        row = nextRow;
    }
    return row;
};