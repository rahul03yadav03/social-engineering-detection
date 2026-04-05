import re


fake_words = ["urgent", "security alert", "login", "click" , "verify", "password", "bank", "account", "confirm",
              # Urgency
    "urgent", "immediate", "now", "today", "expires", "limited time", 
    "act now", "hurry", "asap", "deadline", "final notice", "last warning",
    
    # Security/Threat
    "security alert", "suspicious activity", "unauthorized access", 
    "account locked", "breach", "compromised", "hacked", "fraud", "identity theft",
    
    # Action
    "click", "click here", "tap", "press", "download", "open", "install", 
    "update now", "verify", "validate", "authenticate",
    
    # Credentials
    "login", "password", "username", "credential", "ssn", "social security", 
    "pin", "otp", "verification code", "security question",
    
    # Financial
    "bank", "account", "credit card", "debit", "payment", "transaction", 
    "refund", "invoice", "billing", "balance", "overdue", "suspended", 
    # Trust/Fake Official
    "confirm", "secure", "official", "important", "notification", 
    "alert", "warning", "service", "support", "help desk", "admin",
    
    # Emotional/Bait
    "free", "won", "winner", "congratulations", "selected", "exclusive", 
    "special offer", "gift", "reward", "bonus", "prize"]

fake_domain = ["paypa1.com","g00gle.com","secure-bank.net" # PayPal
    "paypa1.com", "pay-pal.com", "paypal-security.com", 
    "paypal-verify.net", "secure-paypal.org",
    
    # Google
    "g00gle.com", "goog1e.com", "google-security.com", 
    "accounts-google.com", "gmail-verify.net",
    
    # Apple
    "app1e.com", "apple-id.com", "apple-security.com", 
    "icloud-verify.net", "apple-support.org",
    
    # Microsoft
    "micros0ft.com", "microsoft-security.com", "outlook-verify.net", 
    "office365-login.com", "ms-verify.org",
    
    # Banks
    "secure-bank.net", "chase-security.com", "wellsfargo-verify.net", 
    "bankofamerica-alert.com", "citibank-secure.org",
    
    # Social Media
    "faceb00k.com", "facebook-security.com", "instagram-verify.net", 
    "twitter-help.com", "linkedin-security.net", # Amazon
    "amaz0n.com", "amazon-security.com", "prime-verify.net", 
    "amazon-billing.org", "aws-secure-login.com",
    
    # Generic
    "secure-login.net", "account-verify.com", "identity-secure.org", 
    "verification-required.net", "alert-security.com"]


def check_suspicious(email):
    
    points = 0
    
    for word in fake_words:
        if word in email.lower():
            points += 1
            
    return points
    
    
def link_detect(email):
    links =  re.findall(r"http[s]?://\S+", email)
    
    suspense=[]
    
    for link in   links:
        if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", link):
            suspense.append(link)
            
        if "bit.ly" in link or "tinyurl" in link:
            suspense.append(link)
            
    return suspense

def fake_domain_detector(email):
    for domain in fake_domain:
        if domain in email:
            return domain
        
    return None

def emnail_analysis(email):
    score = check_suspicious(email)
    links = link_detect(email)
    fake_domain = fake_domain_detector(email)
    
    print("\n=====ANALYSIS RESULT=====")
    
    if score>2:
        print("Suspicious keywords Detected")
        
    if links:
        print(f"Suspicious Link Found: {links}")
        
    if fake_domain:
        print(f"Fake Domain Detected: {fake_domain}")
    
    if score > 3 or links or fake_domain:
        print("\n This email is likely phishing")
    else:
        print("\n This email looks SAFE")
        
        
        
if __name__ =="__main__":
    email = input("Please enter your url: ")
    emnail_analysis(email)
    
     