from socket import *

serverIP = '0.0.0.0'  # Lắng nghe trên tất cả các địa chỉ IP
serverPort = 12000  # Chạy trên cổng 12000

serverSocket = socket(AF_INET, SOCK_STREAM)  # Tạo socket TCP
serverSocket.bind((serverIP, serverPort))  # Gán socket với cổng
serverSocket.listen(1)  # Lắng nghe kết nối (tối đa 1 hàng đợi)
print('Server sẵn sàng nhận kết nối')

while True:
    connectionSocket, addr = serverSocket.accept()  # Chấp nhận kết nối từ client
    sentence = connectionSocket.recv(1024).decode()  # Nhận dữ liệu từ client
    capitalizedSentence = sentence.upper()  # Chuyển thành chữ hoa
    print('Client:', addr, 'vừa gửi:', sentence)
    print('Server trả lại:', capitalizedSentence)  # Hiển thị kết quả
    connectionSocket.send(capitalizedSentence.encode())  # Gửi kết quả lại client
    
    connectionSocket.close()  # Đóng kết nối với client
