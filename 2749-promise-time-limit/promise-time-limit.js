/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        return new Promise((resolve, reject) => {
            // Start the execution of the provided function
            const fnPromise = fn(...args).then(resolve).catch(reject);
            
            // Set a timeout to reject if time exceeds
            const timer = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);

            // Ensure the timer is cleared if fn resolves in time
            fnPromise.finally(() => clearTimeout(timer));
        });
    };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */