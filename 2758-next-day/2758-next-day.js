/** 
 * @return {string}
 */
Date.prototype.nextDay = function() {
    let ret = new Date(this);
    ret.setDate(ret.getDate() + 1)
    return `${ret.getFullYear()}-${String(ret.getMonth() + 1).padStart(2, "0")}-${String(ret.getDate()).padStart(2, "0")}`
}
/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */