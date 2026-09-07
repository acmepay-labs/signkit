"""signkit - sign and verify strings with HMAC."""

from .encoding import b64decode, b64encode
from .signer import BadSignature, Signer

__version__ = "0.1.0"

__all__ = ["Signer", "BadSignature", "b64encode", "b64decode"]
