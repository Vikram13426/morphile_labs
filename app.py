# app.py
from flask import Flask, render_template
import subprocess
import pytz
from datetime import datetime
import getpass
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get username
    username = getpass.getuser()
    
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Get top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode()
    
    # Format the response
    response = f"""Name: your_name
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}"""
    
    # Return plain text response
    return response, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


