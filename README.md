# 🚀 PromptlyAI

<p align="center">
  <img src="static/images/logo-jam.png" alt="PromptlyAI Logo" width="180px" style="border-radius: 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1);"/>
</p>

<p align="center">
  <a href="https://github.com/egecagintepe/PromptlyAI/stargazers"><img src="https://img.shields.io/github/stars/egecagintepe/PromptlyAI?style=for-the-badge&color=8A2BE2" alt="Stars"></a>
  <a href="https://github.com/egecagintepe/PromptlyAI/network/members"><img src="https://img.shields.io/github/forks/egecagintepe/PromptlyAI?style=for-the-badge&color=blue" alt="Forks"></a>
  <a href="https://github.com/egecagintepe/PromptlyAI/issues"><img src="https://img.shields.io/github/issues/egecagintepe/PromptlyAI?style=for-the-badge&color=red" alt="Issues"></a>
</p>

---

## 🎯 Proje Amacı ve Vizyonu

**PromptlyAI**, yapay zekâ teknolojilerini iş ve eğitim dünyasında en verimli ve etkin şekilde kullanabilmeniz için tasarlanmış **LLM Destekli Etkileşim Mühendisliği Arayüzüdür**.

Kullanıcıların rastgele veya zayıf promptlar (girdiler) yazarak düşük verimli cevaplar almasının önüne geçmeyi hedefler. Sisteme girilen her prompt, arka planda gelişmiş bir yapay zekâ süzgecinden geçirilerek analiz edilir, **0 ile 100 arasında puanlanır** ve kullanıcılara anlık gelişim önerileri sunulur. Ayrıca, sistem her yanıttan sonra sohbetin akışına uygun olarak **yönlendirici derinleştirme promptları** üreterek kullanıcıyı pasif tüketicilikten çıkarıp, aktif bir yapay zekâ okuryazarına dönüştürür.

---

## 💎 Temel Özellikler

| Özellik | Açıklama |
| :--- | :--- |
| **⚡ Prompt İyileştirici** | Girilen zayıf ve karmaşık promptları tek tuşla en yüksek performansı verecek şekilde optimize eder. |
| **📊 Kalite Puanlama & Analiz** | Yazılan promptları 0-100 puan aralığında değerlendirir ve geliştirilmesi gereken noktaları önerir. |
| **💡 Sektörel Şablonlar** | Kullanıcının seçtiği meslek veya sektöre özel en sık sorulan 4 konu başlığı ve bunlara bağlı 6 hazır prompt sunar. |
| **🔄 Akıllı Sohbet Akışı** | Yapay zekanın verdiği her yanıttan sonra, diyaloğu derinleştirecek 6 adet yeni yönlendirici soru önerisi oluşturur. |
| **🔒 Güvenli Oturum & Geçmiş** | SQLite ve JWT tabanlı oturum yönetimi sayesinde kullanıcı geçmişi ve chat verileri güvenle saklanır. |
| **🎨 Premium Tasarım** | Dinamik renk kodlu arayüz, yumuşak hover efektleri ve karanlık tema (Siber-Barok estetik) desteği sunar. |

---

## 🛠️ Teknolojik Altyapı

Modern, hafif ve yüksek performanslı araçlarla inşa edilen mimarimiz:

- **Web Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Asenkron, güvenli ve aşırı hızlı)
- **AI Core:** [Google Gemini 2.5 Flash](https://ai.google.dev/) (En güncel `google-genai` SDK entegrasyonuyla)
- **Database ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) & [SQLite](https://www.sqlite.org/) (Hafif, lokal ve ilişkisel veri yönetimi)
- **Güvenlik:** [Starlette Session Middleware](https://www.starlette.io/middleware/#sessionmiddleware), JWT & Passlib (Güçlü şifreleme ve oturum yönetimi)
- **Frontend & Rendering:** [Jinja2 Templates](https://jinja.palletsprojects.com/), Modern Vanilla CSS & JavaScript

---

## 📂 Proje Dizin Yapısı

```bash
📂 PromptlyAI
 ├── 📄 auth.py          # Kullanıcı kimlik doğrulama, JWT ve Session işlemleri
 ├── 📄 database.py      # SQLAlchemy DB bağlantı motoru ve oturum yapısı
 ├── 📄 main.py          # FastAPI ana uygulama çatısı ve API rotaları
 ├── 📄 models.py        # SQLAlchemy veritabanı şemaları ve ORM tabloları
 ├── 📄 init.py          # Veritabanı tablolarını otomatik oluşturan script
 ├── 📄 requirements.txt # Python bağımlılıkları listesi
 ├── 📄 .env             # Gizli API Anahtarı ve yapılandırmalar (Git'e gitmez!)
 ├── 📄 .gitignore       # Git sisteminde saklanacak dosyaların engelleme listesi
 ├── 📂 templates/       # Jinja2 tabanlı HTML şablonları
 │    ├── base.html      # Ana iskelet şablonu
 │    ├── chat.html      # Sohbet ve prompt iyileştirme arayüzü
 │    ├── login.html     # Giriş ekranı arayüzü
 │    ├── register.html  # Kayıt ekranı arayüzü
 │    └── profile.html   # Kullanıcı istatistikleri ve geçmiş arayüzü
 ├── 📂 static/          # Arayüz tasarım varlıkları (CSS, JS, Görseller)
 │    ├── styles.css     # Özelleştirilmiş Siber-Barok tema tasarımları
 │    └── images/        # Logo ve görsel materyaller
 └── 📄 README.md        # Proje detaylı dökümantasyonu
```

---

## 🚀 Hızlı Kurulum ve Çalıştırma

> [!IMPORTANT]
> Projeyi başlatmadan önce bilgisayarınızda **Python 3.10+** sürümünün kurulu olduğundan emin olun.

### 1️⃣ Projeyi Klonlayın
```bash
git clone https://github.com/egecagintepe/PromptlyAI.git
cd PromptlyAI
```

### 2️⃣ Virtual Environment (Sanal Ortam) Oluşturun ve Aktifleştirin
**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4️⃣ Yapılandırma Dosyalarını Hazırlayın (`.env`)
Proje dizininde `.env` isminde bir dosya oluşturun ve Google Gemini API anahtarınızı tanımlayın:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```
> [!TIP]
> Güvenliğiniz için `.env` dosyası `.gitignore` içerisinde tanımlıdır ve hiçbir şekilde GitHub reposuna yüklenmez.

### 5️⃣ Veritabanını İlklendirin
İlk çalıştırma öncesi SQLite tablolarını oluşturmak için başlatma betiğini çalıştırın:
```bash
python init.py
```

### 6️⃣ Projeyi Başlatın
Uygulamayı lokal ortamda ayağa kaldırmak için uvicorn sunucusunu başlatın:
```bash
python -m uvicorn main:app --port 8000 --reload
```

Sunucu açıldıktan sonra tarayıcınızdan **[http://127.0.0.1:8000](http://127.0.0.1:8000)** adresine giderek uygulamayı test edebilirsiniz!

---

## 👥 Proje Ekibi

<table align="center">
  <tr>
    <td align="center"><b>Aslı Şemşimoğlu</b><br>Bilgisayar Mühendisliği</td>
    <td align="center"><b>Muhammet Seyfi Büyük</b><br>Elektronik Teknolojisi</td>
    <td align="center"><b>Ege Çağın Tepe</b><br>Elektrik-Elektronik Müh.</td>
  </tr>
  <tr>
    <td align="center"><b>Amine Demirbaş</b><br>Bilgisayar Programcılığı</td>
    <td align="center"><b>Döne Beyza Kurt</b><br>Elektrik-Elektronik Müh.</td>
    <td align="center"></td>
  </tr>
</table>

---

<p align="center">
  PromptlyAI bir <b>AIJAM Grup 5</b> projesidir. ❤️ ile geliştirildi.
</p>
