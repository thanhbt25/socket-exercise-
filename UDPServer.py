from socket import *

serverIP = '0.0.0.0'
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)  # Tạo socket UDP
serverSocket.bind((serverIP, serverPort))  # Gán socket với cổng 12000
print("Server sẵn sàng nhận kết nối")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)  # Nhận dữ liệu từ client
    capitalizedSentence = message.decode().upper()  # Chuyển thành chữ hoa
    print('Client:', clientAddress, 'vừa gửi:', message.decode())
    print('Server trả lại:', capitalizedSentence)  # Hiển thị kết quả
    serverSocket.sendto(capitalizedSentence.encode(), clientAddress)  # Gửi kết quả về client
