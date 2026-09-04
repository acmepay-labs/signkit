import base64
from typing import Union


def b64encode(data: Union[str, bytes]) -> str:
    """URL safe base64 without the '=' padding."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def b64decode(data: Union[str, bytes]) -> bytes:
    if isinstance(data, str):
        data = data.encode("ascii")
    # add back the padding we stripped in b64encode
    return base64.urlsafe_b64decode(data + b"=" * (-len(data) % 4))
