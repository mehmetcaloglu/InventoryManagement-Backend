from uygulama_adi.models import Depot

# Depo bilgileri
depolar = [
    {
        "name": "Ankara Depo",
        "type": "AnaDepo",
        "location": "Ankara"
    },
    {
        "name": "İstanbul Ara Depo",
        "type": "AraDepo",
        "location": "İstanbul"
    },
    {
        "name": "İzmir Ara Depo",
        "type": "AraDepo",
        "location": "İzmir"
    },
    {
        "name": "Antalya Ara Depo",
        "type": "AraDepo",
        "location": "Antalya"
    },
    {
        "name": "Bursa Ara Depo",
        "type": "AraDepo",
        "location": "Bursa"
    },
    {
        "name": "Adana Ara Depo",
        "type": "AraDepo",
        "location": "Adana"
    },
    {
        "name": "Trabzon Ara Depo",
        "type": "AraDepo",
        "location": "Trabzon"
    },
    {
        "name": "Gaziantep Ara Depo",
        "type": "AraDepo",
        "location": "Gaziantep"
    },
    {
        "name": "Konya Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Konya"
    },
    {
        "name": "Kayseri Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Kayseri"
    },
    {
        "name": "Samsun Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Samsun"
    },
    {
        "name": "Eskişehir Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Eskişehir"
    },
    {
        "name": "Mersin Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Mersin"
    },
    {
        "name": "Tekirdağ Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Tekirdağ"
    },
    {
        "name": "Denizli Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Denizli"
    },
    {
        "name": "Balıkesir Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Balıkesir"
    },
    {
        "name": "Aydın Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Aydın"
    },
    {
        "name": "Manisa Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Manisa"
    },
    {
        "name": "Sakarya Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Sakarya"
    },
    {
        "name": "Kütahya Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Kütahya"
    },
    {
        "name": "Muğla Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Muğla"
    },
    {
        "name": "Hatay Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Hatay"
    },
    {
        "name": "Afyonkarahisar Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Afyonkarahisar"
    },
    {
        "name": "Kocaeli Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Kocaeli"
    },
    {
        "name": "Malatya Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Malatya"
    },
    {
        "name": "Şanlıurfa Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Şanlıurfa"
    },
    {
        "name": "Van Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Van"
    },
    {
        "name": "Erzurum Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Erzurum"
    },
    {
        "name": "Diyarbakır Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Diyarbakır"
    },
    {
        "name": "Sivas Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Sivas"
    },
    {
        "name": "Edirne Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Edirne"
    },
    {
        "name": "Çorum Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Çorum"
    },
    {
        "name": "Ordu Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Ordu"
    },
    {
        "name": "Bolu Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Bolu"
    },
    {
        "name": "Trabzon Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Trabzon"
    },
    {
        "name": "Bartın Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Bartın"
    },
    {
        "name": "Isparta Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Isparta"
    },
    {
        "name": "Yalova Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Yalova"
    },
    {
        "name": "Kırklareli Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Kırklareli"
    },
    {
        "name": "Kırıkkale Mağaza Depo",
        "type": "MağazaDepo",
        "location": "Kırıkkale"
    }
]


for depo_info in depolar:
    # Depoyu oluştur ve veritabanına ekle
    Depot.objects.create(
        name=depo_info["name"],
        type=depo_info["type"],
        location=depo_info["location"]
    )

print("Depolar eklendi.")
