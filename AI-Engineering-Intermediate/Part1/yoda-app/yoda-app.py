from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

# List of Yoda quotes
yoda_quotes = [
    "Do, or do not. There is no try.",
    "The greatest teacher, failure is.",
    "Pass on what you have learned.",
    "You must unlearn what you have learned.",
    "In a dark place we find ourselves, and a little more knowledge lights our way.",
    "Named must be your fear before banish it you can.",
    "Fear is the path to the dark side.",
    "Difficult to see. Always in motion is the future."
]

# Main route rendering the HTML
@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Yoda Quotes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #2c3e50;
                color: #ecf0f1;
                text-align: center;
                padding: 50px;
            }
            button {
                background-color: #3498db;
                color: #fff;
                border: none;
                padding: 10px 20px;
                font-size: 18px;
                cursor: pointer;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            button:hover {
                background-color: #2980b9;
            }
            .quote {
                font-size: 24px;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <h1>Generate Random Yoda Quotes</h1>
        <div class="quote" id="yodaQuote">Click the button to receive wisdom from Yoda.</div>
        <button onclick="fetchQuote()">Get Quote</button>

        <script>
            async function fetchQuote() {
                const response = await fetch('/get-quote');
                const data = await response.json();
                document.getElementById('yodaQuote').innerText = data.quote;
            }
        </script>
    </body>
    </html>
    ''')

# Route to provide a random quote
@app.route('/get-quote')
def get_quote():
    return jsonify(quote=random.choice(yoda_quotes))

if __name__ == '__main__':
    app.run(debug=True)