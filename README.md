# MLops Final task<br>
Цель проекта: разработать конвеер машинного обучения data-продукта (Web или API приложение).

В ходе проекта было разработано web-приложение для выявления позитивного/негативного отзыва YELP.

## 1. Исходные коды проекта должны находятся в репозитории Git.
## 2. Проект оркестируется с помощью ci/cd (jenkins или gitlab)

![image](https://github.com/A-Kasov/ml-ops-final/assets/67365071/cdb27069-d21f-4759-a900-16f6ee6ab386)

## 3. Датасеты версионируются с помощью dvc и синхронизируются с удалённым хранилищем ([google drive](https://drive.google.com/drive/folders/1r_UeX_nNVAPzxPL3FaFvrAXWYmOnccIM?usp=drive_link))

## 4. Разработка возможностей приложения должна проводиться в отдельных ветках, наборы фичей и версии данных тоже.
   * Ветка main содержит датасет по-умлочанию
   * Ветки data_v1, data_v2, data_v3 содержат датасеты другой версии
   * Добавление новых фичей фиксировалось в ветках <br>
![image](https://github.com/A-Kasov/ml-ops-final/assets/67365071/4776e0bd-3c9d-482b-8f36-33d94d2783e8)

## 5. В коневеере запускаются не только модульные тесты, но и проверка тестами на качество данных.
**Model testing**
![image](https://github.com/A-Kasov/ml-ops-final/assets/67365071/607dcd05-ff5f-4098-848b-3a4ce6357948)
**Data quality testing** <br>
![image](https://github.com/A-Kasov/ml-ops-final/assets/67365071/458b5488-dba7-48a8-b3a5-f5f409d4f736)

## 6. Итоговое приложение реализуется в виде образа docker. Сборка образа происходит в конвеере
![image](https://github.com/A-Kasov/ml-ops-final/assets/67365071/e13e5dba-a413-43f2-a0eb-2d1d0297e97e)

## 7. В проекте может использоваться предварительно обученная модель. Обучать собственную модель не требуется.

   в проекте используется предварительно обученная модель на данных соревнования [Kaggle](https://www.kaggle.com/competitions/dl-urfu-yelp). Классификация пользователей YELP
   
# Пример работы приложения
![image](https://github.com/A-Kasov/ml-ops-final/assets/67365071/234d7bde-77af-4107-a4ea-38f55d136fed)

# Команда проекта
Команда:
* [Мирвода Артем](https://github.com/Roccowen)
* [Сергеев Илья](https://github.com/allwanttokissme)
* [Шевляков Дмитрий](https://github.com/prettygodboi)
* [Касов Артем](https://github.com/A-Kasov)
