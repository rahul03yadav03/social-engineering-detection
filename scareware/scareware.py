import re

def detect_malicious_website(url):
    
    fake_keywords = [
        "login", "verify", "secure", "authenticate", "validate", "confirm", 
        "credential", "password", "username", "signin", "unlock",
        "account", "profile", "membership", "subscription", "access", 
        "restricted", "suspended", "disabled", "locked", "terminated",
        "bank", "credit", "debit", "card", "payment", "invoice", "billing", 
        "transaction", "balance", "overdraft", "refund", "tax", "irs",
        "urgent", "immediate", "now", "today", "expires", "deadline", 
        "limited", "hours", "minutes", "final", "last", "critical", "asap",
        "virus", "malware", "hacked", "breach", "compromised", "unauthorized", 
        "suspicious", "fraud", "attack", "stolen", "leaked",
        "click", "download", "open", "install", "run", "enable", "allow", 
        "grant", "accept", "submit", "continue", "proceed",
        "alert", "warning", "notice", "notification", "attention", "important", 
        "caution", "error", "failed", "blocked",
        "free", "gift", "prize", "won", "winner", "reward", "bonus", 
        "discount", "offer", "deal", "promo", "coupon", "exclusive",
        "official", "service", "support", "help", "admin", "team", "security", 
        "protection", "guarantee", "verified", "trusted",
        "update", "upgrade", "patch", "fix", "renew", "restore", "recover", 
        "reset", "reactivate",
        # Add brand names
        "paypal", "amazon", "google", "microsoft", "apple", "facebook", 
        "netflix", "linkedin", "twitter", "instagram", "whatsapp", "paypa1"
    ]
    
    fake_keywords = list(set(fake_keywords))
    
    
    shorter = [
        "bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly", "short.link",
        "is.gd", "buff.ly", "adf.ly", "shorte.st", "bc.vc", "po.st", "cli.gs",
        "rb.gy", "cutt.ly", "short.io", "rebrand.ly", "tiny.cc", "bl.ink",
        "qr.net", "qrco.de", "goqr.me", "paypa1.com"
    ]
    
    score = 0
    
    u = url.lower()
    
    if u.startswith("http://"):
        score = score + 1
        
    if re.search(r"http[s]?://\d+\.\d+\.\d+\.\d+", u):
        score = score+2
        
    for word in fake_keywords:
        if word in u:
            score = score +1
            
    for s in shorter:
        if s in u:
            score = score + 2
            
    if u.count('.') > 3:
        score = score + 1
        
    if re.search(r'[@\-]', u):
        score = score + 1
        
        
    if score>=3:
        return f"Malicious Website Detected (score: {score})"
    
    else:
        return f"Safe Website (Score: {score})"
    

    
    
if __name__ == "__main__":
    url = input("Enter URL: ")
    result = detect_malicious_website(url)
    print(result)