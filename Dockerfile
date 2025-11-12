#python dependancy
FROM python:3.10

#create app directory
WORKDIR /app

#copy package files first
COPY requrements.txt ./

#install required build dependancies
RUN pip install -r requrements.txt

#copy all other project files
COPY . .

#expose app port
EXPOSE 5000

#run app
CMD [ "python", "app.py" ]