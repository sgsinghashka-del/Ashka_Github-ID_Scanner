import qrcode
import cv2
import numpy as np
import random

# Your GitHub profile
github_url = "https://github.com/sgsinghashka-del"

# Choose one random Instagram-style color
fill_color = (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
)

back_color = (255, 255, 255)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=4,
)

qr.add_data(github_url)
qr.make(fit=True)

img = qr.make_image(fill_color=fill_color, back_color=back_color)
img = img.convert("RGB")

# Save QR for resume
img.save("github_qr_resume.png")

# Show once on screen
open_cv_img = np.array(img)
open_cv_img = cv2.cvtColor(open_cv_img, cv2.COLOR_RGB2BGR)

cv2.imshow("GitHub QR Code", open_cv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("QR Code saved as github_qr_resume.png")