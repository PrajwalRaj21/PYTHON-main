import qrcode
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size =5,
    border =4

    
)

qr.add_data("https://www.instagram.com/rp_rmcf1/")
img = qr.make_image()
img.save("myinsta_QR.png")
