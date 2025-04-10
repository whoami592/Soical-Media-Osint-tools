import requests
import time

# Metadata
__author__ = "Mr. Sabaz Ali Khan"
__tool_name__ = "Social Media OSINT Tool"
__version__ = "1.0"
__date__ = "April 10, 2025"

# Define social media platforms and their username URL templates
PLATFORMS = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",  # Note: LinkedIn may require more specific handling
    "Facebook": "https://www.facebook.com/{}"
}

def check_username(username):
    """
    Check if a username exists on various social media platforms.
    Args:
        username (str): The username to search for.
    """
    print(f"\n[+] Starting OSINT scan for username: {username}")
    print(f"[+] Tool by {__author__} | Version: {__version__} | Date: {__date__}\n")
    
    for platform, url_template in PLATFORMS.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, timeout=5)
            # Check status code (200 usually means the profile exists)
            if response.status_code == 200:
                print(f"[+] {platform}: Profile found - {url}")
            elif response.status_code == 404:
                print(f"[-] {platform}: Profile not found (404)")
            else:
                print(f"[!] {platform}: Unexpected status code ({response.status_code}) - {url}")
        except requests.RequestException as e:
            print(f"[!] {platform}: Error checking - {e}")
        
        # Avoid hitting rate limits
        time.sleep(1)

def main():
    print(f"Welcome to {__tool_name__} by {__author__}")
    print("This tool checks for username existence across social media platforms.\n")
    
    # Get username input from the user
    username = input("Enter the username to scan: ").strip()
    
    if not username:
        print("[!] Error: Username cannot be empty.")
        return
    
    # Run the OSINT check
    check_username(username)
    
    print("\n[+] Scan completed.")

if __name__ == "__main__":
    main()