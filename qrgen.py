import qrcode as qr
data="www.chess.com"
img=qr.make(data)
img.save("myqr.png")