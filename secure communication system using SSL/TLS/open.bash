# Generate a private key for the server
openssl genpkey -algorithm RSA -out server-key.pem

# Generate a self-signed certificate for the server
openssl req -new -x509 -key server-key.pem -out server-cert.pem -days 365

# Generate the client's certificate (for testing purposes)
openssl genpkey -algorithm RSA -out client-key.pem
openssl req -new -key client-key.pem -out client-csr.pem
openssl x509 -req -in client-csr.pem -signkey client-key.pem -out client-cert.pem -days 365
