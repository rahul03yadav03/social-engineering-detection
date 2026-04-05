import re

def detect_baiting(filename):
    
    fake_extension = [".exe", ".bat", ".vbs", ".scr" , ".cmd" ".exe", ".bat", ".vbs", ".scr", ".cmd", ".msi", ".com", 
    ".pif", ".jar", ".ps1", ".wsf", ".js", ".jse", ".hta", ".cpl"]
    
    
    fake_keywords = ["free", "crack", "hack", "keygen", "prize", "offer" "free", "crack", "hack", "keygen", "prize", "offer", "gift", "bonus", 
    "reward", "winner", "lottery", "cash", "money", "rich", "million", "billionaire",
    
    # Urgency
    "urgent", "limited", "expires", "now", "today", "hurry", "last chance", 
    "act fast", "don't wait", "only", "exclusive",
    
    # Piracy
    "cracked", "patched", "activated", "full version", "premium", "pro", 
    "unlocked", "nulled", "warez", "torrent", "serial", "license key",
    
    # Clickbait/Adult
    "hot", "sexy", "xxx", "adult", "dating", "nude", "leaked", "private", 
    "secret", "hidden", "exclusive video",
    
    # Fear
    "virus", "hacked", "compromised", "warning", "alert", "detected", 
    "infected", "security breach", "unauthorized",
    
    # Fake documents
    "invoice", "receipt", "payment", "statement", "report", "confidential"]
    
    
    score = 0
    fnme = filename.lower()
    
    for extension in fake_extension:
        if fnme.endswith(extension):
            score = score+2
            
    if re.search(r'\.\w+\.\w+$',fnme):
        score = score+2
        
        
    for word in fake_keywords:
        if word in fnme:
            score = score+1
            
    if score >= 3:
        return "Baiting Detected (Malicious File)"
    
    else:
        return "Safe File"
    
    
    
    
    
    
if __name__ == "__main__":
    file = input("Enter the file: ")
    result = detect_baiting(file)
    print(result)
