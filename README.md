# KİVİ ARKA PLAN KALDIRMA UYGULAMASI

Bu proje, OpenCV kütüphanesi kullanarak görüntüler üzerindeki belirli nesneleri; dairesellik ve alan özelliklerine göre tespit eden, bunları sayan ve seçilen nesneleri orijinal görüntüden ayıklayarak siyah bir arka plana yerleştiren bir görüntü işleme uygulamasıdır.

# Özellikler

Dinamik Eşikleme: Trackbar (kaydırma çubukları) ile Canny kenar algılama eşiklerini anlık olarak değiştirebilme.

Akıllı Filtreleme: Nesneleri sadece boyutlarına göre değil, şekillerine göre de ayırt edebilme.

Dışbükey Gövde: Nesne kenarlarındaki pürüzleri ve boşlukları kapatarak daha düzgün bir seçim maskesi oluşturma.

Anlık Geri Bildirim: İşlenmiş kenar görüntüsü, tespit edilen nesneler ve nihai sonuç olmak üzere 3 farklı pencerede eş zamanlı izleme.

Kaydetme Seçeneği: 's' tuşuna basarak sonucu yerel dizine kaydetme imkanı.

# Kullanılan Kütüphaneler

OpenCV (cv2)

NumPy

OS

# Teknik İşleyiş ve Kod Mantığı

Kivi Tespit ve Arka Plan Temizleme Sistemi
Bu proje, OpenCV kütüphanesi kullanarak görüntüler üzerindeki belirli nesneleri dairesellik ve alan özelliklerine göre tespit eden, bunları sayan ve seçilen nesneleri orijinal görüntüden ayıklayarak siyah bir arka plana yerleştiren bir görüntü işleme projesidir.

Özellikler
Dinamik Eşikleme: Trackbar ile Canny kenar algılama eşiklerini anlık olarak değiştirebilme.

Akıllı Filtreleme: Nesneleri sadece boyutlarına göre değil, şekillerine göre de ayırt edebilme.

Dışbükey Gövde: Nesne kenarlarındaki pürüzleri ve boşlukları kapatarak daha düzgün bir seçim maskesi oluşturma.

Anlık Geri Bildirim: İşlenmiş kenar görüntüsü, tespit edilen nesneler ve nihai sonuç olmak üzere 3 farklı pencerede eş zamanlı izleme.

Kaydetme Seçeneği: 's' tuşuna basarak sonucu yerel dizine kaydetme imkanı.

# Teknik İşleyiş ve Kod Mantığı
Sistem temel olarak bir "Görüntü İşleme Hattı" üzerinde çalışır:

1. Ön İşleme (Preprocessing)

Görüntü önce gri tonlamaya çevrilir ve ardından Gaussian Blur uygulanır. Bu adım, görüntüdeki gürültüyü azaltarak kenar algılamanın daha sağlıklı çalışmasını sağlar.

2. Kenar Algılama ve Genişletme

Canny Edge Detection algoritması ile nesne sınırları belirlenir. Belirlenen sınırlar, dilate işlemi ile birleştirilerek kopuk çizgilerin önüne geçilir.

3. Kontur Analizi ve Geometrik Filtreleme

Kodun kalbi olan bu bölümde şu matematiksel filtreler uygulanır:

Alan Filtresi: Belirli bir piksel değerinden küçük olan gürültüler elenir.

Dairesellik Formülü: Nesnenin daireselliği hesaplanır.

4. Maskeleme ve Convex Hull

Tespit edilen konturlar Convex Hull yöntemiyle dıştan sarılır. Bu, meyvenin kenarlarındaki içe doğru olan girintileri kapatarak maskenin meyveyi tam kaplamasını sağlar. Ardından oluşturulan siyah maske orijinal görüntü ile çarpılarak nesne arka plandan koparılır.

#Input

![kivi](https://github.com/user-attachments/assets/4d1f8545-fca3-45cf-8903-cdb584122e8c)

#Output

![kivi_sonuc](https://github.com/user-attachments/assets/2f69c656-238b-4b54-a039-07bb0d400732)

# Sonuç

Uygulama çalıştırıldığında kullanıcıya dört temel etkileşim sunar:

1.Alt/Üst Eşik: Kenar hassasiyetini ayarlar.

2.Min Alan: Küçük toz veya gürültüleri temizler.

3.Dairesellik: Sadece kivi gibi yuvarlak formları seçer.

4.Çıktı: Tespit edilen her nesne numaralandırılır ve "SONUC" penceresinde arka planı tamamen temizlenmiş, temiz bir veri elde edilir.

# Kullanım Notu:

Program penceresi aktifken 'q' tuşuna basarak döngüyü sonlandırabilir ve uygulamadan güvenli bir şekilde çıkış yapabilirsiniz.
