import qrcode

img = qrcode.make('https://www.instagram.com/eljn_0/')

img.save("qu.png")