import matplotlib.pyplot as plt

def plot_ping_times(times):
    if not times:
        print("Tidak ada data ping untuk ditampilkan")
        return
    plt.plot(times, marker="o", linestyle="-")
    plt.xlabel("Tes ke-")
    plt.ylabel("Waktu respon (ms)")
    plt.title("Monitoring Ping")
    plt.grid(True)
    plt.show()
