FROM python:3.10
EXPOSE 7860
WORKDIR /YELP_classification
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]