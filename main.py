import qrcode

#Texto a codificar
texto = "https://github.com/bje-dev"

qr = qrcode.QRCode(version=1, box_size=10, border=2)
qr.add_data(texto)
qr.make(fit=True)

imagen_qr = qr.make_image(fill_color="blue", back_color="white")
imagen_qr.save("codigo_qr.png")




