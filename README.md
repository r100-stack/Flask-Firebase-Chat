# Flask Firebase Chat

Today, almost all websites/apps provide dynamic content. This dynamic content could be inventory of products on sale, list of customers, orders, and more.

To maintain and provide this dynamic content, we need a database layer of some sort. To access this database layer easily, we would also need a backend layer as an abstraction.

Different database and backend solutions exist in the market today. In this exercise, we are going to talk about:

1. Flask (backend server) + MySQL (database server)
2. Firebase's Firestore (serverless backend and database)

You can see a demo of the finished exercise on [flaskchat.rohankadkol.com](https://flaskchat.rohankadkol.com)

Here is a screeshot of what we're going to build.

<img src="assets/flask_screenshot_1.gif">

## How to follow this repo

This repo is an exercise that is split into 10 steps. Each step is further split into starter and solution code branches. Each branch has a couple of ``TODOs``.

The recommended way to follow this repo is to complete each of the 10 steps in order. Also, it's recommended to complete the ``TODOs`` in each step in order.

The solutions to each ``TODO`` is provided in this ``README``. The solutions for each step is also available in the ``SolutionCode`` branch of that step. Eg. ``Step1-StarterCode`` contains all the incomplete TODOs for step 1 and ``Step1-SolutionCode`` contains the solution for each TODO in step 1.

## How to use git in this repo

To switch between branches, you can use the ``git``. You can either use the branch selector on the bottom left of VSCode or you can use some ``git`` commands in the terminal.

```bash
# To clone to repo
git clone https://github.com/rohan-kadkol/Flask-Firebase-Chat.git

# To list all branches
git branch -a

# To checkout a branch. Note, the branch will be downloaded if it doesn't exist locally
git checkout <branch name>
example,
git checkout Step1-StarterCode

# Save your work in a branch (This may be needed before switching to a new branch)
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

## Setup to follow this repo

We will be using MySQL as our backend. Hence, let us set it up for our app.

Requirements:

1. MySQL server
2. Credentials to access the MySQL server

### Option 1 (**Recommended**)

To save time and avoid setup errors, you can use this [pre-setup VM](https://drive.google.com/drive/folders/1AN_HY_vOSVv108QnYIhSHkFDQ-Z8mmYK?usp=sharing).

* VM login: ``kali``
* VM password: ``kali``
* MySQL username: ``user``
* MySQL password: ``password``

What does the VM contain?

* VSCode
    * Todo Tree extension
    * Python extension
    * and more...
* MySQL server
    * Running server
    * Credentials
* All required apt-get packages
* Firebase command line tool

### Option 2 (Manual setup)

Follow the below instructions on either your local or virtual machine. Choose the appropriate option depending on your OS.

* Windows: [Tutorial guide](https://www.liquidweb.com/kb/install-mysql-windows/)
* Linux: [Tutorial guide](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
* Mac: [Tutorial guide](https://www.positronx.io/how-to-install-mysql-on-mac-configure-mysql-in-terminal/)

___

To test if your MySQL server is working, type ``mysql`` in the command line. You might get an error similar to the one below

```
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
```

If you do get this error, you can start the server with this command

```bash
/etc/init.d/mysql start
```

If it asks for a password, enter the system password (``kali`` if you're using the [pre-setup VM](###option-1-(**recommended**)))

___

Once you have a **running** MySQL server along with **valid credentials**, we can setup our messages table in the database.

Run the below commands to setup the table.

```
mysql -u user -p
<Enter your MySQL password>
```

```
create database flaskchat;

use flaskchat;

create table messages (
    ID int auto_increment,
    message varchar(200),
    sender varchar(50),
    primary key (ID)
);
```

## Setting up Python dependencies

Regardless of where you're using the pre-setup VM or your local machine, we need to setup some Python dependencies.

Instead of installing these dependencies on your local system's Python installation, we will install it in a Python virtual environment. This increases modularity, prevents dependency version conflicts, and more.

```bash
# To create a virtual environment
python3 -m venv env

# To enter the created virtual environment
source env/bin/activate

# To exit the virtual environment
deactivate
```

If you see an (env) in the beginning of each command, you have successfully created and entered the Python virtual environment.

<img src="assets/python_venv_setup_editted.png">

All dependencies we need for this project are in ``requirements.txt``. To install it, run the following in the terminal **while entered in the Python virtual environment**.

```bash
pip install -r requirements.txt
```

# 1. Flask version

## Step 1: Setting up and starting the Flask server

To begin working on this step, switch to the ``Step1-StarterCode`` branch.

```bash
git checkout Step1-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step1-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_1.png">

___


Flask makes server setup very easy. With just a few lines of code, we can get a basic server up and running.

Let's start by doing some imports.

``init_flask.py``
```python
# TODO 1-2
from flask import Flask
from sqlalchemy import create_engine

# TODO 3
import os
```

Instead of hard coding our database's credentials, let us take it as an environment variable. Then the credentials can be dynamically entered through the command line. This increases flexibility and also more importantly increases security.

``init_flask.py``
```python
# TODO 4-5
username = os.environ['FLASKCHAT_DB_USERNAME']
password = os.environ['FLASKCHAT_DB_PASSWORD']
```

Now, let us create a definition of the Flask app. Here we can specify additional configurations for the Flask app. However, in our basic case, no additional configurations are needed.

``init_flask.py``
```python
# TODO 6
app = Flask(__name__)
```

To link our Flask server with our MySQL server, we need to create a URI that refers to the database. Then we need to create a database engine using this URI.

``init_flask.py``
```python
# TODO 7-8
DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user=username, password=password, server='localhost', database='flaskchat')

engine = create_engine(DATABSE_URI)
```

That is it for the Flask server setup! Now let's start working on our first endpoint.

Our first endpoint will be ``GET /``. This endpoint should return the ``index.html`` file in the ``/templates`` folder. The ``index.html`` file is in the ``/templates`` folder as Flask, by default, looks for ``html`` files in the ``/templates`` folder. Keeping it in any other folder and refering to it will give an error.

``app.py``
```python
# TODO 9-10
from flask import Flask, render_template
from init_flask import app

# TODO 11-13
@app.route('/', methods=['GET'])
def index():
    """GET / - Endpoint to display the homepage HTML file."""

    return render_template('index.html')
```

Now to run the server, head to the terminal and cd into the project directory. Next, let us setup some environment variables needed to configure Flask. Finally, we can run a simple command to start the Flask server.

```bash
# Required: To tell which is the main Flask file with all endpoints
export FLASK_APP=app.py

# Optional: To tell that this Flask server is not in development (non-production) mode. Hence, it will automatically reload the server when it detects changes.
export FLASK_ENV=development

# Required: MySQL db credentials used by init_flask.py
# MySQL db username
export FLASKCHAT_DB_USERNAME=user
# MySQL db password
export FLASKCHAT_DB_PASSWORD=password

# To start the Flask server
flask run
```

To test the server, open a browser and go to [localhost:5000](localhost:5000). You should now see an HTML page that says Flask Chat. Don't worry if you get an error saying "Error downloading messages". We will fix that in the later steps.

<img src="assets/step1_sol.png">

<!-- TODO***: Add a screenshot at the end of each step. -->

## Step 2: Creating a connection to the MySQL db

To begin working on this step, switch to the ``Step2-StarterCode`` branch.

```bash
git checkout Step2-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step2-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_2.png">

___


Programming is not only about getting the right output. It is also about robustness, efficiency, code structure and more. A common programming pattern to avoid bugs and improve readability is to create layers of abstractions. We're going to do the same.

Let us create a layer of abstraction that creates a database connection. This connection can then be used by any endpoint we implement in the future steps.

``error_handling.py``
```python
# TODO 1-3
conn = engine.connect()
response = func(conn=conn)
```

When there is no error, the try block executes completely. Hence, ``response = output of func``. However, when there is an error, we should return an HTTP response with code 500.

``error_handling.py``
```python
# TODO 4-5
response = jsonify({
    'success': False,
    'error': str(ex)
}), 500
```

Database connections must always be closed after its use. Reusing database connections and/or unclosed connections may cause problems down the line.

After closing the connection, we can return the response generated by either the try block (success, 200) or the catch block (failure, 500)

``error_handling.py``
```python
# TODO 6
conn.close()

# TODO 7
return response
```

This step was just a layer of abstraction. Hence, there won't be any visible change in website.

<img src="assets/step2_sol.png">

## Step 3: GET /messages

To begin working on this step, switch to the ``Step3-StarterCode`` branch.

```bash
git checkout Step3-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step3-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_3.png">

___


Time to create our second endpoint! We will now create a ``GET /messages`` endpoint to return all the messages in our db.

First let us do some imports.

``app.py``
```python
# TODO 1
from flask import Flask, jsonify, render_template

# TODO 2
from error_handling import get_connection_and_handle_error
```

Now, let us create the endpoint similar to step 1 (``GET /``).

Let us also include the ``@get_connection_and_handle_error`` decorator (layer of abstraction) that we created in step 2. This will give us a db connection that we can use to run SQL statements.

Define a function ``get_messages(*args, **kwargs)``.

``app.py``
```python
# TODO 3-5
@app.route('/messages', methods=['GET'])
@get_connection_and_handle_error
def get_messages(*args, **kwargs):
```

Then use ``**kwargs`` to get the db connection that ``@get_connection_and_handle_error`` provides.

Using the db conn, execute the following SQL statement.
```sql
select ID, message, sender from messages order by ID desc;
```

Iterate through all the records the above SQL statement returns to create a list of messages.

Finally, return an HTTP 200 response with ``success=True`` and the list of messages

``app.py``
```python
# TODO 6-10
def get_messages(*args, **kwargs):
    """GET /messages - Returns a JSON response with the messages in the database."""

    conn = kwargs['conn']
    results = conn.execute(
        'select ID, message, sender from messages order by ID desc;')

    messages = []

    for row in results:
        messages.append({
            'ID': row['ID'],
            'message': row['message'],
            'sender': row['sender']
        })

    return jsonify({
        'success': True,
        'messages': messages
    })
```

Now let's configure our frontend to make a request to the ``GET /messages`` endpoint of our backend.

``custom_ajax_flask.js``
```javascript
// TODO 11-16
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

// TODO 17-18
response = await sendAjaxRequest('/messages', 'GET', null);
    return response;
```

Sometimes a regular refresh using ``F5`` may not display any changes. Hence, do a hard refresh on your browser by pressing ``Ctrl+F5``.

You should now see some samples messages or no messages if no sample messages exist in the db. Regardless, you shouldn't see the error that we were seeing in steps 1 and 2.

<img src="assets/step3_sol.gif">

<!-- TODO***: Add sample messages to the MySQL db in the Kali VM -->

<!-- TODO***: Do we need a ___ after every step/section? -->

## Step 4: POST /messages

To begin working on this step, switch to the ``Step4-StarterCode`` branch.

```bash
git checkout Step4-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step4-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_4.png">

___


There's no fun in just seeing sample messages. Let us work on adding our own messages to the database.

Let us create a ``POST /messages`` endpoint (Similar to step 3), and use the ``@get_connection_and_handle_error`` to get a db connection.

The only difference is that our frontend now will send a the message and message sender along with the request. Hence, use ``request.json['key']`` to get the ``'message'`` and ``'sender'``.

Execute the following sql statement
```sql
insert into messages (message, sender) values (%s, %s);
```

Finally, return an HTTP 200 response with ``success=True``

``app.py``
```python
# TODO 1
from flask import Flask, jsonify, render_template, request

# TODO 2-8
@app.route('/messages', methods=['POST'])
@get_connection_and_handle_error
def add_message(*args, **kwargs):
    """POST /messages - Adds a message to the database."""

    conn = kwargs['conn']

    message = request.json['message']
    sender = request.json['sender']

    conn.execute(
        'insert into messages (message, sender) values (%s, %s);', (message, sender,))

    return jsonify({
        'success': True
    })
```

Now let's configure our frontend to make a request to the ``POST /messages`` endpoint of our backend.

``custom_ajax_flask.js``
```javascript
// TODO 9-10
response = await sendAjaxRequest('/messages', 'POST', {
    'message': message,
    'sender': sender
});
return response;
```

After doing a hard reload (``Ctrl+F5``), you can test adding a message. After clicking the ``Send`` button, you should see the message appear in the messages list.

<img src="assets/step4_sol.gif">

## Step 5: DELETE /messages

To begin working on this step, switch to the ``Step5-StarterCode`` branch.

```bash
git checkout Step5-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step5-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_5.png">

___


"Oops, I sent a message by accident. I want to delete it."

Let's now work on deleting a message.

First, create a ``DELETE /messages`` endpoint, use the ``@get_connection_and_handle_error`` decorator, and extract the provided connection using ``**kwargs``.

Next, use ``request`` to extract the ID of the message to delete.

Delete the message using the following SQL statement.

```sql
delete from messages where ID=%s;
```

Finally, return an HTTP 200 response with ``success=True``.

``app.py``
```python
# TODO 1-7
@app.route('/messages', methods=['DELETE'])
@get_connection_and_handle_error
def delete_message(*args, **kwargs):
    """DELETE /messages - Deletes a message from the database."""

    conn = kwargs['conn']

    ID = request.json['ID']

    conn.execute('delete from messages where ID=%s;', (ID,))

    return jsonify({
        'success': True
    })
```

Now let's configure our frontend to make a request to the ``DELETE /messages`` endpoint of our backend.

``custom_ajax_flask.js``
```javascript
// TODO 8-9
response = await sendAjaxRequest('/messages', 'DELETE', {
    'ID': ID
});
return response;
```

Now clicking the trash button on each message will delete the message.

<img src="assets/step5_sol.gif">

## Step 6: PATCH /messages

To begin working on this step, switch to the ``Step6-StarterCode`` branch.

```bash
git checkout Step6-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step6-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_6.png">

___


Made an embarassing typo? Let's implement the edit functionality so we correct that embarassing typo.

First, create a ``PATCH /messages`` endpoint, use the ``@get_connection_and_handle_error`` decorator, and extract the provided connection using ``**kwargs``.

Next, use ``request`` to extract the ID and message of the message to edit.

Edit the message using the following SQL statement.

```sql
update messages set message=%s where ID=%s;
```

Finally, return an HTTP 200 response with ``success=True``.

``app.py``
```python
# TODO 1-7
@app.route('/messages', methods=['PATCH'])
@get_connection_and_handle_error
def edit_message(*args, **kwargs):
    """PATCH /messages - Edits a message in the database."""

    conn = kwargs['conn']

    ID = request.json['ID']
    message = request.json['message']

    conn.execute('update messages set message=%s where ID=%s;', (message, ID,))

    return jsonify({
        'success': True
    })
```

Now let's configure our frontend to make a request to the ``PATCH /messages`` endpoint of our backend.

``custom_ajax_flask.js``
```javascript
// TODO 8-9
response = await sendAjaxRequest('/messages', 'PATCH', {
    'ID': ID,
    'message': message
});
return response;
```

<img src="assets/step6_sol.gif">

# 3. Firebase Version

The Flask version works well. It helps us read, add, delete, and update messages in the database. However, with the current implementation, there is one problem: the updates are not real-time.

For example, consider you have two clients using FlaskChat at the same time. When ``Client 1`` sends a message, ``Client 2`` doesn't see the new message instantly. ``Client 2`` only sees the new message on refreshing the page.

We can have the client send a ``GET /messages`` request every ~10 seconds. However, this is inefficient.

We can use some efficient methods like ``Web Sockets``, ``Streaming``, or some other similar methods to make our server real-time. However, these solutions might get complex. 

Making a database/backend real-time is very common. Then a question arrises on why should we implement it every time? What if it could be made as boilerplate code?

** Enters Firestore

[Firestore](https://firebase.google.com/docs/firestore) is a feature provided by a service called [Firebase](https://firebase.google.com/). Firestore is a NoSQL database that provides real-time implementation with almost no setup.

Benefits of Firestore:
* Real-time implementation already done
* Scalable: Firestore automatically scales depending on usage without any setup.
* Serverless: Deploying this db requires no VMs, Kubernetes, etc.

Looking at the benefits Firestore has to offer, we will now implement our getting, adding, deleting, and updating of messages using Firestore instead of Flask.

## Firebase setup

### Option 1: Use pre-setup Firebase config

**If you want to use Firebase hosting, you'll need your own Firebase project. Hence, follow option 2 below**

To save time, you can use the pre-setup configuration. We have created a Firebase project called ``Flask Chat`` with Project ID: ``flaskchat-6684a``.

Below is the ``var firebaseConfig`` needed to configure Firebase

```javascript
var firebaseConfig = {
    apiKey: "AIzaSyAW2ELiIJpHrkU40So9iOqePeGBcgfOB-E",
    authDomain: "flaskchat-6684a.firebaseapp.com",
    databaseURL: "https://flaskchat-6684a.firebaseio.com",
    projectId: "flaskchat-6684a",
    storageBucket: "flaskchat-6684a.appspot.com",
    messagingSenderId: "94841685089",
    appId: "1:94841685089:web:f1abf658720a87403cd620",
    measurementId: "G-FWENEM06PJ"
};
```

### Option 2: Setup a new Firebase project

Instead of using the pre-setup Firebase project in option 1, you can setup your own Firebase project.

1. Head to [console.firebase.google.com](https://console.firebase.google.com)
2. Click on "Add Project" or something similar
3. Enter a project name of your choice
<img src="assets/firebase_create_project.png">
4. Choose whether you want to enable Firebase analytics
<img src="assets/firebase_create_project_2.png">
5. Choose or create a Google Analytics account (only if Firebase analytics is chosen)
<img src="assets/firebase_create_project_3.png">
6. Click on continue when your project setup is ready
<img src="assets/firebase_create_project_4.png">
7. On the dashboard, click the ``</>`` icon near ``Get started by adding Firebase to your app``. This will register a Firebase web app to the Firebase project
<img src="assets/firebase_register_web_app.png">
8. Choose an app name of your liking
<img src="assets/firebase_register_web_app_2.png">
9. Copy only the definition of ``var firebaseConfig``. This is the ``firebaseConfig`` variable that points to your Firebase Project.
<img src="assets/firebase_register_web_app_3.png">

Your ``var firebaseConfig`` should look similar to the ``var firebaseConfig`` above.

## Step 7: Firebase setup and GET messages

<!-- TODO***: Include Firebase setup screenshots -->
<!-- TODO***: Include Firebase setup instructions -->

To begin working on this step, switch to the ``Step7-StarterCode`` branch.

```bash
git checkout Step7-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step7-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_7.png">

___


Now that we have ``var firebaseConfig`` pointing to either the pre-setup Firebase project or your own Firebase project, we can paste it in our project.

Below is the configuration code for that project. It contains:
* Firebase Project config (``var firebaseConfig``) obtained from above
* Firebase dependencies
    * Firebase app
    * Firebase analytics
    * Firebase firestore
* Initialize
    * Firebase app
    * Firebase analytics

**Be sure to replace the below ``var firebaseConfig`` with your own if you are using your own Firebase Project and not the pre-setup one.**

Paste the below code for TODO 1.

``/frontend/index.html``
```html
<!-- TODO 1 -->

<!-- 4. All Firebase/Firestore dependencies -->
<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/8.0.2/firebase-app.js"></script>

<!-- Dependency to analysize # visitors and other analytical data -->
<script src="https://www.gstatic.com/firebasejs/8.0.2/firebase-analytics.js"></script>

<!-- Dependency to use Firestore in your project -->
<script src="https://www.gstatic.com/firebasejs/8.0.2/firebase-firestore.js"></script>

<script>
    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    
    // TODO: Replace with your own firebaseConfig if you are using your own Firebase Project and not the pre-setup one
    
    var firebaseConfig = {
        apiKey: "AIzaSyAW2ELiIJpHrkU40So9iOqePeGBcgfOB-E",
        authDomain: "flaskchat-6684a.firebaseapp.com",
        databaseURL: "https://flaskchat-6684a.firebaseio.com",
        projectId: "flaskchat-6684a",
        storageBucket: "flaskchat-6684a.appspot.com",
        messagingSenderId: "94841685089",
        appId: "1:94841685089:web:f1abf658720a87403cd620",
        measurementId: "G-FWENEM06PJ"
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    firebase.analytics();

    var db = firebase.firestore();
</script>
<!-- End of Firebase/Firestore dependencies -->
```
___

Now that Firebase is set up, we can work on getting the messages.

Now, to get the messages, all we have to do is subscribe as a listener. We would also need to provide a callback to be executed when changes in the Firestore db are detected. This is what makes the Firestore db to be real-time.

On Firebase, data is stored in ``collections``. Each collection has ``documents``. Each document is a set of ``key-value pairs``. Apart from documents, collections can also hold more collections called ``sub-collections``. This enables Firestore to store data in a hierarchical fashion.

Here's an example of how data is stored
<!-- TODO***: Complete the above description of the below example -->
<!-- TODO***: Add screenshot of example -->
<img src="assets/firestore_structure_example.png">

We are going to have a collection called `messages`. In this ``messages`` collection, each document will be a message. Each document (message) will have three fields: message, sender, and timestamp.

<!-- TODO***: Insert example of our Firestore db structure -->

Now that we have planned the structure of our Firestore db, let us work on getting the messages. 

First, use ``db`` and call ``.collection('messages')`` on it. To sort the messages by descending timestamps, simply call ``.orderBy('timestamp', 'desc')`` to the chain.

Finally to subscribe as a listener and add a callback, add a ``.onSnapshot((querySnapshot) {})`` to the chain. Here, querySnapshot is a snapshot of all documents (messages) in the ``messages`` collection.

Within the curly braces of the callback function, create a list of messages by iterating through the ``querySnapshot``.

Then call ``onChange(messages)`` and pass the list of messages as a parameter. Here, ``onChange(messages)`` is a frontend method that displays the passed list of messages to the UI.

<!-- TODO***: Make sure everything that requires ```` is within it. -->

``custom_ajax_firebase.js``
```javascript
// TODO 2-4
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
```

To test the website, you will have to open the ``index.html`` file and not ``localhost:5000``. This is because in our new version, the javascript in the HTML page directly sends requests to the Firestore backend db. There is no intermidiate server as in the case of the Flask implementation.

Hence, type the path to the file in the browser. It should look something similar to,
```
/home/rohan/Documents/Flask-Firebase-Chat/frontend/index.html
```

<img src="assets/step7_sol.gif">

## Step 8: Sending a message

To begin working on this step, switch to the ``Step8-StarterCode`` branch.

```bash
git checkout Step8-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step8-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_8.png">

___


Adding a document to the Firestore db is as easy as doing a ``.add()`` call to the ``db.collection()`` and passing the JSON object to add as a parameter to ``.add()``.

We can use ``.then(function() {})`` and ``.catch(function(error) {})`` to execute code on success and on failure respectively.

Additionally, we wrap the ``.add()`` call in a ``Promise``. We do this so the frontend calling this method can use ``await`` to halt execution until a response is received.

``custom_ajax_firebase.js``
```javascript
// TODO 1-6
async function sendPostMessage(message, sender) {
    return new Promise(async resolve => {
        await db.collection("messages").add({
            message: message,
            sender: sender,
            timestamp: firebase.firestore.Timestamp.now()
        })
            .then(function () {
                console.log('insert successful');
                resolve({ 'success': true });
            })
            .catch(function (error) {
                console.log(error);
                resolve({ 'success': false });
            });
    });
}
```

<img src="assets/step8_sol.gif">

## Step 9: Deleting a message

To begin working on this step, switch to the ``Step9-StarterCode`` branch.

```bash
git checkout Step9-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step9-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_9.png">

___


To delete a document, we first need a reference to it. Each document is given a unique ID by Firebase. Hence, to get a reference to a document, we can do ``db.collection('messages').doc(ID)``, where ID is the id of the document.

Once we have a reference to the document, we can call a ``.delete()`` on it.

Additionally, we use a ``.then(function() {})`` and ``.catch(function(error) {})`` to execute code on success and on failure respectively.

``custom_ajax_firebase.js``
```javascript
// TODO 1-5
async function sendDeleteMessage(ID) {
    return new Promise(async resolve => {
        await db.collection("messages").doc(ID).delete()
            .then(function () {
                console.log('delete successful');
                resolve({ 'success': true });
            })
            .catch(function (error) {
                console.log(error);
                resolve({ 'success': false });
            });
    });
}
```

<img src="assets/step9_sol.gif">

## Step 10: Editing a message

To begin working on this step, switch to the ``Step10-StarterCode`` branch.

```bash
git checkout Step10-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step10-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_10.png">

___


To edit a message, we can call ``onUpdate()`` on the reference to the document to edit. We can then pass the parameters to update in a JSON object passed to ``onUpdate()``. In our case, message is the only parameter of a document that we want to edit.

Additionally, we use a ``.then(function() {})`` and ``.catch(function(error) {})`` to execute code on success and on failure respectively.

``custom_ajax_firebase.js``
```javascript
// TODO 1-6
async function sendPatchMessage(ID, message) {
    return new Promise(async resolve => {
        await db.collection("messages").doc(ID).update({
            message: message
        })
            .then(function () {
                console.log('update successful');
                resolve({ 'success': true });
            })
            .catch(function (error) {
                console.log(error);
                resolve({ 'success': false });
            });
    });
}
```

<img src="assets/step10_sol.gif">

# 4. Firebase Hosting

## Step 11: Hosting the Firebase version of the website with Firebase Hosting

To begin working on this step, switch to the ``Step11-StarterCode`` branch.

```bash
git checkout Step11-StarterCode
```

If you get an error, you might have to save the changes before running the above checkout command. Hence, save your changes using the below command.

```bash
git add .
git commit -m "xyz"
# Here xyz is any message describing the work you've done in the commit
```

Before continuing, confirm you are in the ``Step11-StarterCode`` branch by looking at the bottom left of VS Code.

<img src="assets/vscode_git_branch_11.png">

___


In order to host the Flask version of our website, we would need to host it on a VM or something similar. Hence, we would need to manage scalability, maintainance, and more.

However, with Firebase Hosting, we can simply host the website on a serverless model. Firebase Hosting then automatially handles the scaling and maintainance behind the scenes.

Let us host our Firebase version of our app with Firebase Hosting.

1. Open a terminal in the project folder
2. Install the Firebase command line tools (skip if using pre-setup VM or if already installed).

```bash
npm install -g firebase-tools
```

3. Login to Firebase

```bash
firebase login
```

4. Initialize the project directory as a Firebase project

```bash
firebase init
```

5. From the list of which features we want to set up, choose hosting using ``Space`` and confirm your selection with ``Enter``

<img src="assets/firebase_hosting.png">

6. If you have already created a Firebase Project ( [Firebase Setup, Option #2 above](###option-2:-setup-a-new-firebase-project) ), choose ``Use an existing project`` and choose the created project. If you haven't created a new Firebase project, you can create one by following [these instructions](###option-2:-setup-a-new-firebase-project).

<img src="assets/firebase_hosting_2.png">

7. For the public directory, choose ``frontend`` as all our frontend resources that we want to host is in the ``/frontend`` folder.

8. As our website just has one webpage, configure it as a single page app. This redirects all other paths to the home page. ie. ``/`` and ``/abc`` route to the same HTML page: ``/frontend/index.html``.

9. For our example, we will choose not to set up automatic builds with GitHub. However, you can select this option for your future projects to speed up the time between commiting your changes and seeing them appear on the hosted platform.

10. Since we have already created our ``index.html`` file, we will not need the default ``index.html`` file. Hence, we don't need to overwrite our existing ``index.html`` file with the default one.

<img src="assets/firebase_hosting_3.png">
<img src="assets/firebase_hosting_4.png">

11. Now, to host the website, simply use use the below command.

```bash
firebase deploy
```

<img src="assets/firebase_hosting_5.png">

Now you can use the public url instead of the path to the local ``index.html`` file to access the website.

Your public URL will be something similar to:

```
flaskchat-6684a.web.app
```

<img src="assets/step11_sol.gif">

# Conclusion

That's all we have in our exercise. Congratulations on making it till the end! By following this exercise, you have some basic understanding of:

* Flask servers
* Integrating Flask with MySQL
* Firebase Firestore backend
* Firebase Hosting

I hope you enjoyed this exercise and benefitted from it.

Geaux Tigers! 🐯