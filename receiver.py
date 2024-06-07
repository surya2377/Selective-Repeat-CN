import socket

def receiver():
    host = '127.0.0.1'
    port = 12345

    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind((host, port))

    expected_seq_num = 0

    while True:
        seq_num, packet = receiver_socket.recvfrom(1024).decode('utf-8').split(',')
        seq_num = int(seq_num)

        if seq_num == expected_seq_num:
            print(f"Received: {packet}")
            receiver_socket.sendto(str(seq_num).encode('utf-8'), packet[1])
            expected_seq_num += 1

    receiver_socket.close()

if __name__ == "__main__":
    receiver()
