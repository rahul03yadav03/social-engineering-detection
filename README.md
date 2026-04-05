# Social Engineering Detection Project

##  Overview
This repository contains a **PowerPoint presentation (PPT)** on various **Social Engineering Attacks** and their detection methods.  

All attack types are explained in detail in the PPT.

---

##  Topics Covered in PPT
- Phishing  
- Spear Phishing  
- Whaling  
- Smishing  
- Vishing  
- Pretexting  
- Baiting  
- Quid Pro Quo  
- Tailgating (Piggybacking)  
- Shoulder Surfing  
- Dumpster Diving  
- Impersonation  
- Watering Hole Attack  
- Scareware  

---

##  Detection (Coding Part)
Out of all attacks, the following **4 types are implemented for detection using code**:

1. Phishing (Email)  
2. Smishing (SMS / Text)  
3. Baiting (Malicious Files / USB)  
4. Watering Hole / Scareware (Malicious Websites)  

###  Detection Approach
The code uses techniques like:
- **Regular Expressions (`re` module)**  
- Keyword matching  
- File extension checking  
- URL and text analysis  

- Suspicious keywords:
- Free / Offer: free, crack, hack, keygen, prize, gift  
- Urgency: urgent, limited, hurry, act fast  
- Piracy: cracked, patched, full version, premium  
- Clickbait: hot, sexy, leaked, exclusive  
- Fear: virus, hacked, alert, infected  
- Documents: invoice, payment, confidential  

These patterns are used across the detection scripts to identify potential threats.

---

##  Project Contents
- **PPT File** – Contains explanation of all attack types  
- **Code Files** – Detection scripts for selected attacks  
- **README.md** – Project overview  

---

##  Author
**Rahul Yadav**

---

##  Acknowledgment
- All images in the PPT were generated using AI tools.  
- For coding, only common malicious keywords and file extensions were used to detect attacks; the code itself was written manually.  

---

##  Note
This project is created for **educational purposes only**.

