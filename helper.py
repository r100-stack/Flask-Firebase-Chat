def get_json_from_results(results):
    messages = []
    for row in results:
        messages.append({
            'id': row['id'],
            'message': row['message'],
            'sender': row['sender']
        })
    return messages;