---
curso: BIGDATA
titulo: 17 - Semana 15/Actividad 15_2_Frames_en_Videos
slides: 0
fuente: 17 - Semana 15/Actividad 15_2_Frames_en_Videos.ipynb
---

<div class="cell markdown" id="Z6-MKerq6_ER">

# **Frames en Videos**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="ugOgYoi0xOnb">

``` python
!pip install opencv-python
from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import os
```

</div>

<div class="cell code" id="H5SgDoLvxOs-">

``` python
video = cv2.VideoCapture("/content/carrera.mp4")

if not video.isOpened():
    print("Error abriendo el video")

FRAME_SKIP = 30

output_folder = "/content/frames_extraidos"
os.makedirs(output_folder, exist_ok=True)
```

</div>

<div class="cell code" id="aXzhwLlZzE77">

``` python
frame_number = 0
saved_count = 0

while True:
    ret, frame = video.read()
    if not ret:
        break

    if frame_number % FRAME_SKIP == 0:
        cv2_imshow(frame)
        filename = f"{output_folder}/frame_{frame_number}.jpg"
        cv2.imwrite(filename, frame)
        print("Foto guardada: ",filename)

        saved_count += 1

    frame_number += 1

video.release()
```

</div>
