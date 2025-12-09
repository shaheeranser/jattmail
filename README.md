# Jatt Mail
Python based opensource SMTP server. Developed for a secure SMTP communication available of all platforms.

### Project Structure
```
/
|---jattmail/         # Project package
|   |---__init__.py   # Project initializer
|   |---connection.py # Temporary class
|   |---logs.py       # Handle logs
|   |---settings.py   # Basic configuration
|---test/             # Testing purpose
|   |---client.py     # SMTP client
|---.gitignore        # Git ignore
|---README.md         # Description
|---main.py           # Entry point
|---stop.py           # Stops the server
|---logs.txt          # Default log file
```

### Exmple of TLS Encrypted Session
```
Client: [Connects to port 587]
Server: 220 smtp.gmail.com ESMTP

Client: EHLO client.example.com
Server: 250-smtp.gmail.com at your service
Server: 250-SIZE 35882577
Server: 250-8BITMIME
Server: 250-AUTH LOGIN PLAIN XOAUTH2
Server: 250-ENHANCEDSTATUSCODES
Server: 250-PIPELINING
Server: 250-CHUNKING
Server: 250 SMTPUTF8

Client: STARTTLS
Server: 220 2.0.0 Ready to start TLS

[TLS Handshake occurs here]

Client: EHLO client.example.com (again, over TLS)
Server: 250-smtp.gmail.com at your service
Server: 250-SIZE 35882577
Server: 250-8BITMIME
Server: 250-AUTH LOGIN PLAIN XOAUTH2
Server: 250-ENHANCEDSTATUSCODES
Server: 250-PIPELINING
Server: 250-CHUNKING
Server: 250 SMTPUTF8

Client: AUTH LOGIN
Server: 334 VXNlcm5hbWU6
Client: YWxpY2VAZ21haWwuY29t
Server: 334 UGFzc3dvcmQ6
Client: c2VjcmV0MTIz
Server: 235 2.7.0 Accepted

Client: MAIL FROM:<alice@gmail.com>
Server: 250 2.1.0 OK

Client: RCPT TO:<bob@gmail.com>
Server: 250 2.1.5 OK

Client: DATA
Server: 354 Go ahead

[Email headers and body]
Client: .
Server: 250 2.0.0 OK 1234567890

Client: QUIT
Server: 221 2.0.0 closing connection
```