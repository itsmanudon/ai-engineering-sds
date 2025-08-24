from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

# List of Yoda quotes
yoda_quotes = [
    "Do, or do not. There is no try.",
    "The greatest teacher, failure is.",
    "In a dark place we find ourselves, and a little more knowledge lights our way.",
    "Truly wonderful, the mind of a child is.",
    "Named must be your fear before banish it you can.",
    "Fear is the path to the dark side.",
    "Patience you must have, my young Padawan.",
    "When you look at the dark side, careful you must be. For the dark side looks back.",
]

@app.route('/')
def index():
    # Render a simple HTML template
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Yoda Quotes</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }
                button {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                }
                button:hover {
                    background-color: #45a049;
                }
                .quote {
                    margin-top: 20px;
                    font-size: 20px;
                    font-style: italic;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Random Yoda Quote</h1>
                <button onclick="generateQuote()">Get Quote</button>
                <div class="quote" id="quote"></div>
            </div>

            <script>
                async function generateQuote() {
                    const response = await fetch('/quote');
                    const data = await response.json();
                    document.getElementById('quote').innerText = data.quote;
                }
            </script>
        </body>
        </html>
    ''')

@app.route('/quote')
def quote():
    # Select a random quote
    quote = random.choice(yoda_quotes)
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)