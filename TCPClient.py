from socket import *

serverName = '192.168.0.169'  # Địa chỉ IP của server
serverPort = 12000  # Cổng server

clientSocket = socket(AF_INET, SOCK_STREAM)  # Tạo socket TCP
clientSocket.connect((serverName, serverPort))  # Kết nối đến server

sentence = input('Nhập câu chữ thường: ')  # Nhập dữ liệu từ bàn phím
clientSocket.send(sentence.encode())  # Gửi dữ liệu (chuyển thành bytes)

modifiedSentence = clientSocket.recv(1024)  # Nhận phản hồi từ server
print('Từ server:', modifiedSentence.decode())  # In kết quả nhận được

clientSocket.close()  # Đóng kết nối
