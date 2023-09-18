import socket


def main():
    HOST = "127.0.0.1"
    PORT = 8080

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")

    my_socket.connect((HOST, PORT))
    my_message = input("enter your message: ")
    my_socket.sendall(bytes(my_message, "utf-8"))
    data = my_socket.recv(1024)
    print("received back " + str(data))


if __name__ == "__main__":
    main()
