import requests
from .client import API
from typing import Any, Dict


def save_audio(audio: bytes, file: str):
    with open(file, "wb") as fp:
        fp.seek(0)
        fp.write(audio)
        fp.close()


class FailRequest(Exception):
    ...


def voicemaker_convert(api: Dict[str, Any], proxy: Any = None) -> bytes:
    # Request access resourse
    if proxy is None:
        timeout, verify = None, True
    else:
        timeout, verify = 3, False
    response = requests.post(
        api["URL1"],
        headers=api["HEAD1"],
        data=api["PAYLOAD"].encode("utf-8"),
        proxies=proxy,
        timeout=timeout,
        verify=verify,
    )
    js = response.json()
    path = js["path"][1::]
    # Retriving file mp3
    response = requests.get(api["URL2"].format(path=path), headers=api["HEAD2"])
    return response.content


def freetts_convert(api: Dict[str, Any], proxy: Any = None) -> bytes:
    # Request access resourse
    if proxy is None:
        timeout, verify = None, True
    else:
        timeout, verify = 3, False
    response = requests.get(
        api["URL1"],
        headers=api["HEAD1"],
        params=api["PAYLOAD"],
        proxies=proxy,
        timeout=timeout,
        verify=verify,
    )
    js = response.json()
    # Retriving file mp3
    if js["msg"] == "Fail":
        raise FailRequest("Fail to request FreeTTS")
    else:
        response = requests.get(api["URL2"].format(path=js["id"]), headers=api["HEAD2"])
    return response.content


class Text2Speech(API):
    def convert(self, text: str, proxy: Any = None) -> bytes:
        try:
            api = self.freetts_api(text)
            self.__audio__ = freetts_convert(api, proxy)
        except FailRequest:
            api = self.voicemaker_api(text)
            self.__audio__ = voicemaker_convert(api, proxy)
        return self.__audio__

    def save_to_file(self, filename: str):
        save_audio(self.__audio__, filename)


if __name__ == "__main__":
    __api = API()
    text = "how it's going?"
    __api.setup_voice("am")
    api = __api.freetts_api(text)
    try:
        audio = freetts_convert(api)
    except FailRequest as e:
        print(e)
    else:
        # playsound(audio)
        with open("a.mp3", "wb") as fp:
            fp.seek(0)
            fp.write(audio)
            fp.close()
    __api.close()
