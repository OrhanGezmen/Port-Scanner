import socket

# Hedef IP adresini ve port aralığını belirleyin
target_ip = "127.0.0.1"
start_port = 1
end_port = 1024  # Port aralığı örneğin 1 ila 1024 arası

# Belirtilen IP adresini ve port aralığını taramak için bir döngü kullanın
for port in range(start_port, end_port + 1):
    try:
        # Socket objesi oluşturun
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Belirtilen IP adresi ve port numarasına bağlanmayı dene
        result = s.connect_ex((target_ip, port))
        
        # Bağlantı başarılıysa (0), port açıktır
        if result == 0:
            print(f"Port {port} açık")
        
        # Socket'i kapat
        s.close()
    
    except KeyboardInterrupt:
        print("\nTarama işlemi kullanıcı tarafından iptal edildi.")
        break
    
    except socket.error:
        print("Bağlantı hatası. Port tarama işlemi tamamlanamadı.")
        break
      