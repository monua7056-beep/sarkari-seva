from flask import Flask, render_template_string

app = Flask(__name__)

# ==================== OWNER DETAILS ====================
OWNER_NAME       = "Monu Chaudhary"
WHATSAPP_NUMBER  = "917587507021"
PHONE_NUMBER     = "7587507021"
TELEGRAM_USER    = "MonuChaudhary75"
INSTAGRAM_USER   = "mr_monu_mp_35"
INSTAGRAM_LINK   = "https://instagram.com/mr_monu_mp_35"

# ==================== SERVICES LIST ====================
SERVICES = [
    {"name": "PAN Card",             "icon": "🪪", "desc": "New / Correction"},
    {"name": "Aadhaar Update",       "icon": "🆔", "desc": "Address / Mobile"},
    {"name": "Voter ID Card",        "icon": "🗳️", "desc": "New / Correction"},
    {"name": "Driving Licence",      "icon": "🚗", "desc": "Learner / Permanent"},
    {"name": "Ration Card",          "icon": "🍚", "desc": "New Ration Card"},
    {"name": "Ayushman Card",        "icon": "💳", "desc": "PMJAY Golden Card"},
    {"name": "Passport",             "icon": "📘", "desc": "New / Renewal"},
    {"name": "Birth Certificate",    "icon": "👶", "desc": "Janm Praman Patra"},
    {"name": "Death Certificate",    "icon": "📜", "desc": "Mrityu Praman Patra"},
    {"name": "Income Certificate",   "icon": "💰", "desc": "Aay Praman Patra"},
    {"name": "Caste Certificate",    "icon": "📋", "desc": "Jati Praman Patra"},
    {"name": "Domicile Certificate", "icon": "🏠", "desc": "Mool Niwas Praman"},
    {"name": "e-Shram Card",         "icon": "👷", "desc": "Shramik Registration"},
    {"name": "PM Kisan Samman",      "icon": "🌾", "desc": "Kisan Nidhi"},
    {"name": "Udyam Certificate",    "icon": "🏭", "desc": "MSME Registration"},
    {"name": "GST Registration",     "icon": "🧾", "desc": "New GST Number"},
    {"name": "ITR Filing",           "icon": "📊", "desc": "Income Tax Return"},
    {"name": "Ration e-KYC",         "icon": "✅", "desc": "Ration e-KYC Update"},
    {"name": "PAN-Aadhaar Link",     "icon": "🔗", "desc": "PAN Aadhaar Seeding"},
    {"name": "Voter Card Download",  "icon": "⬇️", "desc": "e-EPIC Download"},
]

# ==================== HTML TEMPLATE ====================
HTML = """
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sarkari Seva Portal | {{ owner }}</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
* { margin:0; padding:0; box-sizing:border-box; font-family:'Poppins',sans-serif; }
body {
  background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1a2980);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  color:#fff; min-height:100vh; overflow-x:hidden;
}
@keyframes gradientBG {
  0% { background-position:0% 50%; }
  50% { background-position:100% 50%; }
  100% { background-position:0% 50%; }
}
.particle {
  position: fixed; border-radius:50%;
  background: rgba(255,215,0,0.15);
  pointer-events:none; z-index:0;
  animation: floatUp linear infinite;
}
@keyframes floatUp {
  0% { transform: translateY(100vh) scale(0); opacity:0; }
  10% { opacity:1; }
  100% { transform: translateY(-100px) scale(1); opacity:0; }
}
header {
  position:relative; z-index:2; text-align:center;
  padding: 25px 15px 20px;
  background: rgba(0,0,0,0.4);
  backdrop-filter: blur(12px);
  border-bottom: 3px solid #FFD700;
  box-shadow: 0 5px 30px rgba(255,215,0,0.35);
  animation: slideDown 0.9s ease;
}
@keyframes slideDown {
  from { transform: translateY(-100%); opacity:0; }
  to   { transform: translateY(0); opacity:1; }
}
.emblem {
  font-size: 48px; margin-bottom: 5px;
  display:inline-block;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0%,100% { transform: scale(1); }
  50% { transform: scale(1.15); }
}
header h1 {
  font-size: 26px; font-weight:900; letter-spacing:1px;
  background: linear-gradient(90deg, #FFD700, #FFA500, #FFD700);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shine 3s linear infinite;
}
@keyframes shine { to { background-position: 200% center; } }
header p { font-size:13px; color:#cfd8dc; margin-top:6px; font-weight:300; }
.owner-tag {
  display:inline-block; margin-top:12px;
  padding: 7px 20px;
  background: linear-gradient(90deg, #FFD700, #FFA500);
  color:#000; font-weight:700; border-radius:25px; font-size:13px;
  box-shadow: 0 0 20px rgba(255,215,0,0.7);
  animation: glow 2s infinite alternate;
}
@keyframes glow {
  from { box-shadow: 0 0 15px rgba(255,215,0,0.5); }
  to   { box-shadow: 0 0 32px rgba(255,215,0,1); }
}
.marquee {
  background:#FFD700; color:#000; padding:8px 0;
  font-weight:700; font-size:13px;
  overflow:hidden; white-space:nowrap;
  position:relative; z-index:2;
}
.marquee span {
  display:inline-block; padding-left:100%;
  animation: scroll 22s linear infinite;
}
@keyframes scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-100%); }
}
.search-box {
  max-width: 520px; margin: 22px auto 8px; padding: 0 15px;
  position:relative; z-index:2;
}
.search-box input {
  width:100%; padding:14px 22px;
  border-radius:30px;
  border: 2px solid rgba(255,215,0,0.5);
  background: rgba(255,255,255,0.1);
  color:#fff; font-size:15px; outline:none;
  backdrop-filter: blur(10px);
  transition: 0.3s;
}
.search-box input:focus {
  border-color:#FFD700;
  box-shadow: 0 0 25px rgba(255,215,0,0.6);
}
.search-box input::placeholder { color:#bbb; }
.container {
  max-width:1200px; margin:0 auto;
  padding: 20px 15px 130px;
  display:grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap:18px;
  position:relative; z-index:2;
}
.card {
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(255,215,0,0.25);
  border-radius:18px;
  padding: 22px 12px 18px;
  text-align:center;
  cursor:pointer;
  transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position:relative; overflow:hidden;
  opacity:0; transform: translateY(35px);
  animation: fadeUp 0.7s forwards;
}
.card::before {
  content:''; position:absolute;
  top:-50%; left:-50%; width:200%; height:200%;
  background: radial-gradient(circle, rgba(255,215,0,0.18), transparent 60%);
  opacity:0; transition:0.5s;
}
.card:hover::before { opacity:1; }
.card:hover {
  transform: translateY(-10px) scale(1.04);
  border-color:#FFD700;
  box-shadow: 0 15px 40px rgba(255,215,0,0.4);
}
.card:active { transform: scale(0.97); }
@keyframes fadeUp { to { opacity:1; transform: translateY(0); } }
.card .icon {
  font-size: 42px; margin-bottom: 10px;
  display:block;
  animation: iconBounce 3s ease-in-out infinite;
}
@keyframes iconBounce {
  0%,100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
.card h3 {
  font-size:14px; font-weight:700; color:#FFD700;
  margin-bottom:4px; letter-spacing:0.3px;
}
.card .desc {
  font-size:11px; color:#cfd8dc; margin-bottom:12px; font-weight:300;
}
.card .apply {
  margin-top:6px;
  background: linear-gradient(90deg, #25D366, #128C7E);
  color:#fff; font-weight:700; font-size:12px;
  padding: 8px 0; border-radius:10px;
  display:flex; align-items:center; justify-content:center; gap:6px;
  box-shadow: 0 4px 12px rgba(37,211,102,0.4);
  transition: 0.3s;
}
.card:hover .apply {
  background: linear-gradient(90deg, #128C7E, #25D366);
  box-shadow: 0 6px 20px rgba(37,211,102,0.7);
}
.contact-bar {
  position: fixed; bottom:0; left:0; right:0;
  background: rgba(0,0,0,0.9);
  backdrop-filter: blur(15px);
  border-top: 2px solid #FFD700;
  padding: 10px 6px;
  display:flex; justify-content:space-around; align-items:center;
  z-index:99;
  box-shadow: 0 -5px 25px rgba(255,215,0,0.35);
  animation: slideUp 0.9s ease;
}
@keyframes slideUp {
  from { transform: translateY(100%); }
  to   { transform: translateY(0); }
}
.contact-btn {
  display:flex; flex-direction:column; align-items:center;
  gap:4px; text-decoration:none;
  color:#fff; font-size:10px; font-weight:600;
  transition: 0.3s; flex:1;
}
.contact-btn i {
  font-size:22px;
  width:46px; height:46px;
  display:flex; align-items:center; justify-content:center;
  border-radius:50%;
  transition: 0.35s;
  color:#fff;
}
.contact-btn:hover i { transform: translateY(-5px) scale(1.15); }
.contact-btn.wa i   { background: linear-gradient(135deg,#25D366,#128C7E); box-shadow:0 0 18px rgba(37,211,102,0.8); }
.contact-btn.tg i   { background: linear-gradient(135deg,#0088cc,#006699); box-shadow:0 0 18px rgba(0,136,204,0.8); }
.contact-btn.ig i   { background: linear-gradient(135deg,#f09433,#dc2743,#bc1888); box-shadow:0 0 18px rgba(220,39,67,0.8); }
.contact-btn.ph i   { background: linear-gradient(135deg,#FFD700,#FFA500); color:#000; box-shadow:0 0 18px rgba(255,215,0,0.8); }
.toast {
  position: fixed; top:20px; left:50%;
  transform: translateX(-50%) translateY(-100px);
  background: linear-gradient(90deg,#25D366,#128C7E);
  color:#fff; padding:12px 25px;
  border-radius:30px; font-weight:700; font-size:13px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.4);
  z-index:999; transition: 0.5s cubic-bezier(0.175,0.885,0.32,1.275);
  display:flex; align-items:center; gap:8px;
}
.toast.show { transform: translateX(-50%) translateY(0); }
.footer-note {
  text-align:center; padding: 15px 10px 110px;
  color:#90a4ae; font-size:11px;
  position:relative; z-index:2;
}
.footer-note b { color:#FFD700; }
@media (max-width:480px) {
  header h1 { font-size:20px; }
  .emblem { font-size:40px; }
  .card .icon { font-size:36px; }
  .card h3 { font-size:12.5px; }
  .container { grid-template-columns: repeat(2, 1fr); gap:12px; }
  .contact-btn i { width:42px; height:42px; font-size:20px; }
}
</style>
</head>
<body>

<header>
  <div class="emblem">🏛️</div>
  <h1>Sarkari Seva Portal</h1>
  <p>Har Sarkari Kaam Ab Ghar Baithe — Fast & Easy</p>
  <div class="owner-tag">👑 Owner: {{ owner }}</div>
</header>

<div class="marquee">
  <span>📢 PAN Card • Aadhaar Update • Voter ID • Driving Licence • Ration Card • Ayushman Card • Passport • e-Shram • PM Kisan • GST • ITR — Sabhi Sarkari Kaam Ke Liye WhatsApp Karein: {{ phone }} &nbsp;&nbsp;&nbsp; ✅ 100% Safe & Trusted Service by {{ owner }} &nbsp;&nbsp;&nbsp;</span>
</div>

<div class="search-box">
  <input type="text" id="searchInput" placeholder="🔍 Search karein... (jaise: PAN, Aadhaar, Voter)" onkeyup="filterCards()">
</div>

<div class="container" id="cardContainer">
  {% for s in services %}
  <div class="card" data-name="{{ s.name|lower }}" style="animation-delay: {{ loop.index0 * 0.06 }}s"
       onclick="applyService('{{ s.name }}')">
    <span class="icon">{{ s.icon }}</span>
    <h3>{{ s.name }}</h3>
    <div class="desc">{{ s.desc }}</div>
    <div class="apply"><i class="fab fa-whatsapp"></i> Apply Now</div>
  </div>
  {% endfor %}
</div>

<div class="footer-note">
  © 2025 <b>Sarkari Seva Portal</b> | Managed by <b>{{ owner }}</b><br>
  Ye ek private service portal hai, government website nahi.
</div>

<div class="contact-bar">
  <a class="contact-btn wa" href="https://wa.me/{{ whatsapp }}?text=Namaste%20{{ owner }}%20ji%2C%20mujhe%20sarkari%20seva%20chahiye" target="_blank">
    <i class="fab fa-whatsapp"></i><span>WhatsApp</span>
  </a>
  <a class="contact-btn tg" href="https://t.me/{{ telegram_user }}" target="_blank">
    <i class="fab fa-telegram"></i><span>Telegram</span>
  </a>
  <a class="contact-btn ig" href="{{ instagram_link }}" target="_blank">
    <i class="fab fa-instagram"></i><span>Instagram</span>
  </a>
  <a class="contact-btn ph" href="tel:+91{{ phone }}">
    <i class="fas fa-phone"></i><span>Call</span>
  </a>
</div>

<div class="toast" id="toast">
  <i class="fas fa-check-circle"></i> <span id="toastMsg">WhatsApp par bhej rahe hain...</span>
</div>

<script>
for (let i=0; i<25; i++) {
  const p = document.createElement('div');
  p.className = 'particle';
  const size = Math.random()*15 + 5;
  p.style.width = size + 'px';
  p.style.height = size + 'px';
  p.style.left = Math.random()*100 + '%';
  p.style.animationDuration = (Math.random()*15 + 12) + 's';
  p.style.animationDelay = (Math.random()*10) + 's';
  document.body.appendChild(p);
}

const OWNER = "{{ owner }}";
const WHATSAPP = "{{ whatsapp }}";

function applyService(serviceName) {
  const msg = `Namaste ${OWNER} ji 🙏%0A%0AMujhe ye sarkari seva chahiye:%0A%0A📌 *Service:* ${serviceName}%0A%0AKripya iska price aur documents ki list bhejiye.%0A%0ADhanyavaad 🙏`;
  const url = `https://wa.me/${WHATSAPP}?text=${msg}`;

  const toast = document.getElementById('toast');
  document.getElementById('toastMsg').innerText = serviceName + ' ke liye WhatsApp khul raha hai...';
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2500);

  setTimeout(() => window.open(url, '_blank'), 400);
}

function filterCards() {
  const q = document.getElementById('searchInput').value.toLowerCase();
  document.querySelectorAll('.card').forEach(card => {
    const name = card.getAttribute('data-name');
    card.style.display = name.includes(q) ? 'block' : 'none';
  });
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        owner=OWNER_NAME,
        services=SERVICES,
        whatsapp=WHATSAPP_NUMBER,
        phone=PHONE_NUMBER,
        telegram_user=TELEGRAM_USER,
        instagram_link=INSTAGRAM_LINK
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
