import re
def detect(message):
    
    malicious_word = ["urgent", "win", "free", "prize", "click", "verify", "account", "bank", "password", "otp", "limited", 
                      "offer", "congratulations","claim", "lottery",
                      
                      
    # Urgency
    "urgent", "immediate", "now", "hurry", "quick", "fast", "rush", "asap", 
    "expires", "deadline", "limited", "last chance", "final notice", "act now", 
    "don't wait", "today only", "ends soon", "running out",
    
    # Win/Reward
    "win", "winner", "won", "prize", "reward", "gift", "free", "bonus", 
    "jackpot", "lottery", "sweepstakes", "giveaway", "lucky", "selected", 
    "chosen", "exclusive", "special", "congratulations", "celebrate",
    
    # Action/Click
    "click", "tap", "press", "here", "link", "open", "download", "install", 
    "run", "enable", "allow", "grant", "accept", "submit", "continue", 
    "proceed", "verify", "confirm", "validate", "authenticate", "complete",
    
    # Account/Security
    "account", "profile", "login", "signin", "password", "credential", 
    "username", "otp", "pin", "code", "security", "secure", "protected", 
    "locked", "suspended", "disabled", "unauthorized", "breach", "compromised", 
    "hacked", "suspicious", "fraud", "stolen",
    
    # Financial
    "bank", "credit", "debit", "card", "payment", "money", "cash", "fund", 
    "transfer", "transaction", "invoice", "billing", "refund", "tax", "irs", 
    "balance", "overdue", "debt", "loan", "investment", "crypto", "bitcoin", 
    "wallet",
    
    # Claim/Collect
    "claim", "collect", "redeem", "activate", "register", "unlock", "access", 
    "retrieve", "recover", "restore", "reset", "update", "upgrade", "renew",
    
    # Trust/Fake Official
    "official", "verified", "trusted", "secure", "guaranteed", "authorized", 
    "certified", "legitimate", "genuine", "authentic", "service", "support", 
    "help", "admin", "team", "department", "agency",
    
    # Fear/Threat
    "warning", "alert", "notice", "attention", "important", "caution", "error", 
    "failed", "blocked", "terminated", "closed", "suspended", "violation", 
    "penalty", "fine", "legal", "lawsuit", "police", "arrest",
    
    # Offer/Deal
    "offer", "deal", "discount", "sale", "promo", "promotion", "coupon", 
    "voucher", "cashback", "save", "cheap", "best price", "order now", 
    "buy now", "shop now", "limited stock"
]
    
    score = 0
    msg = message.lower()
    
    
    for word in malicious_word:
        if word in msg:
            score = score+1
            
            
    
    
    
    url = re.findall(r'http[s]?://\S+|www\.\S+', message)
    
    if url:
        
        score = score+2
        
        
        
        
    if re.search(r'\d{4,}', message):
        score = score + 1
        
        
        
        
    if score >=3:
        return "Smishing Detected (Suspicious message)"
    
    else:
        return "Legitimate Message"
        
   
    
if __name__ == "__main__":
    
    sms = input("Enter SMS message: ")
    result = detect(sms)
    print(result)