import os
import sys
from colorama import init, Fore

init(autoreset=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from baiting.baiting import detect_baiting
from phishing_email.email import emnail_analysis
from scareware.scareware import detect_malicious_website
from smishing.smishng import detect


def main():
    
    sel = input(Fore.GREEN+"Select the type of social engineering attack to analyze (1: Phishing Email, 2: Smishing, 3: Baiting, 4: Scareware): ")
    if sel == "1":
        
        try:
            
            selection = input("Do you want to analysis a file or input the email line by line? (file/line): ")
            if selection.lower() == "file":
                file = input("Please enter the file name: ")
                with open(file, "r") as f:
                    email_content = f.read()
                result = emnail_analysis(email_content)
                return result
            
            elif selection.lower() == "line":
                email = input(Fore.GREEN+"Enter your Email content: ")
                result =  emnail_analysis(email)
                return result
        
        except Exception as e:
            return Fore.RED+ f"An error occurred: {e}"
        
        
    elif  sel == "2":
        try:
            selection = input("Do you want to analysis a file or input the SMS line by line? (file/line): ")
            
            if selection.lower() == "file":
                file = input("Please enter the file name: ")
                with open(file, "r") as f:
                    sms_conetent = f.read()
                result = detect(sms_conetent)
                return result
            
        
            
            elif selection.lower() =="line":
                sms = input(Fore.GREEN+"Enter your SMS message: ")
                result =    detect(sms)
                return result
    
        except Exception as e:
            return Fore.RED+f"An error occurred: {e}"
    
    elif sel== "3":
        try:
            selection = input("Do you want to analysis a file or input the baiting content line by line? (file/line): ")
            if selection.lower() == "file":
                file = input("Please enter the file name: ")
                with open(file, "r") as f:
                    baiting_content = f.read()
                    result = detect_baiting(baiting_content)
                    return result
                
            elif selection.lower() == "line":
                file = input(Fore.GREEN+"Enter the file name:")
                result = detect_baiting(file)
                return file
            
        except Exception as e:
            return Fore.RED+f"An error occured: {e}"
    
    elif sel == "4":
        try:
            selection = input("Do you want to analysis a file or input the URL line by line? (file/line): ")
            if selection.lower() == "file":
                file = input("Please enter the file name: ")
                with open(file, "r") as f:
                    url = f.read()
                result = detect_malicious_website(url)
                return result
            
            elif selection.lower() == "line":
                url = input(Fore.GREEN+"Enter URL:")
                result = detect_malicious_website(url)
                return result
            
        except Exception as e:
            return Fore.RED+f"An error occured: {e}"
    
    else:
        return Fore.RED+ "Invalid selection. Please choose a number between 1 and 4."    

    
    
if __name__=="__main__":
        
        print(Fore.BLUE+"Welcome to the Social Engineering Detection CLI!")
        f_result = main()
        print(f_result)
        
    
    
    

       
        
        