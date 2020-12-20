/**
 * Get a list of mesages whenever the Firestore db changes
 * @param {(messages:Array<object>) => null} onChange function(messages) to call when a change is detected in the Firestore db
 * @returns {null}
 */
function sendGetMessages(onChange) {
    db.collection("messages").orderBy('timestamp', 'desc').onSnapshot((querySnapshot) => {
        var messages = [];

        querySnapshot.forEach((doc) => {
            messages.push({
                'ID': doc.id,
                'message': doc.data()['message'],
                'sender': doc.data()['sender']
            });
        });

        onChange(messages);
    });
}

/**
 * Add a message to Firestore
 * @param {string} message contents of the message to add
 * @param {string} sender sender of the message
 * @returns {Promise<object>} JSON object with a success param
 */
async function sendPostMessage(message, sender) {
    return new Promise(async resolve => {
        // TODO (1): db.collection.add()
        // TODO (2): Pass the following as a parameter to add: {message: message, sender: sender, timestamp: firebase.firestore.Timestamp.now()}
        // TODO (3): .add({}).then(function () {})
        // TODO (4): Within the function, resolve({ 'success': true });
        // TODO (5): .add({}).then(function () {}) .catch(function(error) {})
        // TODO (6): Within the function, resolve({ 'success': false });
    });
}

/**
 * Delete a message from Firestore
 * @param {number} ID ID of the message to delete
 * @returns {Promise<object>} JSON object with a success param
 */
async function sendDeleteMessage(ID) {
    return null;
}

/**
 * Update a message on Firestore
 * @param {number} ID ID of the message to update
 * @param {string} message new message
 * @returns {Promise<object>} JSON object with a success param
 */
async function sendPatchMessage(ID, message) {
    return null;
}