# 自己署名証明書を用いたfastapiのmtlsサンプル

自分で作成するためのサンプル

## How to create cert for mTLS

1. create CA 
```
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 1024 -out ca.pem -subj "/CN=MyCA"
```

2. create server cert and signetured by CA key

```
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -config server_cert.cnf
openssl x509 -req -in server.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out server.pem -days 500 -sha256 -extfile server_cert.cnf -extensions v3_ca
```

3. create client cert and signetured by CA

```
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/CN=myclient"
openssl x509 -req -in client.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out client.pem -days 500 -sha256
```

4. wake uvicorn verver 
```
uvicorn app:app --host 0.0.0.0 --port 8000 --ssl-keyfile=server.key --ssl-certfile=server.pem --ssl-ca-certs=ca.pem --ssl-cert-reqs=2
```

5. comunicate via https

```
python client.py
```