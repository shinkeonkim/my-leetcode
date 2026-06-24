/** 
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function(target) {
    let ans = -1;

    let left = 0;
    let right = this.length - 1;

    while(left <= right) {
        let mid = (left + right) >> 1;

        console.log(left, mid, right);

        if(this[mid] <= target) {
            if(this[mid] == target) {
                ans = Math.max(ans, mid);
            }

            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
};


// [3,4,5].upperBound(5); // 2
// [1,4,5].upperBound(2); // -1
// [3,4,6,6,6,6,7].upperBound(6) // 5