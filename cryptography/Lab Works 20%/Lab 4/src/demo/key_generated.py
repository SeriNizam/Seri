from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_keys(name):

    # generate RSA private key
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048,)

    #serialize private key to PEM format
    private_pem =private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # generate public key
    public_key= private_key.public_key()

    #serialize public key to PEM format
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format= serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save the keys to file
    with open (f"{name}_private_key.pem","wb") as private_file:
        private_file.write(private_pem)

    with open (f"{name}_public_key.pem","wb") as public_file:
        public_file.write(public_pem)

    print (f"{name} keys generated are saved!")

#generat keys for Labu and Labi
generate_rsa_keys("Labu")
generate_rsa_keys("Labi")