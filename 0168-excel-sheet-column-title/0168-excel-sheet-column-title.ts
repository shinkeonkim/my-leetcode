function convertToTitle(columnNumber: number): string {
    if(columnNumber <= 26) {
        return String.fromCharCode(columnNumber + 64);
    }
    columnNumber -= 1;
    return convertToTitle(Math.floor(columnNumber / 26)) + String.fromCharCode((columnNumber % 26) + 65); 
};