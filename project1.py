import qrcode
data="https://www.linkedin.com/in/raviteja-vasamsetti-2b5663299/"
qr=qrcode.make(data)
qr.save("RAVIlinkedin.png")
print("QR code generated and saved as'RAVIlinkedin.png'")
