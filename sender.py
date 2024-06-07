import socket

def sender():
    host = '127.0.0.1'
    port = 12345

    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_address = (host, port)

    packets = ["Packet0", "Packet1", "Packet2", "Packet3", "Packet4"]
    window_size = 3
    base = 0

    while base < len(packets):
        sender_socket.sendto(f"{base},{packets[base]}".encode('utf-8'), receiver_address)

        try:
            ack = int(sender_socket.recv(1024).decode('utf-8'))
            if ack == base:
                print(f"Received ACK: {ack}")
                base += 1
        except socket.timeout:
            print("Timeout: Resending window")

    sender_socket.close()

if __name__ == "__main__":
    sender()
