import socket


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")

    HOST = "127.0.0.1"
    PORT = 8080

    my_socket.bind(
        (HOST, PORT)
    )  # the '' means that we're not inputting an ip address rather we're listening to the requests coming from the local network
    print(f"socket connected to {PORT}")

    my_socket.listen()
    print("socket is listening")

    while True:
        connect, address = my_socket.accept()
        print(f"get connection from {address}")
        data = connect.recv(1024)
        if data:
            print("Received: " + str(data))

        connect.send(data.upper())

        connect.close()

        break

    my_socket.close()


if __name__ == "__main__":
    main()
