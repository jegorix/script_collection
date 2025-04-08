'''
Генерируем QR-код для подключения к Wi-Fi
🔹Импортировать wifi_qrcode_generator
🔹Сгенерировать QR-код
🔹Сохранить QR-код как изображение
pip install wifi_qrcode_generator
'''

import wifi_qrcode_generator as qr

qrCode = qr.wifi_qrcode('название WIFI', False, 'WPA', 'пароль')
qrCode.show()

qrCode.save("qrs/wifi_qr_1.png")