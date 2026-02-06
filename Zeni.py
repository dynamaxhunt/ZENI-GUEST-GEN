from flask import Flask, Response
import random
import io

app = Flask(__name__)

# --- YOUR ACCOUNT GENERATOR LOGIC ---
def generate_accounts():
    # This simulates your Termux script. 
    # It creates text instead of a file on disk.
    accounts_text = ""
    
    for i in range(50): # Generates 50 accounts
        # Replace this logic with your actual generator math
        username = f"Guest_{random.randint(100000, 999999)}"
        password = "pass" + str(random.randint(100,999))
        accounts_text += f"{username} : {password}\n"
    
    return accounts_text

# --- THE DOWNLOAD LINK ---
@app.route('/')
def home():
    return "<h1>Generator is Running</h1><p>Use /download to get the file.</p>"

@app.route('/download')
def download_file():
    # 1. Generate the data
    content = generate_accounts()
    
    # 2. Send it as a file download
    return Response(
        content,
        mimetype="text/plain",
        headers={"Content-disposition": "attachment; filename=accounts.txt"}
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
