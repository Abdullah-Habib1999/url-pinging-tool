from flask import Flask, render_template, request
import requests
import webbrowser
import threading

app = Flask(__name__)

# Function to ping a URL
def ping_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"Successfully pinged {url} - Status Code: {response.status_code}"
        else:
            return f"Failed to ping {url} - Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error pinging {url}: {e}"

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        urls_input = request.form['urls']
        urls_to_ping = urls_input.strip().splitlines()
        for url in urls_to_ping:
            result = ping_url(url)
            results.append(result)
    return render_template('index.html', results=results)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    # Run the Flask app in a separate thread
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
