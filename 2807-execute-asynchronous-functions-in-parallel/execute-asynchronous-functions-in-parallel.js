/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let results = new Array(functions.length);
        let resolvedCount = 0;
        let hasRejected = false;

        functions.forEach((fn, index) => {
            fn()
                .then(result => {
                    if (hasRejected) return; // Ignore if already rejected
                    results[index] = result;
                    resolvedCount++;

                    if (resolvedCount === functions.length) {
                        resolve(results); // Resolve when all have completed
                    }
                })
                .catch(error => {
                    if (!hasRejected) {
                        hasRejected = true;
                        reject(error); // Reject on first failure
                    }
                });
        });

        if (functions.length === 0) {
            resolve([]); // Handle empty input case
        }
    });
};


/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */