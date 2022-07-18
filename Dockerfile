FROM python:3.9
COPY ruapehu.py /
COPY requirements.txt /

RUN python3 -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir --requirement requirements.txt

CMD [ "python3", "./ruapehu.py" ]

