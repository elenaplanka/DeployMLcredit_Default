       
import requests

if __name__ == '__main__':
    # Формируем данные, добавив ключ 'features'
    data = {
        "features": [20000,24,0,15376,18010,17428,18338,17905,19104,3200,0,500,0,1650,0] 
    }
    
    # Выполняем POST-запрос на сервер по эндпоинту /predict с параметром json
    r = requests.post('http://localhost:5000/predict', json=data)
    
    # Выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    
    # Реализуем обработку результата
    if r.status_code == 200:
        # Если запрос выполнен успешно (код обработки=200)
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # Если запрос завершён с кодом, отличным от 200
        # выводим содержимое ответа
        print(r.text)