#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', 8080))          # Bind local host and port # to socket
serverSocket.listen(1)                          # Queue size of the # of request to wait for

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        rawData = connectionSocket.recv(1024)   # Receiving raw bytes
        message = rawData.decode()              # Decoding the bytes into a string
        filename = message.split()[1]           # Splitting the message
        f = open(filename[1:])                  # Opening the file with the message in it

        outputdata =f.read()                    # Read the contents of the file

        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client

        # Uncomment the for loop when we have the connection socket code ready

        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i].encode())
        #     connectionSocket.send("\r\n".encode())
        #     connectionSocket.close()



    except IOError:
        pass
        #Send response message for file not found
        #Fill in start
        #Fill in end
        #Close client socket
        #Fill in start
        #Fill in end

    serverSocket.close()
    sys.exit() #Terminate the program after sending the corresponding data