/**
 * Get a list of mesages whenever the Firestore db changes
 * @param {(messages:Array<object>) => null} onChange function(messages) to call when a change is detected in the Firestore db
 * @returns {null}
 */
function sendGetMessages(onChange) {
    // TODO (2): db.collection("messages").orderBy('timestamp', 'desc').onSnapshot((querySnapshot) => {}
    // TODO (3): Within the method, generate a list of messages from the querySnapshot
    // TODO (4): Call onChange() with the messages list passed as a parameter
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
    return null;
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