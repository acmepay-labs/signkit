# signkit

Tiny helpers for signing and verifying strings with HMAC.
Standard library only.

## Install

```bash
pip install .
```

## Usage

```python
from signkit import BadSignature, Signer

signer = Signer("my-secret-key")

signed = signer.sign("user-42")   # 'user-42.<signature>'

try:
    value = signer.unsign(signed)  # 'user-42'
except BadSignature:
    print("tampered or invalid")
```

The separator (default `.`) and the hash function (default SHA-256) can be changed:

```python
import hashlib

signer = Signer("my-secret-key", sep=":", digest=hashlib.sha512)
```

### Base64 helpers

URL safe base64 without padding, handy for putting data in a signed value:

```python
from signkit import b64decode, b64encode

encoded = b64encode('{"id": 42}')
b64decode(encoded)  # b'{"id": 42}'
```
