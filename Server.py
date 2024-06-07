#Sever side 
import socket, threading

# coanstant
host_ip = '127.0.0.1'
host_port = 11336
encoder = "utf-8"
byte_size = 1024
active_clients = []


def listen_to_messege(client, username,s):
    while True:
        messege = client.recv(2048).decode(encoder)
        if messege != "exit" and messege !="":
            final_mg = username + '>' + messege
            send_mg_to_all(final_mg)
        elif messege == "exit":
            client.close()
            break
        else:
            print(f"The messege sent by the client {username} is empty.")



def send_mg_to_client(client, messege):
    client.sendall(messege.encode())


def send_mg_to_all(messege):
    for user in active_clients:
        send_mg_to_client(user[1], messege)


def client_handler(client,s):
    while True:
        username = client.recv(2048).decode(encoder)
        if username != "":
            active_clients.append((username, client))
            break
        else:
            print("client user name is empty.")
    threading.Thread(target=listen_to_messege, args=(client, username, s,)).start()


# socket with ipv4 with TCP
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host_ip, host_port))
    print(f"Running the server on {host_ip}:{host_port}")
    s.listen()
    print("Server is running...\n")

    # send and receive
    while True:
        client, addr = s.accept()
        print(f"Connected to {client}")

        threading.Thread(target=client_handler, args=(client, s,)).start()



if __name__ == '__main__':
    main()

