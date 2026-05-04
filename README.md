задача проекта:
Разработка и внедрение сервиса прогнозирования дефолта по кредитным картам с контейнеризацией и A/B-тестированием. Внедрить модель прогнозирования дефолта в виде масштабируемого веб-сервиса, готового к промышленной эксплуатации и тестированию новых версий.

- Домен: финансы / кредитный скоринг.
- Датасет: https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

Итоговое решения задачи: контейнеризированное  FLASK приложение на базе  образа FLASK + UWSGI + NGINX

1. Выполнен анализ и предобработка исходного датасета ( см файл scriptML_dataPreprocessing.ipynb), по результатам  проведенной аналитики используя методы из области  Feature Engineering и Feature Selection  была понижена размерность датасета и отобраны наиболее значимые признаки. Далее  было выполнено сравнение  3-х моделей ML  для решения  задачи  бинарной классификации ((LogisticRegression, RandomForestClassifier или GradientBoostingClassifier)) отобрана наиболее стабильная модель с лучшим показателем Accuracy
2. Написано приложение на FLASK для реализации возможности использования  обученной модели для предсказаний по кредитной истории, используя  документируемы POST  запрос :
   ```curl -X POST http://localhost:80/predict -H "Content-Type: application/json" -d '{"features": [0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 500, 0, 0, 0]}'```

ОТобранные признаки( описание на странице датасета):

- LIMIT_BAL   
- AGE          
- PAY_0       
- BILL_AMT1   
- BILL_AMT2 
- BILL_AMT3    
- BILL_AMT4 
- BILL_AMT5 
- BILL_AMT6  
- PAY_AMT1    
- PAY_AMT2   
- PAY_AMT3  
- PAY_AMT4  
- PAY_AMT5  
- PAY_AMT6 

3. Для  запуска  модели требуется  скачать образ docker pull elenazorge/credit_web:latest  с https://hub.docker.com  и в папке проекта выполнить запуск контейнера  docker run -it --rm --name=predict_default -p=80:80 credit_web

4. Необходимы и достаточный  набор файлов  для  запуска контейнера в папке проекта: Dockerfile, app/server.py, app/GBselect_model.joblib, requirements.txt,uwsgi.ini
5. Файл client_requests.py  - опционально реализован  скрипт  для тесттирования  подачи входных данных и предсказания
