import os
import base64


def decrypt_password(encrypted_password: str) -> str:
    """Decrypts an encrypted password using the MASTER_KEY from the environment."""
    master_key = os.getenv('MASTER_KEY')
    if not master_key:
        raise ValueError("MASTER_KEY is not set in the environment variables.")

    key_bytes = master_key.encode()
    encrypted_bytes = base64.b64decode(encrypted_password)

    decrypted = bytearray(len(encrypted_bytes))
    for i in range(len(encrypted_bytes)):
        decrypted[i] = encrypted_bytes[i] ^ key_bytes[i % len(key_bytes)]

    return decrypted.decode()