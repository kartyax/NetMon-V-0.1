# NetMon-V-0.1
Mini project monitoring jaringan sederhana berbasis **Python (CLI)**.  
Dibuat untuk mempelajari dasar-dasar monitoring dan visualisasi trafik jaringan di Linux.

---

## ⚙️ Persyaratan
- **Python 3.10+**
- Sistem operasi Linux
- Paket Python ada di `requirements.txt`

---

## Cara Instalasi
Salin perintah ini ke terminal:

```bash
# Clone repo
git clone https://github.com/username/NetMon-V-0.1.git
cd NetMon-V-0.1

# Buat virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Buat folder logs jika belum ada
mkdir -p logs
