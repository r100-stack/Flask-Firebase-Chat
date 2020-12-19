/**
 * Sends an ajax request of the specified type to the specified url and with the specified body
 * @param {string} url url of where to send the request to
 * @param {string} type type of the request. Eg. GET, POST, PATCH, DELETE
 * @param {string|object} body body of the request. Eg. {"ID": 5} to delete the message with ID=5
 * @returns {Promise<object>} A promise containing messages
 */
function sendAjaxRequest(url, type, body) {
    return new Promise(resolve => {
        try {
            resolve(null);
        } catch (error) {
            console.log(error);
        }
    });
}

/**
 * Send a GET /messages request to get all the messages in the database
 * @returns {object} messages as a JSON array of JSON objects (messages)
 */
async function sendGetMessages() {
    return null;
}

/**
 * Send a POST /messages request to add a message to the database
 * @param {string} message message to insert in the database
 * @param {string} sender sender of the message
 * @returns {object} JSON object with a success param
 */
async function sendPostMessage(message, sender) {
    return null;
}

/**
 * Send a DELETE /messages request to delete a message from the database
 * @param {number} ID ID of the message to delete
 * @returns {object} JSON object with a success param
 */
async function sendDeleteMessage(ID) {
    return null;
}

/**
 * Send a PATCH /messages request to update a message in the database
 * @param {number} ID ID of the message to update
 * @param {string} message new message
 * @returns {object} JSON object with a success param
 */
async function sendPatchMessage(ID, message) {
    return null;
}