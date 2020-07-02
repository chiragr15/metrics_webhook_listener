FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "metric_listener.py"]
EXPOSE 5000
MAINTAINER Chirag Rudresh <chiragrudresh15@gmail.com>
