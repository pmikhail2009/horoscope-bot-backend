from flask import Flask, request, jsonify
from flask_cors import CORS
from random import choice

app = Flask(__name__)
CORS(app)  # Разрешает запросы из Mini App

# Данные для генерации предсказаний
priv = ['Привет, ', 'Здравствуйте, ', 'Привяо, ', 'Хэлоу, ', 'Ку, ', 'КУ, ', 'Приветствую, ',
        'Добрый день, ', 'Здравствуй, ']
zodiak = ["овен", "телец", "близнецы", "рак", "лев", "дева", "весы",
          "скорпион", "стрелец", "козерог", "водолей", "рыбы"]
nach = [' вы увидите ', ' найдёте ', ' в ближайшем будущем вас ждёт ', ' сегодня вы увидите',
        ' завтра обнаружите ', ' в этом году вас ждёт ', ' этой ночью вы заметите ']
sred = ['приятный сюрприз ', 'подарок ', 'новость ', 'интересную вещь ', 'открытку ']
konec = ['от любимого(ой)!', 'от незнакомца!', 'из ниоткуда?!', 'от близкого!']

@app.route('/predict', methods=['POST'])
def predict():
    """API для генерации предсказания"""
    try:
        data = request.json
        zodiac = data.get('zodiac', '').lower().strip()
        
        # Проверка валидности знака зодиака
        if zodiac not in zodiak:
            return jsonify({
                'success': False,
                'error': 'Неверный знак зодиака'
            }), 400
        
        # Генерация предсказания
        prediction = choice(priv) + zodiac + choice(nach) + choice(sred) + choice(konec)
        
        return jsonify({
            'success': True,
            'prediction': prediction,
            'zodiac': zodiac
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/zodiac_list', methods=['GET'])
def zodiac_list():
    """API для получения списка знаков зодиака"""
    return jsonify({
        'success': True,
        'zodiacs': zodiak
    })

@app.route('/health', methods=['GET'])
def health():
    """Проверка работоспособности сервера"""
    return jsonify({
        'status': 'ok',
        'message': 'Flask server is running'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
