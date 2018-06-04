########################################################################################
#                                                                                      #
#                       SERVICE FOR SHADOW SUITE FRAMEWORK                             #
#                                                                                      #
########################################################################################
# Coding=UTF-8

service_version = 1.0

# Import directives
try:
    import os
    import sys
    import traceback
    from core import misc
    from core import error
    from core.logger import log
    from core import multitasking
    import API

    # Place your 'import' directives below
    import socket
    import select

    import_error = False

except(ImportError, ModuleNotFoundError):
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your service information here.
info = {
        "name": "simpleIM Chat Server", # Service filename (Change this; I recommend you to use the filename as the service name.)
        "version": "1.0", # version
        "author": "Catayao56", # Author
        "desc": "SimpleIM service for setting up a server.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56", # Additional information about the author; this could be
        "lastupdate": "Jun. 02, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this service using Shadow Suite's API?
        "needsroot": "1", # Does this service needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = [] # Put needed dependencies here.
service_status = 1 # 0  == Stable, 1 == Experimental, 2 == Unstable, 3 == WIP
#files = [] # Uncomment this line if the service needs a subdirectory to use.
#E.g.: SERVICE_NAME_OR_SUBDIRECTORY_NAME/

# Changelog of the service
changelog = "Version 1.0:\nInitial servicee release"
# Changelog format:
#
# changelog = "Version 2.0:\nUpdate Description\n\nVersion1.0\nInitial service release"

global HOST
global SOCKET_LIST
global RECV_BUFFER
global PORT

# Prints the service information
def service_info():
    # Unofficial way to convert integer to Boolean
    # (well, not really a boolean, as it is a string).
    # if [argument] == 0 then True; Otherwise, False.
    if info['needsroot'] == "0":
        superm = "True"
    else:
        superm = "False"

    print("Service Name: " + info['name'])
    print("Service Version: " + info['version'])
    print("Service Author: " + info['author'])
    print("Service Description: " + info['desc'])
    print()
    print("Service Author's Email: " + info['email'])
    print("Service Author's Info: " + info['authorinfo'])
    print("Service's last update: " + info['lastupdate'])
    print("Shadow Suite API Support: " + info['usingapi'])
    print("Needs root: " + superm)
    print()
    # Prints the dependencies via for loop. I just copy/pasted it from a reference book
    # and modified it XD
    print("Dependencies:", end=' ')
    for item in dependencies:
        print(item, ",", end=' ')
    print()
    # Prints the changelog of the service.
    print("Changelog:\n" + "\n" + changelog)
    print("\n\n")

# Main service function
def main(global_variables):
    if import_error is True:
        return None

    else:
        """ First, it checks the value assigned to the 'needsroot' variable in the 
        dictionary 'info', then if the value is equal to zero, it calls the 'geteuid()'
        function from the 'os' module. If the result from geteuid is also zero, then
        the module will call the function 'service_body()'. Otherwise, it will print an
        error message. If the value assigned to the 'needsroot' variable in the dictionary
        'info' is not equal to zero, then the module will not call the 'geteuid()' function
        from the 'os' module, and will immediately call 'service_body()' function. """
        if info['needsroot'] == "0":
            if os.geteuid() != 0:
                print(error.errorCodes().ERROR0005)
                return 0

            else:
                multitasking.set_engine("process")
                service_body(global_variables)

        else:
            multitasking.set_engine("process")
            service_body(global_variables)

def stop_service():
    multitasking.killall('', '')

@multitasking.task
def service_body(global_variables):
    # To support module versions older than v7.0
    # Remember, services and modules use the same API!
    API_ShadowSuite = API.ShadowSuite(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], global_variables['DEBUGGING'])
    
    r"""
    Chat Server
    In this chapter, we'll make a chat server. The server is like a middle
    man among clients. It can queue up to 10 clients. The server broadcasts
    any messages from a client to the other participants. So, the server
    provides a sort of chatting room.
    
    In this chat code, the server is handling the sockets in non-blocking
    mode using select.select() method:
    
    ready_to_read, ready_to_write, in_error = \
            select.select(
            potential_readers,
            potential_writers,
            potential_errs,
            timeout)
            
    We pass select() three lists:

    the first contains all sockets that we might want to try reading
    the second all the sockets we might want to try writing to
    the last (normally left empty) those that we want to check for errors
    Though the select() itself is a blocking call (it's waiting for I/O
    completion), we can give it a timeout. In the code, we set time_out = 0,
    and it will poll and never block.

    Actually, the select() function monitors all the client sockets and the
    server socket for readable activity. If any of the client socket is
    readable then it means that one of the chat client has send a message.

    When the select function returns, the ready_to_read will be filled with
    an array consisting of all socket descriptors that are readable.
    
    In the code, we're dealing with two cases:
    
    If the master socket is readable, the server would accept the new connection.
    If any of the client socket is readable, the server would read the message,
    and broadcast it back to all clients except the one who send the message.
    """
    global HOST
    global SOCKET_LIST
    global RECV_BUFFER
    global PORT

    HOST = '' 
    SOCKET_LIST = []
    RECV_BUFFER = 4096 
    PORT = 9009
    chat_server()

def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print(misc.CGR +"[" + info['name'] + "] Chat server started on port " + str(PORT) + misc.END)
 
    while True:

        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print("Client (%s, %s) connected" % addr)
                 
                broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
             
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                try:
                    # receiving data from the socket.
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # there is something in the socket
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        # remove the socket that's broken    
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()
    
# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)

            except :
               # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
