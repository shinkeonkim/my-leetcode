/** 
 * @return {string}
 */
Date.prototype.nextDay = function() {
    let ret = new Date(this);
    ret.setDate(ret.getDate() + 1)
    return ret.toISOString().substring(0, 10)
}
/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */