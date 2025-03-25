from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  # Tạo socket UDP
serverSocket.bind(('', serverPort))  # Gán socket với cổng 12000

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)  # Nhận dữ liệu từ client
    modifiedMessage = message.decode().upper()  # Chuyển thành chữ hoa
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)  # Gửi kết quả về client
