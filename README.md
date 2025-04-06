# 🧠 Dokter Vin - Chatbot Psikolog Gen Z

Chatbot AI berbasis web yang dibuat menggunakan Python Flask dan integrasi dengan Gemini API. Bot ini dirancang untuk menjadi teman curhat virtual yang memahami gaya bicara Gen Z, menggunakan pendekatan psikologi seperti CBT, Mindfulness, dan validasi emosi.

---

## ✨ Fitur Utama

- 🤖 Chatbot dengan gaya Gen Z: santai tapi profesional  
- 🧘‍♀️ Menggunakan pendekatan psikologi seperti CBT & mindfulness  
- 🧠 Respon empatik & tidak memberikan diagnosa langsung  
- ⚠️ Deteksi otomatis kata sensitif dan saran hotline mental health  
- 💬 UI responsif dengan efek typing indicator  
- 🔐 Session-based chat history (tidak tersimpan di database)  

---

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python Flask  
- **Frontend**: HTML, CSS, JavaScript (jQuery)  
- **AI**: [Gemini Generative AI](https://ai.google.dev/)  
- **Style**: Custom CSS  
- **Session Handling**: Flask Session  

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 2. Buat Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set API Key Gemini

Edit bagian ini di `app.py`:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

> 🔐 **Catatan:** Jangan commit API key kamu ke GitHub. Gunakan `.env` di produksi.

### 5. Jalankan Aplikasi

```bash
python app.py
```

Buka browser dan akses: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Contoh Percakapan

**Pengguna:**  
> "Akhir-akhir ini aku ngerasa kosong bgt..."

**Bot:**  
> "Ygy... itu berat banget gasih. Tapi makasih udah cerita, kamu hebat udah sampai di titik ini. Gimana kalo kita coba latihan napas bareng bentar?"

---

## 📁 Struktur Folder

``` bash
.
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md
└── requirements.txt
```

---

## 🛡️ Deteksi Krisis

Jika pengguna mengetik kata seperti `bunuh diri`, `gantung diri`, atau `mati`, chatbot akan langsung memberikan saran hotline dan tidak menggunakan AI response biasa.

---

## 💡 Roadmap

- [ ] Tambah autentikasi user  
- [ ] Simpan chat history ke database  
- [ ] Tambahkan suara (Text-to-Speech)  
- [ ] Responsif untuk mobile 100%  

---

## 🙌 Kontribusi

Pull request terbuka! Jangan ragu buat bantu ngembangin fitur atau memperbaiki bug.