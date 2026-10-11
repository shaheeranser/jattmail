# jattmail

A Python-based SMTP server (early-stage). It opens a TCP socket, accepts connections, and logs the data clients send; a control command shuts it down remotely.

> **Status:** early prototype — the server currently accepts connections and logs traffic; full SMTP command handling (and TLS) is not yet implemented.

## Requirements

- Python 3.10+

## Getting started

```bash
python main.py
```

Starts the server on the address/port defined in `jattmail/settings.py` (default `127.0.0.1:2500`).

Stop it with:

```bash
python stop.py
```

which connects to the running server and sends the break command.

## Configuration

Edit `jattmail/settings.py`:

| Setting | Default | Description |
| --- | --- | --- |
| `ADDRESS` | `127.0.0.1` | Bind address (`0.0.0.0` for all interfaces) |
| `PORT` | `2500` | Listen port (25 is the standard SMTP port) |
| `CONNECTIONS` | `5` | Backlog / simultaneous connections |
| `TIMEOUT` | `0.1` | Socket timeout (seconds) |
| `LOG_ECHO` | `True` | Print logs to the console |
| `LOG_WRITE` | `True` | Write logs to a file |
| `LOG_FILE` | `logs.txt` | Log file name |
| `BREAK` | `exit()` | Message that stops the server |

## Project structure

```
/
|---jattmail/         # Project package
|   |---__init__.py   # Server class (JattMail)
|   |---connection.py # Connection bookkeeping
|   |---logs.py       # Logging
|   |---settings.py   # Configuration
|---test/             # Testing
|   |---client.py     # Sample smtplib client
|---.gitignore        # Git ignore
|---README.md         # Description
|---main.py           # Entry point
|---stop.py           # Stops the server
|---logs.txt          # Default log file
```

## Test client

`test/client.py` is a sample `smtplib` client pointed at `127.0.0.1:2500`.

## Example: TLS-encrypted SMTP session (reference)

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
