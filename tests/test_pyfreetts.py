from pyfreetts import __version__
from pyfreetts import Text2Speech
import unittest
from pyfreetts.tts import voicemaker_convert


def test_version():
    assert __version__ == "0.1.0"


def test_voicemaker_convert():
    api = Text2Speech()
    api.setup_voice("am", 6)
    myAPI = api.voicemaker_api("how it's going?")
    audio0 = voicemaker_convert(myAPI)
    myAPI = api.freetts_api("how it's going?")
    myAPI["PAYLOAD"] = (
        ("Language", "am"),
        ("Voice", "test"),
        ("TextMessage", "text"),
        ("id", "test"),
        ("type", "1"),
    )
    # audio1 = voicemaker_convert(myAPI, PROXY2)
    api.close()
    assert isinstance(audio0, bytes)


class TestText(unittest.TestCase):
    def test_convert(self):
        # English US - America
        api = Text2Speech()
        api.setup_voice("am", 6)
        audio = api.convert("how's it going?")
        api.save_to_file("test.mp3")
        # api.convert("how's it going?",PROXY1)
        api.voicemaker_api("how's it going?")
        api.setup_voice("vi", 1)
        api.freetts_api("test_vi")
        api.close()
        self.assertIsInstance(audio, bytes)

    def test_choice_voice(self):
        api = Text2Speech()
        api.setup_voice("br", 2)
        api.close()
        self.assertIsInstance(api.freetts_api("test"), dict)
        self.assertIsInstance(api.voicemaker_api("test"), dict)


if __name__ == "__main__":
    unittest.main()
