from socket import *

serverName = '10.10.103.232'  # Địa chỉ của server (có thể là IP hoặc tên miền)
serverPort = 12000  # Cổng server đang lắng nghe

clientSocket = socket(AF_INET, SOCK_DGRAM)  # Tạo socket UDP

isContinue = True

while isContinue:
    replyMessage = input('Nhập tin nhắn:')  # Nhập câu từ bàn phím
    if replyMessage == 'quit':
        isContinue = False
        break
    clientSocket.sendto(replyMessage.encode(), (serverName, serverPort))  # Gửi dữ liệu đến server

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # Nhận phản hồi từ server
    print(modifiedMessage.decode())  # Hiển thị phản hồi

clientSocket.close()  # Đóng kết nối
