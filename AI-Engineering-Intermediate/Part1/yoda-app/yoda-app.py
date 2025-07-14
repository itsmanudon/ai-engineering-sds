from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

YODA_QUOTES = [
    "Do or do not. There is no try.",
    "The greatest teacher, failure is.",
    "Train yourself to let go of everything you fear to lose.",
    "Fear is the path to the dark side.",
    "Named must be your fear before banish it you can.",
    "You must unlearn what you have learned.",
    "Pass on what you have learned.",
    "Difficult to see. Always in motion is the future.",
    "Adventure. Excitement. A Jedi craves not these things.",
    "Size matters not. Look at me. Judge me by my size, do you?",
    "Much to learn, you still have.",
    "Truly wonderful, the mind of a child is.",
    "In a dark place we find ourselves, and a little more knowledge lights our way.",
]

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <title>Yoda Quote Generator</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        html, body {
            min-height: 100%;
        }
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(120deg, #313860 0%, #55c663 100%);
            min-height: 100vh;
            margin: 0;
            padding: 0;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: rgba(40,50,70,0.95);
            border-radius: 20px;
            box-shadow: 0 6px 24px rgba(0,0,0,.1);
            padding: 40px 30px 30px 30px;
            display: flex;
            flex-direction: column;
            align-items: center;
            max-width: 430px;
            width: 95vw;
        }
        h1 {
            font-weight: 800;
            letter-spacing: 1px;
            margin-bottom: 18px;
            font-size: 2rem;
            color: #dbfa6c;
            text-shadow: 2px 4px 12px #222a;
        }
        .quote-box {
            min-height: 80px;
            margin-bottom: 24px;
            color: #f4ffe0;
            font-size: 1.3rem;
            text-align: center;
            transition: color .19s, filter .19s;
            line-height: 1.5;
            font-style: italic;
            font-family: 'Georgia', serif;
        }
        button {
            background: linear-gradient(90deg,#8ae231,#42d492);
            color: #133913;
            border: none;
            border-radius: 9px;
            padding: 14px 35px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: background .18s, transform .12s, box-shadow .18s;
            box-shadow: 0 2px 14px rgba(0,0,0,0.08);
        }
        button:hover, button:focus {
            background: linear-gradient(90deg,#42d492,#8ae231);
            transform: scale(1.04);
            outline: none;
        }
        .footer {
            margin-top: 44px;
            font-size: 0.95rem;
            color: #f7ffb7aa;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Yoda Quote Generator</h1>
        <div class="quote-box" id="quote-box">"{{ first_quote }}"</div>
        <button id="new-quote-btn">Give me Yoda wisdom</button>
    </div>
    <div class="footer">
        Generated with Python &middot; May the Force be with you
    </div>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        const btn = document.getElementById('new-quote-btn');
        const box = document.getElementById('quote-box');

        btn.onclick = function() {
            btn.disabled = true;
            box.style.filter = "blur(2px)";
            fetch("/api/quote")
                .then(res => res.json())
                .then(data => {
                    // Quote fade effect
                    box.style.transition = "color 0.24s, filter 0.24s";
                    box.style.color = "#fff0";
                    setTimeout(() => {
                        box.textContent = '"' + data.quote + '"';
                        box.style.color = "#f4ffe0";
                        box.style.filter = "none";
                        btn.disabled = false;
                    }, 240);
                })
                .catch(() => {
                    box.textContent = '"Failed to fetch wisdom. Try again."';
                    box.style.color = "#ffe0e0";
                    box.style.filter = "none";
                    btn.disabled = false;
                });
        };
    });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    first_quote = random.choice(YODA_QUOTES)
    return render_template_string(TEMPLATE, first_quote=first_quote)

@app.route('/api/quote')
def random_quote():
    quote = random.choice(YODA_QUOTES)
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)