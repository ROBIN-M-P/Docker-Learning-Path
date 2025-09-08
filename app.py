from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def hello():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Portfolio</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1f1c2c, #928dab);
                color: #e0e0e0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 40px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                text-align: center;
                max-width: 600px;
                width: 90%;
            }
            .header {
                margin-bottom: 20px;
            }
            .title {
                font-size: 2.5em;
                font-weight: 700;
                color: #fff;
                margin-bottom: 10px;
            }
            .subtitle {
                font-size: 1.2em;
                font-style: italic;
                color: #ccc;
            }
            .button-group {
                margin-top: 30px;
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            .button {
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 15px 25px;
                font-size: 1em;
                color: #fff;
                text-decoration: none;
                border-radius: 8px;
                transition: transform 0.3s ease, background-color 0.3s ease;
                background: #3a3a3a;
            }
            .button:hover {
                transform: translateY(-3px);
                background: #505050;
            }
            .button img {
                margin-right: 10px;
                filter: invert(1);
            }
            .footer {
                margin-top: 40px;
                font-size: 0.9em;
                color: #aaa;
            }
            .profile-pic {
                width: 120px;
                height: 120px;
                border-radius: 50%;
                border: 3px solid #fff;
                box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <img src="https://via.placeholder.com/120" alt="Profile Picture" class="profile-pic">
                <div class="title">Hello there!</div>
                <div class="subtitle">Welcome to my personal portfolio.</div>
            </div>
            <div class="button-group">
                <a href="https://github.com/ROBIN-M-P" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub Icon" width="20"> My GitHub
                </a>
                <a href="https://www.linkedin.com/in/robinmp/" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn Icon" width="20"> My LinkedIn
                </a>
            </div>
        </div>
        <div class="footer">
            © 2025 Robin M.P. All rights reserved.
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
