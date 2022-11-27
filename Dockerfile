FROM python

COPY requirements.txt .

COPY tether.py .

COPY apikey.py .

RUN pip install -r requirements.txt

COPY apikey.py .

CMD [ "python","./tether.py" ]
