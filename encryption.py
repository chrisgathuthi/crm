import base64

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from django.conf import settings

# Load the certificate from the certificate file
with open('ProductionCertificate.cer', 'rb') as cert_file:
    certificate = x509.load_pem_x509_certificate(cert_file.read(), default_backend())

# Load the public key from the certificate
public_key = certificate.public_key()

# Encrypt your password using PKCS #1.5 padding
password = ''.encode('utf-8')  # Replace with your actual password
encrypted_password = public_key.encrypt(
    password,
    padding.PKCS1v15()
)

base64_encrypted_password = base64.b64encode(encrypted_password).decode('utf-8')
print(base64_encrypted_password)
