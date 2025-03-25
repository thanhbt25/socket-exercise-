from socket import *

serverName = 'localhost'  # Địa chỉ của server (có thể là IP hoặc tên miền)
serverPort = 12000  # Cổng server đang lắng nghe

clientSocket = socket(AF_INET, SOCK_DGRAM)  # Tạo socket UDP

message = input('Input lowercase sentence:')  # Nhập câu từ bàn phím
clientSocket.sendto(message.encode(), (serverName, serverPort))  # Gửi dữ liệu đến server

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # Nhận phản hồi từ server
print(modifiedMessage.decode())  # Hiển thị phản hồi

clientSocket.close()  # Đóng kết nối
