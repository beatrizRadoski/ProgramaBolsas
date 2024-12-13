FROM python:3.11

WORKDIR C:\desafio_sprint6

COPY . .

RUN mkdir -p /root/.aws

COPY .aws /root/.aws

RUN pip install --no-cache-dir boto3

CMD ["python","desafio.py"]