задача — внедрить модель прогнозирования дефолта в виде масштабируемого веб-сервиса, готового к промышленной эксплуатации и тестированию новых версий.

curl -X POST http://localhost:80/predict -H "Content-Type: application/json" -d '{"features": [0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 500, 0, 0, 0]}'
docker run -it --rm --name=predict_default -p=80:80 credit_web
