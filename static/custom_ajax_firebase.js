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
// TODO: Need to update docs and add more meaningful docs
async function sendPostMessage(message, sender) {
    return new Promise(async resolve => {
        await db.collection("messages").add({
            message: message,
            sender: sender,
            timestamp: firebase.firestore.Timestamp.now()
        })
        .then(function() {
            console.log('insert successful');
            resolve({'success': true});
        })
        .catch(function(error) {
            console.log(error);
            resolve({'success': false});
        });
    });
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