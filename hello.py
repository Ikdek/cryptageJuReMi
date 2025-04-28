from flask import Flask, render_template_string, request, send_file
import time
from io import BytesIO

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CryptoSecure</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Roboto+Mono&display=swap">
    <style>
        :root {
            --primary: #5e35b1;
            --primary-light: #7e57c2;
            --primary-dark: #4527a0;
            --secondary: #00acc1;
            --secondary-light: #26c6da;
            --secondary-dark: #00838f;
            --accent: #ec407a;
            --text: #212121;
            --text-light: #757575;
            --background: #f5f5f7;
            --card-bg: #ffffff;
            --border: #e0e0e0;
            --grid-color: rgba(94, 53, 177, 0.05);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: var(--background);
            color: var(--text);
            line-height: 1.6;
            background-image: 
                linear-gradient(0deg, rgba(245, 245, 247, 1) 0%, rgba(245, 245, 247, 0.98) 100%),
                repeating-linear-gradient(0deg, var(--grid-color) 0px, var(--grid-color) 1px, transparent 1px, transparent 40px),
                repeating-linear-gradient(90deg, var(--grid-color) 0px, var(--grid-color) 1px, transparent 1px, transparent 40px);
            background-size: 100% 100%, 100% 100%, 100% 100%;
        }

        .header {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            padding: 2rem 0;
            text-align: center;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .header::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, var(--secondary), var(--accent), var(--secondary));
        }

        .header h1 {
            font-weight: 600;
            font-size: 2.2rem;
            margin-bottom: 0.5rem;
        }

        .header p {
            font-weight: 300;
            font-size: 1rem;
            max-width: 600px;
            margin: 0 auto;
            opacity: 0.9;
        }

        .container {
            max-width: 900px;
            margin: 2rem auto;
            padding: 0 1.5rem;
        }

        .card {
            background-color: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            padding: 2rem;
            margin-bottom: 2rem;
            border-top: 4px solid var(--primary);
            position: relative;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--text);
            font-weight: 500;
            font-size: 0.95rem;
        }

        input[type="text"], select {
            width: 100%;
            padding: 0.75rem 1rem;
            background-color: var(--background);
            border: 1px solid var(--border);
            border-radius: 4px;
            color: var(--text);
            font-family: 'Roboto Mono', monospace;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }

        input[type="text"]:focus, select:focus {
            outline: none;
            border-color: var(--primary-light);
            box-shadow: 0 0 0 3px rgba(126, 87, 194, 0.2);
        }

        select {
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%235e35b1' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 10px center;
            background-size: 20px;
            padding-right: 40px;
        }

        .button-container {
            display: flex;
            justify-content: flex-end;
            margin-top: 1.5rem;
        }

        button {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 4px;
            background: var(--primary);
            color: white;
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
            font-size: 0.95rem;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }

        button:hover {
            background: var(--primary-dark);
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        button:active {
            transform: translateY(0);
            box-shadow: none;
        }

        .result-card {
            background-color: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            padding: 2rem;
            margin-top: 2rem;
            border-top: 4px solid var(--secondary);
        }

        .result-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid var(--border);
        }

        .result-title {
            font-weight: 600;
            color: var(--text);
            font-size: 1.1rem;
        }

        .time-taken {
            font-size: 0.85rem;
            color: var(--text-light);
        }

        #result {
            padding: 1rem;
            background-color: var(--background);
            border: 1px solid var(--border);
            border-radius: 4px;
            color: var(--text);
            font-family: 'Roboto Mono', monospace;
            font-size: 0.9rem;
            word-break: break-all;
            margin-bottom: 1.5rem;
            max-height: 200px;
            overflow-y: auto;
        }

        .action-buttons {
            display: flex;
            justify-content: flex-end;
            gap: 1rem;
        }

        .download-button, .copy-button {
            background: var(--secondary);
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .download-button:hover, .copy-button:hover {
            background: var(--secondary-dark);
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .footer {
            text-align: center;
            padding: 2rem 0;
            color: var(--text-light);
            font-size: 0.85rem;
            border-top: 1px solid var(--border);
            margin-top: 3rem;
        }

        .footer a {
            color: var(--primary);
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        /* Icons */
        .icon {
            display: inline-block;
            width: 20px;
            height: 20px;
            stroke-width: 0;
            stroke: currentColor;
            fill: currentColor;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 1.8rem;
            }

            .card, .result-card {
                padding: 1.5rem;
            }

            .action-buttons {
                flex-direction: column;
                gap: 0.75rem;
            }

            .download-button, .copy-button {
                width: 100%;
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>CryptoSecure</h1>
        <p>Solution professionnelle de chiffrement pour la sécurité de vos données</p>
    </header>

    <div class="container">
        <div class="card">
            <form method="post">
                <div class="form-group">
                    <label for="key">Clé de chiffrement</label>
                    <input type="text" id="key" name="key" value="{{ key }}" placeholder="Entrez votre clé de chiffrement">
                </div>

                <div class="form-group">
                    <label for="string">Texte à traiter</label>
                    <input type="text" id="string" name="string" value="{{ string }}" placeholder="Entrez le texte à chiffrer ou déchiffrer">
                </div>

                <div class="form-group">
                    <label for="action">Action à effectuer</label>
                    <select id="action" name="action">
                        <option value="encrypt" {% if action == 'encrypt' %}selected{% endif %}>Chiffrer</option>
                        <option value="decrypt" {% if action == 'decrypt' %}selected{% endif %}>Déchiffrer</option>
                    </select>
                </div>

                <div class="button-container">
                    <button type="submit">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"></path>
                        </svg>
                        Exécuter
                    </button>
                </div>
            </form>
        </div>

        {% if result %}
        <div class="result-card">
            <div class="result-header">
                <div class="result-title">Résultat de l'opération</div>
                <div class="time-taken">Temps d'exécution : {{ time_taken }} secondes</div>
            </div>

            <div id="result">{{ result }}</div>

            <div class="action-buttons">
                <button class="copy-button" onclick="copyResult()">
                    <svg class="icon" viewBox="0 0 24 24">
                        <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"></path>
                    </svg>
                    Copier le résultat
                </button>

                <form action="/download_log" method="post" style="display: inline;">
                    <input type="hidden" name="log_data" value="{{ log_data }}">
                    <button class="download-button" type="submit">
                        <svg class="icon" viewBox="0 0 24 24">
                            <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"></path>
                        </svg>
                        Télécharger le log
                    </button>
                </form>
            </div>
        </div>
        {% endif %}
    </div>

    <footer class="footer">
        <p>© 2025 CryptoSecure. Tous droits réservés. Solution de chiffrement professionnelle.</p>
    </footer>

    <script>
        function copyResult() {
            var resultText = document.getElementById("result").textContent;
            navigator.clipboard.writeText(resultText).then(function() {
                alert("Résultat copié dans le presse-papiers !");
            }, function(err) {
                console.error("Erreur lors de la copie : ", err);
            });
        }
    </script>
</body>
</html>
'''


def encrypt(key, string):
    result = ""
    for i, char in enumerate(string):
        shift = (ord(char) + ord(key[i % len(key)])) % 256
        result += chr(shift)
    return result.encode('latin1').decode('latin1')


def decrypt(key, encrypted_string):
    result = ""
    for i, encrypted_char in enumerate(encrypted_string):
        shift = (ord(encrypted_char) - ord(key[i % len(key)])) % 256
        result += chr(shift)
    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    action = 'encrypt'  # Default value
    if request.method == 'POST':
        key = request.form['key']
        string = request.form['string']
        action = request.form['action']
        start_time = time.time()
        if action == 'encrypt':
            result = encrypt(key, string)
        elif action == 'decrypt':
            result = decrypt(key, string.encode('latin1').decode('latin1'))
        end_time = time.time()
        time_taken = round(end_time - start_time, 4)
        log_data = f"Action: {action}\nClé: {key}\nTexte: {string}\nRésultat: {result}\nTemps pris: {time_taken} secondes"
        return render_template_string(template, result=result, key=key, string=string, time_taken=time_taken,
                                      log_data=log_data, action=action)
    return render_template_string(template, key='', string='', result='', time_taken='', log_data='', action=action)


@app.route('/download_log', methods=['POST'])
def download_log():
    log_data = request.form['log_data']
    return send_file(BytesIO(log_data.encode()), as_attachment=True, download_name='log.txt')


if __name__ == '__main__':
    app.run(debug=True)