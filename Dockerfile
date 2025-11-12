FROM python:3.10
WORKDIR /app
COPY requrements.txt ./
RUN pip install -r requrements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "app.py" ]