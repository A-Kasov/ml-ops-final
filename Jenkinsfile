pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'data_v1', url: 'https://github.com/A-Kasov/ml-ops-final.git'
            }
        }
        stage('Install requirements') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage('Downloading data') {
            steps {
                sh 'dvc fetch model/my_model.h5'
                sh 'dvc fetch model/tokenizer.pkl'
                sh 'dvc fetch data/YELP_data.csv'
                sh 'dvc pull'
            }
        }
        stage('Data quality testing') {
            steps {
                sh 'python3 -m pytest ./tests/test_dataset.py'
            }
        }
        stage('Data preprocess') {
            steps {
                sh 'python3 ./src/data_preprocess.py'
            }
        }
        stage('Model testing') {
            steps {
                sh 'python3 -m pytest ./tests/test_model.py'
            }
        }
        stage('Docker build') {
            steps {
                sh 'sudo docker build -t yelp-classifier .'
            }
        }
        stage('Docker run') {
            steps {
                sh 'sudo docker run -d -p 7860:7860 yelp-classifier'
                sh 'sleep 15s'
            }
        }
        stage('Gradio test') {
            steps {
                sh 'python3 -m pytest ./tests/test_gradio.py'
            }
        }
    }
}
