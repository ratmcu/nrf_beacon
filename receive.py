from multiprocessing.connection import Listener

# client
def child(conn):
    while (True):
        try:
            msg = conn.recv()
        except:
            break
        # this just echos the value back, replace with your custom logic
        conn.send(msg)

# server
def mother(address):
    serv = Listener(address)
    while (True):
        client = serv.accept()
        child(client)

mother(('', 5023))
