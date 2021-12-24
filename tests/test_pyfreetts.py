from pyfreetts import __version__
from pyfreetts import Text2Speech
from .__init__ import TEST
import unittest


def test_version():
    assert __version__ == "0.1.0"


# Text2Speech Testcase
class TestText(unittest.TestCase):
    def test_convert(self):
        module = Text2Speech()
        # English US - America
        module.setup_voice("am", 6)
        audio = module.convert("how's it going?")
        module.close()
        self.assertIsInstance(audio, bytes)
