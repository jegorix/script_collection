'''
Генерируем QR-код для подключения к Wi-Fi
🔹Импортировать wifi_qrcode_generator
🔹Сгенерировать QR-код
🔹Сохранить QR-код как изображение
название wifi желательно без пробела - заменить на _
pip install wifi_qrcode_generator
'''

# import wifi_qrcode_generator as qr
#
# qrCode = qr.wifi_qrcode('название WIFI', False, 'WPA', 'пароль')
# qrCode.show()
#
# qrCode.save("qrs/wifi_qr_1.png")

# import wifi_qrcode_generator as qr
#
# qrCode = qr.wifi_qrcode('ds 813_5G', False, 'WPA', '81301202412')
# qrCode.show()
#
# qrCode.save("qrs/wifi_qr_1.png")


import wifi_qrcode_generator as qr
from PIL import Image
import os

# Generate the QR code object
qrCode = qr.wifi_qrcode('название WIFI', False, 'WPA', 'пароль')

# Convert the QRCode object to an image
qrImage = qrCode.make_image(fill_color="black", back_color="white")

# Ensure the output directory exists
if not os.path.exists("qrs"):
    os.makedirs("qrs")

# Display the QR code
qrImage.show()

# Save the QR code to a file
qrImage.save("qrs/wifi_qr_1.png")