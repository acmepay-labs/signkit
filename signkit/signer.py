import hashlib
import hmac
from typing import Union

from .encoding import b64encode


class BadSignature(Exception):
    """Raised when a signed value is malformed or was tampered with."""


class Signer:
    """Signs strings as 'value<sep>signature' using HMAC."""

    def __init__(self, key: Union[str, bytes], sep: str = ".", digest=hashlib.sha256):
        if not key:
            raise ValueError("key must not be empty")
        self.key = key.encode("utf-8") if isinstance(key, str) else key
        self.sep = sep
        self.digest = digest

    def signature(self, value: str) -> str:
        mac = hmac.new(self.key, value.encode("utf-8"), self.digest)
        return b64encode(mac.digest())

    def sign(self, value: str) -> str:
        if self.sep in value:
            raise ValueError(f"value must not contain the separator {self.sep!r}")
        return f"{value}{self.sep}{self.signature(value)}"

    def verify(self, value: str, signature: str) -> bool:
        # compare bytes, compare_digest does not accept non-ascii str
        return hmac.compare_digest(
            signature.encode("utf-8"), self.signature(value).encode("utf-8")
        )

    def unsign(self, signed: str) -> str:
        """Check the signature and return the original value."""
        if not isinstance(signed, str):
            raise BadSignature("signed value must be a string")
        value, sep, signature = signed.rpartition(self.sep)
        if not sep:
            raise BadSignature(f"no {self.sep!r} found in value")
        if not self.verify(value, signature):
            raise BadSignature("signature does not match")
        return value
