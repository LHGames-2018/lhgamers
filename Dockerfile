FROM polyhx/python-seed

ADD . .

RUN pip3 install -r requirements.txt

EXPOSE 3000

CMD ["python3", "server.py"]
