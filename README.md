# Baabocrypt Blowfish Symmetrical Encryption Chat

This was a small example I wanted to try out to see if a symmetrical communication tool over websocket works

----

## Technologies

In this project, the following are utilized

- **Flask**: Flask is a lightweight web framework for Python that allows us to build web applications easily and efficiently.

- **Flask-SocketIO**: Flask-SocketIO is an extension for Flask that enables real-time, bidirectional communication between the web server and the client using WebSockets.

- **CryptoJS**: CryptoJS is a JavaScript library that provides various cryptographic algorithms, including encryption and decryption functions. We can use CryptoJS to securely encrypt and decrypt data in the browser.

By combining Flask, Flask-SocketIO, and CryptoJS, we can create a secure and real-time communication tool over websockets, ensuring the confidentiality and integrity of the transmitted data.

## How does it work?

Encryption is done client-sided through said CryptoJS library. The encrypted messages are sent over the websocket.
The access keys (or defined "key" within blowfish) is also used client-sided. This means that encryption and decryption all happen client-sided.
The only thing the server gets is the encrypted message, broadcasted to everyone, and decryption will only happen to the clients where this decryption is valid.


## Screenshots

The use of the tool

![Example Screenshot](/repo-content/application-example.gif)

What the console sees

![Example Screenshot](/repo-content/screenshot-console.png)