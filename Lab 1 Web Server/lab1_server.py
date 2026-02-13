#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', 8080))                  # Bind local host and port # to socket
serverSocket.listen(1)                                  # Queue size of the # of request to wait for

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        rawData = connectionSocket.recv(1024)           # Receiving raw bytes

        # If rawData is empty we need to continue to prevent a crash.
        if len(rawData) == 0:
            connectionSocket.close()
            continue

        message = rawData.decode()                      # Decoding the bytes into a string
        filename = message.split()[1]                   # Splitting the message
        f = open(filename[1:])                          # Opening the file with the message in it

        outputdata = f.read()                           # Read the contents of the file

        response = "HTTP/1.1 200 OK\r\n\r\n"            # server response message back to user
        connectionSocket.send(response.encode())        # encoding the response message into bytes to send to user

        # Sending the message character by character to the user
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())          # End of message
        f.close()                                       # Closing file
        connectionSocket.close()                        # Closing socket connection

    except IOError:

        response = "HTTP/1.1 404 Not Found\r\n\r\n"     # Send response message for file not found
        connectionSocket.send(response.encode())        # Encode and send response message
        connectionSocket.close()                        # Close client socket



serverSocket.close()
sys.exit()                                              #Terminate the program after sending the corresponding data