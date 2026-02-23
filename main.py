import cv2
import numpy as np
import os

# Görseli hazırlar.
def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    return blur

# Kenarları düzenler.
def get_edges(img, low, high):
    edges = cv2.Canny(img, low, high)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)
    return edges, dilated

def arkaplani_siyah_yap(original_img, selected_contours, filename):
    # Orijinal görüntüyle aynı boyutta, tamamen siyah bir tuval oluşturur.
    black_background = np.zeros_like(original_img)

    # Sadece seçilen nesnelerin içini beyaz yapan bir maske oluşturur.
    mask = np.zeros(original_img.shape[:2], dtype=np.uint8)
    for cnt in selected_contours:
        cv2.drawContours(mask, [cnt], -1, 255, -1)

    # Maskeyi kullanarak orijinal resimdeki nesneleri siyah tuvale kopyalar.
    black_background[mask == 255] = original_img[mask == 255]

    if not os.path.exists("output"):
        os.makedirs("output")

    cv2.imwrite(f"output/kivi_sonuc.jpg", black_background)
    print(f"kivi_sonuc.jpg' olarak kaydedildi!")


def main():
    ALT_ESIK = 160
    UST_ESIK = 40
    MIN_ALAN = 2000

    path = "kivi.jpeg"
    img = cv2.imread(path)

    if img is None:
        print(f"Hata: '{path}' dosyası bulunamadı!")
        return

    processed_base = preprocess_image(img)
    edges, dilated = get_edges(processed_base, ALT_ESIK, UST_ESIK)

    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = img.copy()
    current_selected_contours = []
    count = 0

    for cnt in contours:
        if cv2.contourArea(cnt) > MIN_ALAN:
            count += 1
            current_selected_contours.append(cnt)

            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX, cY = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
                cv2.drawContours(output, [cnt], -1, (0, 255, 0), 2)
                cv2.putText(output, str(count), (cX - 10, cY),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.putText(output, f"Bulunan Nesne: {count}", (20, 40), 1, 1.5, (0, 0, 255), 2)

    cv2.imshow('Tespit Edilen Nesneler', output)
    cv2.imshow('Kenar Analizi (Canny)', edges)

    print(f"Toplam {count} nesne bulundu. Kaydediliyor...")

    arkaplani_siyah_yap(img, current_selected_contours, "tespit_edilen_nesneler")

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # 'q' tuşuna basılırsa döngüden çık
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()