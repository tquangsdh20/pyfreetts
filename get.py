from hideip import HideMe

# The path file socks5.csv
file = "socks5.csv"
hide = HideMe(file)

# Get the avaiable proxy
for i in range(3):
    proxy = hide.torrent()
    print(proxy)
