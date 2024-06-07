#client side chat (New)
import socket, threading
des_ip='127.0.0.1'
des_port=11336
encoder="utf-8"
byte_size=1024

def listen_to_server_mg(client, myname):
    while True:
        messege=client.recv(2048).decode(encoder)
        if messege !="":
            username=messege.split('>')[0]
            content=messege.split('>')[1]
            if username != myname:
                print(f"{username}> {content}")
            else:
                pass
        else:
            print("Exit from the chat...\n")
            main()
def send_mg_to_server(client):
    while True:
        messege = input("")
        if messege !="":
            client.sendall((messege).encode())
        else:
            client.sendall(("(empty)").encode())
def communicate_to_server(client):
    username = input("Enter the user name (Type 'exit' for ending the chat): ")
    if username !="":
        client.sendall(username.encode())
    else:
        print("User name can not be empty! Enter valid user name again")
    threading.Thread(target=listen_to_server_mg, args=(client, username,)).start()
    send_mg_to_server(client)
def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((des_ip,des_port))
    print("connected to the server")
    communicate_to_server(client)
if __name__ == '__main__':
    main()
