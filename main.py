import cv2
import numpy as np
import os


def nothing(x):
    pass

# Görseli hazırlar.
def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    return blur


def arkaplani_siyah_yap(original_img, selected_contours):
    black_background = np.zeros_like(original_img)
    mask = np.zeros(original_img.shape[:2], dtype=np.uint8)

    for cnt in selected_contours:
        # Hull kullanarak yarım ay boşluklarını kapatıyoruz
        hull = cv2.convexHull(cnt)
        cv2.drawContours(mask, [hull], -1, 255, -1)

    black_background[mask == 255] = original_img[mask == 255]
    return black_background


def main():
    path = "kivi.jpeg"
    img = cv2.imread(path)

    if img is None:
        print(f"Hata: '{path}' dosyası bulunamadı!")
        return

    cv2.namedWindow('Ayarlar')
    cv2.createTrackbar('Alt Esik', 'Ayarlar', 75, 255, nothing)
    cv2.createTrackbar('Ust Esik', 'Ayarlar', 90, 255, nothing)
    cv2.createTrackbar('Min Alan', 'Ayarlar', 4000, 6000, nothing)
    cv2.createTrackbar('Dairesellik %', 'Ayarlar', 70, 100, nothing)

    while True:
        alt_esik = cv2.getTrackbarPos('Alt Esik', 'Ayarlar')
        ust_esik = cv2.getTrackbarPos('Ust Esik', 'Ayarlar')
        min_alan = cv2.getTrackbarPos('Min Alan', 'Ayarlar')
        daire_esik = cv2.getTrackbarPos('Dairesellik %', 'Ayarlar') / 100.0

        processed = preprocess_image(img)
        # Kenarları düzenler.
        edges = cv2.Canny(processed, alt_esik, ust_esik)
        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(edges, kernel, iterations=1)

        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        output_img = img.copy()
        current_selected_contours = []
        count = 0

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > min_alan:
                perimeter = cv2.arcLength(cnt, True)
                if perimeter == 0: continue
                circularity = 4 * np.pi * (area / (perimeter * perimeter))

                if circularity > daire_esik:
                    count += 1
                    hull = cv2.convexHull(cnt)
                    current_selected_contours.append(hull)

                    cv2.drawContours(output_img, [hull], -1, (0, 255, 0), 2)

                    M = cv2.moments(hull)
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        cv2.putText(output_img, str(count), (cX, cY), 1, 1.5, (255, 0, 0), 2)

        final_result = arkaplani_siyah_yap(img, current_selected_contours)

        cv2.imshow('1. Kenar Analizi', edges)
        cv2.imshow('2. Tespit Edilenler', output_img)
        cv2.imshow('3. SONUC', final_result)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            if not os.path.exists("output"): os.makedirs("output")
            cv2.imwrite("output/kivi_sonuc.jpg", final_result)
            print("Kaydedildi!")

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
