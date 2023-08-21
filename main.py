import socket

target_ip = "127.0.0.1"
start_port = 1
end_port = 1024 
for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port} açık")
        
        
        s.close()
    
    except KeyboardInterrupt:
        print("\nTarama işlemi kullanıcı tarafından iptal edildi.")
        break
    
    except socket.error:
        print("Bağlantı hatası. Port tarama işlemi tamamlanamadı.")
        break
      
