import qrcode

img = qrcode.make("Hello, This is the first one")
img.save("sampleqr.png")