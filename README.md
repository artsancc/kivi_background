# KİVİ ARKA PLAN KALDIRMA UYGULAMASI

Bu proje, görüntü işleme tekniklerini kullanarak bir görsel üzerindeki nesneleri tespit eder, sayar ve arka planını karartarak yeni bir dosya olarak kaydeder.

# Özellikler

Gürültüleri azaltmak için Gaussian Blur ve GrayScale dönüşümü.

Canny Edge Detection algoritması ile hassas sınır tespiti.

Kopuk kenarları birleştirmek için dilation tekniği.

Nesneleri orijinal resimden alıp siyah arka plana yerleştirme.

Bulunan her nesnenin merkezine numara verme ve yeşil çerçeveleme.

# Kullanılan Kütüphaneler

OpenCV (cv2)

NumPy

OS

# Teknik İşleyiş ve Kod Mantığı

Ön İşleme (Preprocessing):
Görsel, preprocess_image fonksiyonu ile işlenir. Burada Grayscale dönüşümü ile veri sadeleştirilir ve Gaussian Blur ile yüksek frekanslı gürültüler bastırılarak Canny algoritması için ideal zemin hazırlanır.

Kenar Algılama ve Morfoloji:
get_edges fonksiyonu, Canny Edge Detection kullanarak pikseller arasındaki yoğunluk değişimlerinden nesne sınırlarını çıkarır. Ardından dilate işlemi uygulanarak, nesne sınırlarındaki olası kopukluklar birleştirilir ve kapalı alanlar oluşturulur.

Kontur Analizi ve Filtreleme:
cv2.findContours ile tespit edilen sınırlar gruplanır. MIN_ALAN parametresi kullanılarak, belirlenen değerden küçük olan alanlar elenir. cv2.moments hesaplaması ile her nesnenin ağırlık merkezi bulunarak numaralandırma işlemi yapılır.

Maskeleme ve Segmentasyon:
arkaplani_siyah_yap fonksiyonunda, orijinal görüntüyle aynı boyutta siyah bir numpy dizisi oluşturulur. Tespit edilen nesnelerin içini beyaz yapan bir maske hazırlanır. Bu maske referans alınarak sadece nesneler orijinal resimden kopyalanıp siyah tuvale yapıştırılır.

#Input

![kivi](https://github.com/user-attachments/assets/4d1f8545-fca3-45cf-8903-cdb584122e8c)

#Output

![kivi_sonuc](https://github.com/user-attachments/assets/f9c49b54-439a-4c4d-a752-e63fd4a6b4f8)

# Sonuç

Konsol Çıktısı: Tespit edilen toplam nesne sayısı terminale yazdırılır.

Görsel Çıktı: Ekranda iki pencere açılır; biri kenar analizini, diğeri ise numaralandırılmış nesneleri gösterir.

Dosya Çıktısı: output/kivi_sonuc.jpg adıyla, sadece tespit edilen nesnelerin olduğu siyah arka planlı yüksek çözünürlüklü bir görsel kaydedilir.

# Kullanım Notu:
Program penceresi aktifken 'q' tuşuna basarak döngüyü sonlandırabilir ve uygulamadan güvenli bir şekilde çıkış yapabilirsiniz.
