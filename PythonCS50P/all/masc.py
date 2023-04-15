import cv2
import sys
# загрузка каскада Хаара для распознавания лиц
face_cascade = cv2.CascadeClassifier(face_cascade.load('haarcascade_frontalface_default.xml'))

# загрузка изображения
img = cv2.imread(sys.argv[1])

# преобразование изображения в оттенки серого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# поиск лиц на изображении
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# перебор найденных лиц и наложение маски
for (x, y, w, h) in faces:
    # координаты и размеры лица
    print("Face coordinates: x=%d, y=%d, w=%d, h=%d" % (x, y, w, h))

    # наложение маски на лицо
    mask = cv2.imread('smile.png')
    mask = cv2.resize(mask, (w, h))
    roi = img[y:y+h, x:x+w]
    mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    ret, mask_binary = cv2.threshold(mask_gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask_binary)
    img_bg = cv2.bitwise_and(roi, roi, mask=mask_binary)
    mask_fg = cv2.bitwise_and(mask, mask, mask=mask_inv)
    dst = cv2.add(img_bg, mask_fg)
    img[y:y+h, x:x+w] = dst

# отображение результата
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()