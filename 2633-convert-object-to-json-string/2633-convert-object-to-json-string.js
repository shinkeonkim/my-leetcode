const isPrimitive = obj => obj !== Object(obj);
const isObject = obj => obj.constructor == Object;
const isArray = obj => Array.isArray(obj);
const isString = obj => typeof obj === "string";

/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) {
        return "null";
    }

    if (isString(object)) {
        return `"${object}"`
    }

    if(isPrimitive(object)) {
        return "" + object
    }

    if(isArray(object)) {
        return "[" + object.map((v) => jsonStringify(v)).join(",") + "]";
    }

    let keys = Object.keys(object);
    return "{" + keys.map((key) => `"${key}":${jsonStringify(object[key])}`) + "}"
};