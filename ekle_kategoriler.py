from uygulama_adi.models import Category

kategoriler = [
    "100 sayfalık defter",
    "Yapışkan ve İşaretleyiciler",
    "spiral bağlantılı ajanda",
    "Roller Kalem ve Tükenmez Kalemler",
    "Kurşun Kalemler",
    "Tükenmez Kalemler",
    "kullanıcı dostu hesap makinesi",
    "Yapıştırıcılar ve Bantlar",
    "Kalem Setleri",
    "80 sayfalık A5 boyutunda ince defter",
    "Anahtarlıklar",
    "S ve B uçlu artist kalemden oluşan set",
    "siyah mürekkepli tükenmez kalem",
    "A4 boyutunda belge dosyası",
    "Keçeli ve Highlighter Kalemler",
    "120 sayfalık spiral defter",
    "cepli ajanda",
    "hassas silgi",
    "Kalıcı Kalemler",
    "Yapışkanlı Notlar",
    "Siyah Kalemler",
    "Suluboya Kalemleri",
    "Defterler",
    "176 sayfa",
    "Jel Kalemler",
    "İnce Uçlu Kalemler",
    "30 sayfalık delgeç",
    "dolma kalem",
    "Yazı Araçları",
    "Mekanik Kalemler",
    "arkadaşına hediye edilebilecek not defteri",
]

for kategori_adi in kategoriler:
    Category.objects.create(name=kategori_adi)
