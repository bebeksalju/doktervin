import google.generativeai as genai
from flask import Flask, render_template, request, jsonify, session

genai.configure(api_key="####################")

# Inisialisasi Flask
app = Flask(__name__)

# Set secret key untuk session
app.secret_key = "secret_key_123"

# Route utama untuk halaman web
@app.route("/")
def home():
    return render_template("index.html")

# Endpoint untuk menangani pesan pengguna

# Modifikasi route chat
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    # Inisialisasi chat history di session jika belum ada
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    # Prompt yang lebih terstruktur
    initial_prompt = {
        "role": "user",
        "parts": [
            "Kamu adalah psikiater ahli yang sangat memahami Gen Z. jawabanmu singkat namun sangat berkenan dan dapat mengetahui perasaan pasien. ",
            "Gaya bicaramu:",
            "- Santai tapi profesional",
            "- Gunakan slang Gen Z yang tepat (e.g., 'gasih', 'ygy', 'btw')",
            "- Tetap empatik dan berbasis teknik psikologi",
            "Teknik yang harus digunakan:",
            "- CBT untuk masalah kognitif",
            "- Mindfulness untuk kecemasan",
            "- Validasi emosi",
            "JANGAN:",
            "- Memberi diagnosa langsung",
            "- Terlalu formal/kaku",
            "- Mengabaikan perasaan pasien",
            "Percakapan saat ini:"
        ]
    }
    
    # Gabungkan history dengan prompt baru
    messages = [initial_prompt] + session['chat_history'] + [
        {"role": "user", "parts": [user_message]}
    ]
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Cek kata sensitif
    sensitive_words = ["bunuh diri", "bundir", "mati", "gantung diri"]
    if any(word in user_message.lower() for word in sensitive_words):
        response_text = (
            "Waduh, ini serius banget gasih... 🙁 Aku sangat sarankan kamu hubungi profesional atau "
            "telepon hotline kesehatan mental ya. Kamu nggak sendirian, aku di sini buat dengerin kamu. "
            "Ini nomor hotline yang bisa dihubungi: 119 atau 1-800-273-TALK (8255)."
        )
    else:
        try:
            response = model.generate_content(messages)
            response_text = response.text
            
            # Simpan ke history (batasi agar tidak terlalu panjang)
            session['chat_history'].extend([
                {"role": "user", "parts": [user_message]},
                {"role": "model", "parts": [response_text]}
            ])
            session['chat_history'] = session['chat_history'][-6:]  # Simpan 3 balasan terakhir
        except Exception as e:
            response_text = "Aduh, error nih. Bisa ulangi lagi? Aku kurang denger tadi..."

    return jsonify({"response": response_text})


# Menjalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)