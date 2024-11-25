# pip install Pillow==9.5.0
# pip install qrcode
# pip install "qrcode[pil]"

# Imports
import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# # Taking image which user wants 
# Logo_link = '/home/emanuelet/Desktop/VSCode/Python_SempreVerde/SempreVerdeSourceCode/Images/logo_QRCode.png'

# # Loading the image
# logo = Image.open(Logo_link).convert("RGBA")

# # Ajust logo size
# basewidth = 100
# wpercent = (basewidth / float(logo.size[0]))
# hsize = int((float(logo.size[1]) * float(wpercent)))
# logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

# Create base QRCode
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=9,
    border=4,
)

# Add URL to QRCode
url = 'https://github.com/emanuelet123/SempreVerde/tree/main/bin'
QRcode.add_data(url)
QRcode.make(fit=True)

# Colors
BGQRcolor = (153, 199, 124) # lightgreen
QRcolor = (29, 110, 45) # darkgreen

# Gerando o QR Code com fundo branco para posterior transparência
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color=BGQRcolor
).convert("RGBA")

# Tornando o fundo branco transparente
QRimg_data = QRimg.getdata()
new_data = []
for item in QRimg_data:
    # Se o pixel for branco, torna-o transparente
    if item[:3] == (255, 255, 255):
        new_data.append((255, 255, 255, 0))  # Transparente
    else:
        new_data.append(item)  # Cor do QR
QRimg.putdata(new_data)

# Posicionando o logo transparente no centro do QR Code
# pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
# QRimg.paste(logo, pos, logo)  # O terceiro parâmetro preserva a transparência do logo

# Salvando o QR Code final com logo e fundo transparente
QRimg.save('./QRCode/Download_APK.png')
