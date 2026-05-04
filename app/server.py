from flask import Flask, request, jsonify
import joblib
import numpy as np

# Загрузка модели напрямую с помощью joblib
model = joblib.load('GBselect_model.joblib')

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    "Test message. The server is running"
    return jsonify({'status': 'healthy'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    "Try predict"
    try:
        # Получаем список признаков из запроса
        features = request.json.get('features')

        # Проверка на наличие признаков
        if features is None:
            return jsonify({"error": "Missing 'features' key in request."}), 400
        
        # Проверка на количество признаков
        if len(features) != 15:
            return jsonify({"error": "Number of features must be exactly 15."}), 400

        # Преобразуем в массив numpy и изменяем форму
        features = np.array(features).reshape(1, 15)
        
        # Выполнение предсказания
        prediction = model.predict(features)
        
        return jsonify({'prediction': prediction.tolist()}), 200

    except Exception as e:
        # Обработка общих ошибок
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run('localhost', 5000)

