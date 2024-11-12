from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>System Information</h1>
    <p>Go to <a href='/htop'>/htop</a> to view system information.</p>
    """

@app.route('/htop')
def htop():
    # User details
    full_name = "Yasaswi Jillellamudi"  # Updated full name
    username = "Yasaswi"  # Updated system username
    
    # Current server time in IST
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    # Get the top command output
    top_output = subprocess.getoutput("top -bn 1")

    # Generate HTML output
    html_content = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time in IST:</strong> {ist_time}</p>
    <h2>Top Output</h2>
    <pre>{top_output}</pre>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
