/**
 * @param {number} year
 * @param {number} month
 * @return {number}
 */
var numberOfDays = function(year, month) {
    const monthsWith31 = [1, 3, 5, 7, 8, 10, 12];
    const monthsWith30 = [ 4, 6, 9, 11];
    if(monthsWith31.includes(month)){
        return 31
    }
    if(monthsWith30.includes(month)){
        return 30
    }
    if((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)){
        return 29
    }
    return 28
};