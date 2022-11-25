#!  download image for OS
FROM python:3.10.7   

#!create working directory
RUN mkdir /Django_login

#! copy the dat
WORKDIR /myproject/

#!ADD data to directory
ADD . /myproject

#! install dependencies  
RUN pip install --upgrade pip  

#! run this command to install all dependencies  
RUN pip install -r requirements.txt  

#! port where the Django app runs  
EXPOSE 8000  

#! start server  
CMD python manage.py runserver 0:8000