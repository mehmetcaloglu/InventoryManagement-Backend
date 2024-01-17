from uygulama_adi.models import Category,Product

# Ürünlerin listesi
urunler = [
  {
    "name": "Faber-Castell 24 Renkli Kalem Seti",
    "description": "Yüksek kaliteli renkli kalemlerle tamamlanmış 24 adet set.",
    "category": "Boya Kalemleri",
    "price": 49.99,
    "desi": 0.3
  },
  {
    "name": "Moleskine Hard Cover İnce Defter",
    "description": "Sert kapaklı, 100 sayfalık defter.",
    "category": "Defterler",
    "price": 19.99,
    "desi": 0.2
  },
  {
    "name": "Parker Urban Gold Gold Trim Dolma Kalem",
    "description": "Şık ve zarif dolma kalem modeli.",
    "category": "Dolma Kalemler",
    "price": 299.99,
    "desi": 0.1
  },
  {
    "name": "Stabilo BOSS Fluo Kalem Seti",
    "description": "4 farklı neon renkli fluo kalemlerle komple set.",
    "category": "Yapışkan ve İşareeyiciler",
    "price": 19.99,
    "desi": 0.15
  },
  {
    "name": "Herlitz Renkli Cili Spiralli Ajanda",
    "description": "Renkli cilt kaplamalı, spiral bağlantılı ajanda.",
    "category": "Ajandalar",
    "price": 29.99,
    "desi": 0.3
  },
  {
    "name": "Uni-Ball Jetstream Yeniden Dolan Roller Kalem",
    "description": "Hızlı kuruyan mürekkep ile sürekli pürüzsüz yazı yazma deneyimi sunan roller kalem.",
    "category": "Roller Kalem ve Tükenmez Kalemler",
    "price": 14.99,
    "desi": 0.05
  },
  {
    "name": "Staeder Noris HB Kurşun Kalem Seti",
    "description": "12 adet HB kurşun kalem seti.",
    "category": "Kurşun Kalemler",
    "price": 9.99,
    "desi": 0.1
  },
  {
    "name": "Pilot FriXion Tükenmez Kalem Seti",
    "description": "3 adet silinebilir tükenmez kalem ve 6 adet ek yedek uçtan oluşan set.",
    "category": "Tükenmez Kalemler",
    "price": 39.99,
    "desi": 0.2
  },
  {
    "name": "Casio FX-82EX Bilimsel Hesap Makinesi",
    "description": "Bilimsel hesaplamalar ve istatistik için ideal, kullanıcı dostu hesap makinesi.",
    "category": "Hesap Makinesi",
    "price": 69.99,
    "desi": 0.2
  },
  {
    "name": "Tesa Extra Güçlü Bant Rulo",
    "description": "Güçlü yapışma özelliği ile tüm yapıştırma ihtiyaçlarını karşılar.",
    "category": "Yapıştırıcılar ve Banar",
    "price": 9.99,
    "desi": 0.1
  },
  {
    "name": "Schneider Slider Basic Toplu Kalem Seti",
    "description": "10 adet siyah ve mavi renkte toplu kalem set.",
    "category": "Kalem Seeri",
    "price": 24.99,
    "desi": 0.2
  },
  {
    "name": "Deri Kapaklı A5 Spiral İnce Defter",
    "description": "Şık deri kapaklı, 80 sayfalık A5 boyutunda ince defter.",
    "category": "Defterler",
    "price": 17.99,
    "desi": 0.15
  },
  {
    "name": "Miffy Kawaii Anahtarlık",
    "description": "Sevimli Miffy karakterli kawaii anahtarlık.",
    "category": "Anahtarlıklar",
    "price": 9.99,
    "desi": 0.05
  },
  {
    "name": "Tombow Dual Brush Kalem Seti",
    "description": "12 adet farklı renkte çift uçlu kalem set.",
    "category": "Boya Kalemleri",
    "price": 59.99,
    "desi": 0.2
  },
  {
    "name": "Pilot G-2 0.7 Jel Kalem",
    "description": "Sıvı mürekkepli ve 0.7 uçlu jel kalem.",
    "category": "Roller Kalem ve Tükenmez Kalemler",
    "price": 5.99,
    "desi": 0.05
  },
  {
    "name": "Faber-Castell PITT Artist Kalem Seti",
    "description": "8 adet F, S ve B uçlu artist kalemden oluşan set.",
    "category": "Sanat Kalemleri",
    "price": 34.99,
    "desi": 0.15
  },
  {
    "name": "Oxford Lined Grid İnce Defter",
    "description": "Çizgili ve kareli grid baskılı, 80 sayfalık ince defter.",
    "category": "Defterler",
    "price": 12.99,
    "desi": 0.1
  },
  {
    "name": "BIC Cristal Original Tükenmez Kalem",
    "description": "Uzun süre dayanan, siyah mürekkepli tükenmez kalem.",
    "category": "Tükenmez Kalemler",
    "price": 3.99,
    "desi": 0.05
  },
  {
    "name": "Durable Color Klas Belge Dosyası",
    "description": "Renkli plastik kapaklı, A4 boyutunda belge dosyası.",
    "category": "Dosya ve Klasörler",
    "price": 6.99,
    "desi": 0.1
  },
  {
    "name": "Zebra Mildliner Çift Uçlu Pastel Kalem Seti",
    "description": "5 adet farklı renkte pastel tonlu çift uçlu kalem set.",
    "category": "Keçeli ve Highlighter Kalemler",
    "price": 19.99,
    "desi": 0.15
  },
  {
    "name": "Stabilo Point 88 Renkli Kalemler Seti",
    "description": "20 adet farklı renkte ince uçlu renkli kalem seti.",
    "category": "Boya Kalemleri",
    "price": 39.99,
    "desi": 0.2
  },
  {
    "name": "Maped Color'Peps Keçeli Kalem Seti",
    "description": "12 adet farklı renkte keçeli kalem seti.",
    "category": "Keçeli Kalemler",
    "price": 19.99,
    "desi": 0.15
  },
  {
    "name": "Pilot G-Tec C4 Jel Kalem Seti",
    "description": "5 adet siyah jel kalem seti.",
    "category": "Roller Kalem ve Tükenmez Kalemler",
    "price": 24.99,
    "desi": 0.1
  },
  {
    "name": "Fabriano Yumuşak Kapaklı Spiral Defter",
    "description": "Yumuşak kapaklı, 120 sayfalık spiral defter.",
    "category": "Defterler",
    "price": 14.99,
    "desi": 0.2
  },
  {
    "name": "Lamy Safari Fountain Kalem Seti",
    "description": "3 adet farklı renkte Lamy Safari dolma kalem seti.",
    "category": "Dolma Kalemler",
    "price": 149.99,
    "desi": 0.1
  },
  {
    "name": "Stabilo Swing Cool Renkli Tükenmez Kalem Seti",
    "description": "8 adet farklı renkte Stabilo Swing Cool tükenmez kalem seti.",
    "category": "Tükenmez Kalemler",
    "price": 19.99,
    "desi": 0.1
  },
  {
    "name": "Moleskine Pocket Soft Cover Ajanda",
    "description": "Yumuşak kapaklı, cepli ajanda.",
    "category": "Ajandalar",
    "price": 34.99,
    "desi": 0.2
  },
  {
    "name": "Faber-Castell 36 Renkli Keçeli Kalem Seti",
    "description": "Yüksek kaliteli keçeli kalemlerle tamamlanmış 36 adet set.",
    "category": "Keçeli Kalemler",
    "price": 59.99,
    "desi": 0.3
  },
  {
    "name": "Schneider Slider Memo XB Renkli Kalem Seti",
    "description": "6 adet renkli slider kalem seti.",
    "category": "Kalem Seeri",
    "price": 19.99,
    "desi": 0.15
  },
  {
    "name": "Tombow Mono Zero Silgi",
    "description": "İnce uçlu, hassas silgi.",
    "category": "Silgiler",
    "price": 8.99,
    "desi": 0.05
  },
  {
    "name": "Edding 3000 Permanen Marker Seti",
    "description": "4 adet farklı renkte kalıcı marker seti.",
    "category": "Kalıcı Kalemler",
    "price": 12.99,
    "desi": 0.1
  },
  {
    "name": "Post-it Renkli Sayfalar Bloknot",
    "description": "Renkli sayfalarıyla kullanılabilen bloknot.",
    "category": "Yapışkanlı Noar",
    "price": 9.99,
    "desi": 0.05
  },
  {
    "name": "Stabilo PointMax Renkli Keçeli Kalem Seti",
    "description": "8 adet farklı renkte kalın uçlu Stabilo PointMax kalem seti.",
    "category": "Keçeli Kalemler",
    "price": 29.99,
    "desi": 0.2
  },
  {
    "name": "Schneider Link-It Soft Renkli Tükenmez Kalem Seti",
    "description": "10 adet farklı renkte link-it soft tükenmez kalem seti.",
    "category": "Tükenmez Kalemler",
    "price": 39.99,
    "desi": 0.15
  },
  {
    "name": "Faber-Castell 12 Aquarelle Suluboya Kalem Seti",
    "description": "12 adet farklı renkte suluboya kalemi seti.",
    "category": "Suluboya Kalemleri",
    "price": 34.99,
    "desi": 0.2
  },
  {
    "name": "Schneider Maxx 244 Tükenmez Kalem Seti",
    "description": "4 adet siyah ve mavi renkte max 244 tükenmez kalem seti.",
    "category": "Tükenmez Kalemler",
    "price": 12.99,
    "desi": 0.1
  },
  {
    "name": "Oxford A4 Çizgili Defter",
    "description": "96 sayfalık çizgili defter.",
    "category": "Defterler",
    "price": 14.99,
    "desi": 0.15
  },
  {
    "name": "Zebra Clickart Pastel Kalemler Seti",
    "description": "12 adet farklı renkte pastel renkli kalem seti.",
    "category": "Keçeli Kalemler",
    "price": 24.99,
    "desi": 0.1
  },
  {
    "name": "Uni Posca Boya Kalem Seti",
    "description": "16 adet farklı renkte posca boya kalemlerden oluşan set.",
    "category": "Boya Kalemleri",
    "price": 59.99,
    "desi": 0.2
  },
  {
    "name": "Nuuna Grafik Defter A5",
    "description": "Tasarım defteri, 176 sayfa.",
    "category": "Defterler",
    "price": 49.99,
    "desi": 0.2
  },
  {
    "name": "Pilot G-2 0.5 Jel Kalem Seti",
    "description": "6 adet siyah ve mavi renkte jel kalem seti.",
    "category": "Roller Kalem ve Tükenmez Kalemler",
    "price": 19.99,
    "desi": 0.1
  },
  {
    "name": "Derwent Coloursoft Renkli Kalem Seti",
    "description": "36 adet farklı renkte renkli kalem seti.",
    "category": "Boya Kalemleri",
    "price": 99.99,
    "desi": 0.3
  },
  {
    "name": "Pentel EnerGel Tükenmez Kalem Seti",
    "description": "4 adet farklı renkte enerGel tükenmez kalem seti.",
    "category": "Tükenmez Kalemler",
    "price": 19.99,
    "desi": 0.1
  },
  {
    "name": "Zebra Sarasa Clip Jelly Renkli Jel Kalem Seti",
    "description": "14 adet farklı renkte sarasa clip jel kalem seti.",
    "category": "Jel Kalemler",
    "price": 29.99,
    "desi": 0.15
  },
  {
    "name": "Stabilo Pen 68 Metal Box Renkli Kalemler",
    "description": "20 adet farklı renkte stabilo pen 68 renkli kalem seti.",
    "category": "Boya Kalemleri",
    "price": 44.99,
    "desi": 0.2
  },
  {
    "name": "Staeder Noris Olfa Kesici Seti",
    "description": "Noris olfa kesici ve 10 adet yedek bıçaktan oluşan set.",
    "category": "Makas ve Kesiciler",
    "price": 14.99,
    "desi": 0.15
  },
  {
    "name": "Tesa Tükenmez Bant Rulo",
    "description": "Şeffaf yapışkanlı tükenmez bant rulosu.",
    "category": "Yapışkan ve İşareeyiciler",
    "price": 7.99,
    "desi": 0.1
  },
  {
    "name": "Schneider Line-Up Metal Tükenmez Kalem Seti",
    "description": "5 adet farklı renkte line-up metal tükenmez kalem seti.",
    "category": "Tükenmez Kalemler",
    "price": 24.99,
    "desi": 0.15
  },
  {
    "name": "Fabriano Quadrato Not Defteri",
    "description": "Kare formunda not defteri, 80 sayfa.",
    "category": "Defterler",
    "price": 19.99,
    "desi": 0.1
  },
  {
    "name": "Uni-ball Signo Sparkling Jel Kalem Seti",
    "description": "8 adet parlak renkte jel kalem seti.",
    "category": "Jel Kalemler",
    "price": 19.99,
    "desi": 0.1
  },
  {
    "name": "Tombow Fudenosuke Yumuşak Uçlu Kalem Seti",
    "description": "3 adet farklı yumuşaklıkta fudenosuke kalem seti.",
    "category": "İnce Uçlu Kalemler",
    "price": 14.99,
    "desi": 0.05
  },
  {
    "name": "Lamy Safari Dolmakalem",
    "description": "Rahat ve sağlam tasarımlı dolmakalem.",
    "category": "Dolma Kalemler",
    "price": 149.99,
    "desi": 0.1
  },
  {
    "name": "Schneider Link-It Toplu Kalem Seti",
    "description": "10 adet siyah ve mavi renkte link-it kalem seti.",
    "category": "Kalem Seeri",
    "price": 29.99,
    "desi": 0.15
  },
  {
    "name": "Post-it Renkli Flag Şerier Seti",
    "description": "8 farklı renkte flag şerit içeren set.",
    "category": "Yapışkan ve İşareeyiciler",
    "price": 9.99,
    "desi": 0.05
  },
  {
    "name": "Deli Power Grip Delgeç",
    "description": "Ergonomik tutma yerli, 30 sayfalık delgeç.",
    "category": "Diğer Kırtasiye Ürünleri",
    "price": 22.99,
    "desi": 0.2
  },
  {
    "name": "Staeder Triplus Renkli Kalemler",
    "description": "10 adet farklı renkte ince uçlu renkli kalem seti.",
    "category": "Boya Kalemleri",
    "price": 19.99,
    "desi": 0.1
  },
  {
    "name": "Caran d'Ache Kalem Seti",
    "description": "12 adet farklı renkte Caran d'Ache kalem seti.",
    "category": "Boya Kalemleri",
    "price": 59.99,
    "desi": 0.2
  },
  {
    "name": "Pilot Wahl Eversharp Dolma Kalem",
    "description": "Klasik stile sahip, dolma kalem.",
    "category": "Dolma Kalemler",
    "price": 149.99,
    "desi": 0.1
  },
  {
    "name": "Arine 200 Siyah Uçlu Kalem Seti",
    "description": "5 adet siyah uçlu kalem seti.",
    "category": "Kalem Seeri",
    "price": 19.99,
    "desi": 0.1
  },
  {
    "name": "Zebra Fude Sign Pen Prensip Kalem Seti",
    "description": "3 adet farklı kalınlıkta prensip kalem seti.",
    "category": "Yazı Araçları",
    "price": 14.99,
    "desi": 0.05
  },
  {
    "name": "Stabilo Pen 68 Renkli Keçeli Kalem Seti",
    "description": "20 adet farklı renkte pen 68 kalem seti.",
    "category": "Boya Kalemleri",
    "price": 44.99,
    "desi": 0.2
  },
  {
    "name": "Staeder Noris Club 12 Renkli Kalem Seti",
    "description": "12 adet farklı renkte noris club kalem seti.",
    "category": "Boya Kalemleri",
    "price": 19.99,
    "desi": 0.15
  },
  {
    "name": "Maped Color'Peps Su Bazlı Boya Kalem Seti",
    "description": "24 adet farklı renkte su bazlı boya kalem seti.",
    "category": "Boya Kalemleri",
    "price": 39.99,
    "desi": 0.3
  },
  {
    "name": "Schneider Maxx 265 Tükenmez Kalem Seti",
    "description": "4 adet siyah ve mavi renkte max 265 kalem seti.",
    "category": "Tükenmez Kalemler",
    "price": 19.99,
    "desi": 0.1
  },
  {
    "name": "Uni-ball Signo Beyaz Jel Kalem",
    "description": "Koyu ve düzgün yazma sağlayan beyaz jel kalem.",
    "category": "Kalem Seeri",
    "price": 6.99,
    "desi": 0.05
  },
  {
    "name": "Pilot G2 Tükenmez Kalem Seti",
    "description": "6 adet renkli g2 tükenmez kalem seti.",
    "category": "Tükenmez Kalemler",
    "price": 19.99,
    "desi": 0.15
  },
  {
    "name": "Tombow Mono Drawing Silgi",
    "description": "Güçlü silme işlemine sahip silgi.",
    "category": "Silgiler",
    "price": 5.99,
    "desi": 0.05
  },
  {
    "name": "Pentel R.S.V.P. Tükenmez Kalem Seti",
    "description": "8 adet farklı renkte tükenmez kalem seti.",
    "category": "Tükenmez Kalemler",
    "price": 24.99,
    "desi": 0.15
  },
  {
    "name": "Uni Pin Fine Line Siyah Fineliner Kalem Seti",
    "description": "3 adet farklı uç kalınlığına sahip siyah fineliner kalem seti.",
    "category": "Siyah Kalemler",
    "price": 14.99,
    "desi": 0.05
  },
  {
    "name": "Rotring Tikky Mekanik Kurşun Kalem Seti",
    "description": "3 adet farklı renkte tıkky mekanik kurşun kalem seti.",
    "category": "Mekanik Kalemler",
    "price": 14.99,
    "desi": 0.1
  },
  {
    "name": "Fabriano en İyi Arkadaşlar Not Defteri",
    "description": "Sevimli desenli, arkadaşına hediye edilebilecek not defteri.",
    "category": "Defterler",
    "price": 12.99,
    "desi": 0.1
  },
  {
    "name": "Faber-Castell Connector Grip Boya Kalem Seti",
    "description": "12 adet farklı renkte connector grip kalem seti.",
    "category": "Boya Kalemleri",
    "price": 29.99,
    "desi": 0.2
  }
]

for urun in urunler:
    # Kategori nesnesini bul veya oluştur
    kategori, olusturuldu = Category.objects.get_or_create(name=urun["category"])
    
    # Ürünü oluştur ve veritabanına ekle
    Product.objects.create(
        name=urun["name"],
        description=urun["description"],
        category=kategori,
        price=urun["price"],
        desi=urun["desi"]
    )

print("Ürünler eklendi.")
