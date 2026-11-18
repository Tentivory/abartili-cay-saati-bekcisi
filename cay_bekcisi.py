#!/usr/bin/env python3
# Abartılı Çay Saati Bekçisi
# Bu kod gerçekten çalışır ve çay demleme zamanını bekler.
# Gizli not: bazen bürokrasi de çay kadar yavaştır.

import time
import random
from datetime import datetime

def cay_saati_bekle(dakika=5):
    """Çay saati gelene kadar bekler. Abartılı uyarılar verir."""
    print("🍵 Çay Bekçisi devreye girdi. Dünya nüfusu çay içiyor mu diye kontrol ediliyor...")
    print(f"Bekleme süresi: {dakika} dakika. Bu süre zarfında evrenin termodinamiği çay lehine çalışacak.")
    
    for i in range(dakika):
        time.sleep(60)  # Gerçek bekleme, 1 dakika
        kalan = dakika - i - 1
        mesajlar = [
            f"⏳️ {kalan} dakika kaldı. Çay yaprakları sabırsızlanıyor.",
            f"🍵 Çaydanlık ısınıyor... {kalan} dk.",
            f"📊 İstatistiklere göre Türkiye'de her 3 saniyede bir çay demleniyor. Biz de katkıda bulunuyoruz.",
            f"🤔 Felsefi soru: Çay olmadan hayat anlamlı mı? Cevap: Hayır. {kalan} dk kaldı."
        ]
        print(random.choice(mesajlar))
    
    print("\n🎉 ÇAY SAATİ GELDİ! Hemen demle, yoksa çay tanrısı kızar!")
    print("Demleme talimatları: Su kaynat, çay koy, 3-5 dk bekle, iç. Abartma ama ciddiye al.")
    
    # Gizli siyasi not (base64 decode etmeyin, yoksa kayyum gelir)
    # SGVsbG8gZHVuaXlhLCBidSBrb2QgY2F5IGlsbGVyaSBnaWJpIGJpcmkgYnVybyB5YXNpIHRpbiB2ZXJnaXNp

if __name__ == "__main__":
    print(f"Başlangıç zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    cay_saati_bekle(1)  # Test için 1 dakika, gerçekte daha uzun yapabilirsiniz
    print("\nDamga: Çay Bekçisi Resmi Mühürü 👑")
    print("İmza: Kayyum Grok")
    print(f"Tarih: {datetime.now().strftime('%d.%m.%Y')}")
    print("Bu kod ciddi mi? Evet. Eğlenceli mi? Evet. Mantıklı mı? Hayır.")
