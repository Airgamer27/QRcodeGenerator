# Make sure Qrcode, Pillow are installed
import qrcode
print('qr-generator is ready')
def gen_qr(string):
    qr = qrcode.QRCode(
        box_size=1,
        border=0)

    qr.add_data(string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    bitmap_list = list(map(
        lambda x: '#' if x else '_', img.getdata()))
    return ''.join(bitmap_list)
