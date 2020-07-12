## Flask & Heroku Model Deployment

## Gereklilikler

Repo olduğu gibi kopyalanmalı.

## Projeyi Heroku'dan Çalıştırmak için

1. Bu repo olduğu gibi kopyalanarak yeni bir repo oluşturulur. Örneğin sales_prediction isimli bir repo.
2. heroku.com'dan hesap açılır.
3. Create New App bölümünden yeni bir uygulama açılır ve isimlendirilir.
4. Deploy bölümünde yer alan "Deployment Method" bölümünden github seçilir.
5. sales_prediction isminde github'ta yer alan repo ile eşleştirme yapılır.
6. manual deploy diyerek model deploy edilir.

## Dizindeki Dosyaların Tanımları
data (klasor. icerisinde Advertising.csv dosyasi var)

templates (html template. icerisinde template.html dosyasi var)

Procfile (heroku ile flask arasındaki iletişim için kullanılır)

app.py (flask uygulamasi)

model.py (modellemenin yapildigi script)

regression_model.pkl (model nesnesi)

requirements.txt (modüller ve versiyonlarının bilgisi. heroku tarafı için çok önemlidir.)




*İstenildiği taktirde data klasörü, model.py dosyası alınmayabilir. (1. maddeyle çelişiyoruz evet). Neden? Çünkü pkl model nesnesi zaten elimizde. Bu model nesnesini oluşturmak için model.py ve data içerisindeki Advertising.csv dosyaları kullanıldı.
