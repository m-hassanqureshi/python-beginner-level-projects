import qrcode
from PIL import Image

# Simple QR code creation
img=qrcode.make("https://github.com/m-hassanqureshi")
img.save("simple.png")

# Advanced QR code generation
advanced_qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=1)
advanced_qr.add_data("https://github.com/m-hassanqureshi")
advanced_qr.make(fit=True)
advanced_img = advanced_qr.make_image(fill_color="green", back_color="white")
advanced_img.save("advanced_qr.png")
