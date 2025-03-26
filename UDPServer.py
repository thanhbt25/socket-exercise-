from socket import *

serverIP = '0.0.0.0'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)  # Tạo socket UDP
serverSocket.bind((serverIP, serverPort))  # Gán socket với cổng 12000
print("Server sẵn sàng nhận kết nối")

while True:
    isContinue = True

    while isContinue:
        recevMessage, clientAddress = serverSocket.recvfrom(2048)  # Nhận dữ liệu từ client
        print('Client:', clientAddress, 'vừa gửi:', recevMessage.decode())
        replyMessage = recevMessage.decode().upper()

        print('Server trả lời:', )  # Hiển thị kết quả
        serverSocket.sendto(replyMessage.encode(), clientAddress)  # Gửi kết quả về client
