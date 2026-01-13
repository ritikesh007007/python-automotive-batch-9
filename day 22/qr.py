import qrcode

doc_url = "https://docs.google.com/document/d/1rssW2-mj9RRblQ1y0ixu4MIOrnHzits1MA08fXh42GA/edit?tab=t.426n27tfmj71"

qr = qrcode.QRCode(version=1, box_size=15, border=4)
qr.add_data(doc_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("group_doc_qr.png")
print("QR saved as group_doc_qr.png - scan to access Doc!")
