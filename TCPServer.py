from socket import *

serverIP = '0.0.0.0'  # Lắng nghe trên tất cả các địa chỉ IP
serverPort = 12000  # Chạy trên cổng 12000

serverSocket = socket(AF_INET, SOCK_STREAM)  # Tạo socket TCP
serverSocket.bind((serverIP, serverPort))  # Gán socket với cổng
serverSocket.listen(1)  # Lắng nghe kết nối (tối đa 1 hàng đợi)
print('Server sẵn sàng nhận kết nối')

while True:
    connectionSocket, addr = serverSocket.accept()  # Chấp nhận kết nối từ client
    print('Đã kết nối với:', addr)

    isContinue = True
    while isContinue: # Lặp lại việc nhận và trả lời tin nhắn, khi không muốn kết nối với client này nữa thì đóng 
        recevMessage = connectionSocket.recv(1024).decode()  # Nhận dữ liệu từ client 
        print('Client:', addr, 'vừa gửi:', recevMessage)
        if recevMessage == 'quit':
            isContinue = False
            break
        
        replyMessage = input('Nhập tin nhắn: ')

        connectionSocket.send(replyMessage.encode())  # Gửi kết quả lại client
        #isContinue = input('Tiếp tục? (y/n): ') == 'y'
    
    connectionSocket.close()  # Đóng kết nối với client
    print('Đã đóng kết nối với:', addr)
