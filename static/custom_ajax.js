function sendAjaxRequest(url, type, body) {
    return new Promise(resolve => {
        $.ajax({
            url: url,
            type: type,
            headers: { 'Content-Type': 'application/json' },
            data: JSON.stringify(body),
            async: true,
            success: function (response) {
                resolve(response);
            }
        });
    });
}

async function sendGetMessages() {
    response = await sendAjaxRequest('/messages', 'GET', null);
    return response;
}

/**
 * Send a POST /messages request to add a message to the database
 */
async function sendPostMessage(message, sender) {
    response = await sendAjaxRequest('/messages', 'POST', {
        'message': message,
        'sender': sender
    });
    return response;
}