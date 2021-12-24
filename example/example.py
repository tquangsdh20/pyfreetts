from pyfreetts import Text2Speech


module = Text2Speech()
# 'am' = English US
# 'br' = English UK
# Others language follow the ISO-Language Code
module.setup_voice('am')
module.convert('how are you?')
module.save_to_file('test.mp3')
module.close()