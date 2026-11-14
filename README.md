<div align="center">

# 🛡️ Social Engineering Detection

### *Humans are the weakest link. Let's teach code to spot the bait.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=gnubash&logoColor=white)
![Detections](https://img.shields.io/badge/Detectors-4-red?style=for-the-badge)
![Purpose](https://img.shields.io/badge/Purpose-Educational-success?style=for-the-badge)
![License](https://img.shields.io/badge/Made%20by-Rahul%20Yadav-blueviolet?style=for-the-badge)

**A beginner-friendly cybersecurity project: a full PowerPoint on 14 social engineering attacks, plus a Python CLI that detects 4 of them.**

[Overview](#-overview) • [Attacks Covered](#-attacks-covered-in-the-ppt) • [Detectors](#-the-detection-engine) • [Quick Start](#-quick-start) • [How It Works](#-how-it-works) • [Structure](#-project-structure)

</div>

---

## 🎯 Overview

Social engineering attacks don't break systems. They **break people**. This project has two parts:

| 📊 Theory | 💻 Practice |
|---|---|
| A PowerPoint explaining **14 social engineering attacks** in detail | A Python CLI that **detects 4 of those attacks** using pattern analysis |

---

## 🎭 Attacks Covered in the PPT

<table>
<tr>
<td>

**📧 Digital Attacks**
- Phishing
- Spear Phishing
- Whaling
- Smishing
- Vishing
- Baiting
- Watering Hole Attack
- Scareware

</td>
<td>

**🕴️ Human / Physical Attacks**
- Pretexting
- Quid Pro Quo
- Tailgating (Piggybacking)
- Shoulder Surfing
- Dumpster Diving
- Impersonation

</td>
</tr>
</table>

---

## 🔍 The Detection Engine

Four attacks are implemented as working detectors:

| # | Attack | Input | Module |
|:-:|---|---|---|
| 1️⃣ | **Phishing** 📧 | Email text | `phishing_email/email.py` |
| 2️⃣ | **Smishing** 📱 | SMS text | `smishing/smishng.py` |
| 3️⃣ | **Baiting** 💾 | File name | `baiting/baiting.py` |
| 4️⃣ | **Scareware / Watering Hole** 🌐 | URL | `scareware/scareware.py` |

---

## ⚙️ How It Works

Each detector builds a **risk score** from simple, explainable signals. If the score crosses a threshold, the input is flagged.

```
 Input ──▶  Keyword Scan ──▶ Pattern Checks ──▶ Risk Score ──▶ Verdict
                                                     │
                                          ≥ threshold → 🚨 Malicious
                                          <  threshold → ✅ Safe
```

### Techniques used

- 🔤 **Regular expressions** (`re` module)
- 🗝️ **Keyword matching** across threat categories
- 📎 **File extension checking**
- 🔗 **URL and text analysis**
- 🎭 **Lookalike domain detection** (e.g. `paypa1.com`, `g00gle.com`)

### Keyword categories

| Category | Example triggers |
|---|---|
| 🎁 **Free / Offer** | `free`, `crack`, `hack`, `keygen`, `prize`, `gift` |
| ⏰ **Urgency** | `urgent`, `limited`, `hurry`, `act fast` |
| 🏴‍☠️ **Piracy** | `cracked`, `patched`, `full version`, `premium` |
| 🎣 **Clickbait** | `hot`, `sexy`, `leaked`, `exclusive` |
| 😱 **Fear** | `virus`, `hacked`, `alert`, `infected` |
| 📄 **Fake documents** | `invoice`, `payment`, `confidential` |

### Detector signals at a glance

| Detector | What it checks | Flagged when |
|---|---|---|
| 📧 **Phishing** | Suspicious keywords, shortened or IP-based links, fake domains | Score > 3, **or** any bad link, **or** a fake domain |
| 📱 **Smishing** | Scam keywords, URLs, long digit strings (OTPs, phone numbers) | Score ≥ 3 |
| 💾 **Baiting** | Executable extensions, double extensions (`photo.jpg.exe`), bait keywords | Score ≥ 3 |
| 🌐 **Scareware** | `http://`, IP-based URLs, URL shorteners, keywords, many subdomains, `@` / `-` characters | Score ≥ 3 |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/rahul03yadav03/social-engineering-detection
cd social-engineering-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Only one external package is needed: `colorama`, for colored terminal output.

### 3. Run the CLI

```bash
python main.py
```

You'll see:

```
Welcome to the Social Engineering Detection CLI!
Select the type of social engineering attack to analyze
(1: Phishing Email, 2: Smishing, 3: Baiting, 4: Scareware):
```

Pick a number, then choose whether to analyze a **file** or type the content **line by line**.

---

## 🧪 Try It Out

| Detector | Sample input | Expected result |
|---|---|---|
| 💾 Baiting | `free_game_crack.exe` | 🚨 Baiting Detected |
| 💾 Baiting | `holiday_photo.jpg` | ✅ Safe File |
| 📱 Smishing | `Congratulations! You won a prize. Click http://bit.ly/claim now` | 🚨 Smishing Detected |
| 🌐 Scareware | `http://192.168.1.1/secure-login/verify` | 🚨 Malicious Website |
| 📧 Phishing | `Urgent: verify your account at http://paypa1.com` | 🚨 Likely phishing |

> Run each module directly too: `python baiting/baiting.py`, and so on.

---

## 📁 Project Structure

```
social-engineering-detection/
│
├── 📊 PPT file                  # Explanation of all 14 attacks
├── 📄 README.md                 # You are here
├── 📦 requirements.txt          # Dependencies (colorama)
│
├── 🐍 main.py                   # CLI entry point
│
├── baiting/
│   └── baiting.py               # Malicious file detection
├── phishing_email/
│   └── email.py                 # Phishing email analysis
├── scareware/
│   └── scareware.py             # Malicious website detection
└── smishing/
    └── smishng.py               # Smishing (SMS) detection
```

---

## ⚠️ Limitations

This is an **educational, rule-based** project, not a production security tool.

- Keyword matching can produce **false positives** (safe messages flagged) and **false negatives** (clever attacks missed).
- It does not check live threat feeds, scan file contents, or use machine learning.
- Never rely on it as your only line of defense.

## 🔮 Future Ideas

- [ ] Machine-learning classifier to replace pure keyword scoring
- [ ] Vishing detection from call transcripts
- [ ] Real-time URL reputation lookup
- [ ] Web or GUI front end
- [ ] Unit tests and sample datasets

---

## 👤 Author

**Rahul Yadav**

## 🙏 Acknowledgments

- 🎨 All images in the PPT were generated using AI tools.
- 🤖 AI was used only to research common malicious keywords and file extensions. The detection code itself was written manually.

---

<div align="center">

### 📌 Disclaimer

*This project is created for **educational purposes only**.*

⭐ **If you found this useful, give the repo a star!** ⭐

</div>
