from rembg import remove
from PIL import Image
import io

# 設定檔案路徑
input_path = 'when the game is real .png' # 換成你的圖片檔名
output_path = 'when the game is real_no_bg.png'

with open(input_path, 'rb') as i:
    input_data = i.read()
    # 這裡就是你截圖中想用的那行，放在程式碼裡才有效
    output_data = remove(input_data, alpha_matting=True)
    
    with open(output_path, 'wb') as o:
        o.write(output_data)

print("完成去背！")