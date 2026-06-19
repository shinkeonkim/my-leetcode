const isPrimitive = obj => obj !== Object(obj);
const isObject = obj => obj.constructor == Object;
const isArray = obj => Array.isArray(obj);


/**
 * @param {null|boolean|number|string|Array|Object} o1
 * @param {null|boolean|number|string|Array|Object} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (o1 === o2) return true;

    if(isPrimitive(o1) || isPrimitive(o2)) {
        return false;
    }

    if(isArray(o1) || isArray(o2)) {
        if(!isArray(o1) || !isArray(o2)) return false;

        return (
            o1.length === o2.length &&
                o1.every((v, i) => areDeeplyEqual(v, o2[i]))
        )
    }

    const keys1 = Object.keys(o1);
    const keys2 = Object.keys(o2);

    return (
        keys1.length === keys2.length &&
            keys1.every(key => key in o2 && areDeeplyEqual(o1[key], o2[key]))
    )
};