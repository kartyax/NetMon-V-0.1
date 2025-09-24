import pyfiglet
from module import mon, graf

def header():
    banner = pyfiglet.figlet_format("Netmon V 0.1")
    print(banner)

if __name__ == "__main__":
    try:
        header()
        print("Network Monitoring")
        print("1. Ping")
        print("2. Traceroute")
        print("3. Port Scan")
        print("4. Ping + Grafik")

        choice = input("Pilih menu: ").strip()

        if choice == "1":
            host = input("Masukkan host: ") or "8.8.8.8"
            output, _ = mon.ping(host)
            print(output)

        elif choice == "2":
            host = input("Masukkan host: ") or "8.8.8.8"
            print(mon.traceroute(host))

        elif choice == "3":
            target = input("Masukkan host: ") or "127.0.0.1"
            print(mon.port_scan(target))

        elif choice == "4":
            host = input("Masukkan host: ") or "8.8.8.8"
            _, times = mon.ping(host, 5)
            graf.plot_ping_times(times)

        else:
            print("Pilihan tidak valid")

    except KeyboardInterrupt:
        print("\nKeluar dari program...")
