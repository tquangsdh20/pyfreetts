from .packages import urllib3

def get(
    self,
    url: str = "",
    headers=None,
    params=None,
    proxies=None,
    verify=True,
    timeout=None,
): ...
def post(
    self,
    url: str = "",
    headers=None,
    proxies=None,
    data=None,
    timeout=None,
    verify=True,
): ...

__all__ = ["get", "post"]
