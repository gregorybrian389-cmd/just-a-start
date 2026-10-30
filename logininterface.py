import getpass
from datetime import datetime

# --- 1. CONSTANTS ---
# Max attempts before the system locks out
MAX_ATTEMPT = 3 

# --- 2. USER DATABASE (DICTIONARY) ---
USERS = {
    'clare': {
        'password': 'pass123',
        'role': 'student'
    },
    'Admin': {
        'password': 'admin',
        'role': 'Administrator'
    },
    'guest': {
        'password': 'guest',
        'role': 'guest'
    }
}

# --- 3. DISPLAY BANNER ---
def display_banner():
    """Displays the welcome message at the start"""
    print("=" * 50)
    print("WELCOME TO BBIT LOGIN PORTAL")
    print("=" * 50)
    print() # Prints a blank line for readability

# --- 4. GET CREDENTIALS ---
def get_credentials():
    """Handles user input for the login form"""
    print("Please enter your login details")
    # .strip() removes accidental spaces, .lower() ignores Capitalization
    username = input("Enter your username: ").strip().lower()
    password = getpass.getpass("Enter your password: ").strip()
    return username, password

# --- 5. VALIDATE INPUT ---
def validate_input(username, password):
    """Checks if the user left the fields blank"""
    if not username or not password:
        print("Incorrect password (Please try again)")
        return False
    return True

# --- 6. AUTHENTICATE ---
def authenticate(username, password):
    """Checks the credentials against the user dictionary"""
    user_record = USERS.get(username)
    
    if user_record is None:
        return False # Username does not exist
    
    if user_record["password"] == password:
        return True # Password is correct
    
    return False

# --- 7. LOG FAILED ATTEMPT ---
def log_failed_attempt(username):
    """Records the time of a failed login"""
    timestamp = datetime.now()
    print(f"LOG: Failed login attempt for '{username}' at {timestamp}")

# --- 8. DISPLAY RESULTS ---
def display_result(success, username):
    """Shows success or failure message after login process"""
    if success:
        role = USERS[username]["role"]
        print("=" * 50)
        print(f"Login successful, {username}")
        # .upper() makes the role stand out as requested in your notes
        print(f"Role: {role.upper()}") 
        print("=" * 50)
    else:
        print("Unsuccessful login")

# --- 9. MAIN FUNCTION (THE MANAGER) ---
def main():
    """Orchestrates the sequence of events"""
    attempts = 0
    display_banner()
    
    while attempts < MAX_ATTEMPT:
        # Step 1: Get data
        u, p = get_credentials()
        
        # Step 2: Validate data
        if validate_input(u, p):
            
            # Step 3: Authenticate data
            if authenticate(u, p):
                display_result(True, u)
                return # Exit program on success
            else:
                # Step 4: Handle failure
                log_failed_attempt(u)
                attempts += 1
                print(f"Attempts left: {MAX_ATTEMPT - attempts}")
                print("-" * 20)
        
    print("\nACCESS DENIED: Account locked due to too many failed attempts.")

# --- 10. ENTRY POINT (THE START BUTTON) ---
if __name__ == "__main__":
    main()