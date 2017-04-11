#!/usr/bin/env python
from socket import socket, AF_INET, SOCK_STREAM


def receive_all_until(sock_fd, msg_end):
    data = ""
    while not data.endswith(msg_end):
        data = data + sock_fd.recv(1)
    print data


ADDRESS = "212.182.24.27"
PORT = 143
EMAIL = "pasumcs@infumcs.edu"
PASSWORD = "P4SInf2017"
CRLF = "\r\n"

SERVER_ADDRESS = (ADDRESS, PORT)
sock = socket(AF_INET, SOCK_STREAM)

sock.connect(SERVER_ADDRESS)
receive_all_until(sock, CRLF)

MSG_LOGIN_TAG = "T0"
MSG_LOGIN = MSG_LOGIN_TAG + " LOGIN " + EMAIL + " " + PASSWORD + CRLF
sock.sendall(MSG_LOGIN)
receive_all_until(sock, MSG_LOGIN_TAG)

MSG_SELECT_TAG = "T1"
MSG_SELECT = MSG_SELECT_TAG + " SELECT Inbox" + CRLF
sock.sendall(MSG_SELECT)
receive_all_until(sock, MSG_SELECT_TAG)

MSG_FETCH_TAG = "T2"
MSG_FETCH = MSG_FETCH_TAG + " FETCH 1 BODY[]" + CRLF
sock.sendall(MSG_FETCH)
receive_all_until(sock, MSG_FETCH_TAG)

MSG_CLOSE_TAG = "T3"
MSG_CLOSE = MSG_CLOSE_TAG + " CLOSE" + CRLF
sock.sendall(MSG_CLOSE)
receive_all_until(sock, MSG_CLOSE_TAG)

MSG_LOGOUT_TAG = "T4"
MSG_LOGOUT = MSG_LOGOUT_TAG + " LOGOUT" + CRLF
sock.sendall(MSG_LOGOUT)
receive_all_until(sock, MSG_LOGOUT_TAG)
