function sendAjaxRequest(url, type, body) {
    return new Promise(resolve => {
        try {
            $.ajax({
                url: url,
                type: type,
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(body),
                complete: function (response) {
                    console.log(response.responseJSON);
                    resolve(response.responseJSON);
                }
            });   
        } catch (error) {
            console.log(error);
        }
    });
}

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
 * Send a POST /messages request to add a message to the database
 */
async function sendPostMessage(message, sender) {
    response = await sendAjaxRequest('/messages', 'POST', {
        'message': message,
        'sender': sender
    });
    return response;
}

async function sendDeleteMessage(ID) {
    response = await sendAjaxRequest('/messages', 'DELETE', {
        'ID': ID
    });
    return response;
}

async function sendPatchMessage(ID, message) {
    response = await sendAjaxRequest('/messages', 'PATCH', {
        'ID': ID,
        'message': message
    });
    return response;
}