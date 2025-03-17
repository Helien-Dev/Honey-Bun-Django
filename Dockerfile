FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install django-components
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]