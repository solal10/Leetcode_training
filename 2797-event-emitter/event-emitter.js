class EventEmitter {
    constructor() {
        this.events = {}; 
    }

    /**
     * Subscribes a callback function to an event.
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object} An object with an `unsubscribe` method.
     */
    subscribe(eventName, callback) {
        if (!this.events[eventName]) {
            this.events[eventName] = []; // Initialize event list
        }

        this.events[eventName].push(callback); // Store callback

        return {
            unsubscribe: () => {
                this.events[eventName] = this.events[eventName].filter(fn => fn !== callback);
            }
        };
    }

    /**
     * Emits an event and calls all registered callbacks with given arguments.
     * @param {string} eventName
     * @param {Array} args
     * @return {Array} Array of return values from all callbacks.
     */
    emit(eventName, args = []) {
        if (!this.events[eventName]) return []; // No listeners exist
        
        return this.events[eventName].map(callback => callback(...args));
    }
}

/**
 * Example Usage
 */
const emitter = new EventEmitter();

// Subscribe to the onClick event
function onClickCallback() { return 99; }
const sub = emitter.subscribe('onClick', onClickCallback);

console.log(emitter.emit('onClick')); // Output: [99]

sub.unsubscribe(); // Unsubscribes the callback

console.log(emitter.emit('onClick')); // Output: []
