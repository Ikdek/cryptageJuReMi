from flask import Flask, render_template_string, request
import time

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JuReMi UwU</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #ffe6f2;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ffc5c5;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 105, 180, 0.2);
            animation: fadeIn 1s, sparkle 5s infinite;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        @keyframes sparkle {
            0% {
                box-shadow: 0 0 10px rgba(255, 105, 180, 0.2);
            }
            50% {
                box-shadow: 0 0 20px rgba(255, 105, 180, 0.5);
            }
            100% {
                box-shadow: 0 0 10px rgba(255, 105, 180, 0.2);
            }
        }
        h1 {
            text-align: center;
            color: #ff69b4;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                transform: scale(1);
            }
        }
        form {
            margin-top: 20px;
        }
        label {
            display: block;
            margin-bottom: 10px;
            color: #666;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button[type="submit"] {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background: #ff69b4;
            color: #fff;
            cursor: pointer;
            margin: 0 10px;
            transition: background 0.3s ease;
        }
        button[type="submit"]:hover {
            background: #ff3385;
        }
        #result {
            margin-top: 20px;
            padding: 10px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .time-taken {
            font-size: 14px;
            color: #666;
            margin-top: 10px;
        }
        .uwu {
            font-size: 20px;
            color: #ff69b4;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>JuReMi UwU</h1>
        <form method="post">
            <label for="key">Clé :</label>
            <input type="text" id="key" name="key" value="{{ key }}">
            <label for="string">Texte :</label>
            <input type="text" id="string" name="string" value="{{ string }}">
            <button type="submit" name="action" value="encrypt">Chiffrer</button>
            <button type="submit" name="action" value="decrypt">Déchiffrer</button>
        </form>
        {% if result %}
            <div id="result">
                Résultat : {{ result }}
            </div>
            <div class="time-taken">
                Temps pris : {{ time_taken }} secondes
            </div>
        {% endif %}
        <div class="uwu">UwU</div>
    </div>
</body>
</html>
'''

def encrypt(key, string):
    result = ""
    for i, char in enumerate(string):
        shift = (ord(char) + ord(key[i % len(key)])) % 256
        result += chr(shift)
    return result

def decrypt(key, encrypted_string):
    result = ""
    for i, encrypted_char in enumerate(encrypted_string):
        shift = (ord(encrypted_char) - ord(key[i % len(key)])) % 256
        result += chr(shift)
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        key = request.form['key']
        string = request.form['string']
        action = request.form['action']
        start_time = time.time()
        if action == 'encrypt':
            result = encrypt(key, string)
        elif action == 'decrypt':
            result = decrypt(key, string)
        end_time = time.time()
        time_taken = end_time - start_time
        return render_template_string(template, result=result, key=key, string=string, time_taken=time_taken)
    return render_template_string(template, key='', string='', result='', time_taken='')

if __name__ == '__main__':
    app.run(debug=True)
