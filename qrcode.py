import pyqrcode
from pyqrcode import QRCode

s = "https://github.com/OmkarSurve07/"

url = pyqrcode.create(s)

url.svg("youtube.svg", scale = 8)
