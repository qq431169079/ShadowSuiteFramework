import sys
import socket
import select
 
def chat_client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    # connect to remote host
    try :
        s.connect((host, port))

    except :
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host. You can start sending messages')
    sys.stdout.write('[Me] '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print('\nDisconnected from chat server')
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()     
            
            else :
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush() 

if __name__ == "__main__":
    sys.exit(chat_client())

"""
The client code does either listen to incoming messages from the server or check user input. If the user types in a message then send it to the server.

We use select() function to handle both messages: one from stdin which is a user input and the other from the server. As we recall, the server side usage which is a non-blocking mode, we don't do anything on the select() function, and we use it as blocking mode. So, the select() function blocks (waits) till something happens. It will return only when either the server socket receives a message or the user enters a message.
"""

"""
Run the code
We should run the server first:

$ python chat_server.py
Chat server started on port 9009
Then, the client code:

$ python chat_client.py localhost 9009
Connected to remote host. You can start sending messages
Note that the client should use the same port number as the server does.

Here are the output from a sample run:

// server terminal
$ python chat_server.py
Chat server started on port 9009
Client (127.0.0.1, 48952) connected
Client (127.0.0.1, 48953) connected
Client (127.0.0.1, 48954) connected


// client 1 terminal
$ python chat_client.py localhost 9009
Connected to remote host. You can start sending messages
[Me] [127.0.0.1:48953] entered our chatting room
[Me] [127.0.0.1:48954] entered our chatting room
[Me] client 1
[('127.0.0.1', 48953)] client 2
[('127.0.0.1', 48954)] client 3
[Me] Client (127.0.0.1, 48954) is offline
[Me] 


// client 2 terminal
$ python chat_client.py localhost 9009
Connected to remote host. You can start sending messages
[Me] [127.0.0.1:48953] entered our chatting room
[Me] [127.0.0.1:48954] entered our chatting room
[Me] client 1
[('127.0.0.1', 48953)] client 2
[('127.0.0.1', 48954)] client 3
[Me] Client (127.0.0.1, 48954) is offline
[Me] 

// client 3 terminal
$ python chat_client.py localhost 9009
Connected to remote host. You can start sending messages
[('127.0.0.1', 48952)] client 1
[('127.0.0.1', 48953)] client 2
[Me] client 3
[Me] ^CTraceback (most recent call last):
  File "chat_client.py", line 52, in 
    sys.exit(chat_client())
  File "chat_client.py", line 30, in chat_client
    read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
KeyboardInterrupt
Note that the client #3 did go off the line at the end by typing ^C
"""
