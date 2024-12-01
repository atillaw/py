

print('___________________________________________________________________')
print("")

def bold_text(text):
    return "\033[1m" + text + "\033[0m"  

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"  

def menu():
    print(color_text("🐍" + "═" * 66, "92"))  
    print(color_text(" 1. Python nedir?", "93")) 
    print(color_text(" 2. Python'un sahibi kimdir?", "93"))
    print(color_text(" 3. Python modülleri ve ne işe yaradıkları", "93"))
    print(color_text(" 4. Tool nedir?", "93"))
    print(color_text(" 5. Tool nasıl yapılır?", "93"))
    print(color_text(" 6. Checker nasıl yapılır?", "93"))
    print(color_text(" 7. Checker nedir?", "93"))
    print(color_text(" 0. Çıkış", "91")) 
    print(color_text("🐍" + "═" * 66, "92"))
    print("")

def cevaplar(secim):
    print(color_text("🔷" + "═" * 55, "94"))  
    if secim == 1:
        print(bold_text(color_text("Python nedir?", "95")))  
        print(color_text("Python, yüksek seviyeli, genel amaçlı bir programlama dilidir. 1991 yılında Guido van Rossum tarafından geliştirilmiştir. Basit ve okunabilir söz dizimi, Python'u hem başlangıç seviyesindeki programcılar hem de uzmanlar arasında popüler hale getirmiştir.", "97"))  
    elif secim == 2:
        print(bold_text(color_text("Python'un sahibi kimdir?", "95")))
        print(color_text("Python dilinin yaratıcısı Guido van Rossum'dur. Python, Python Software Foundation (PSF) tarafından desteklenmektedir ve açık kaynak bir projedir, yani dünyanın her yerinden geliştiriciler tarafından geliştirilmeye devam ediyor.", "97"))
    elif secim == 3:
        print(bold_text(color_text("Python modülleri ve ne işe yaradıkları", "95")))
        print(color_text("Python modülleri, önceden yazılmış kod parçalarıdır. Geliştiricilerin işini kolaylaştırır ve projelerinde tekrar eden işleri kolayca yapmalarını sağlar. Örneğin, 'requests' modülü ile HTTP istekleri yapılabilir, 'numpy' modülü ise matematiksel işlemleri hızlandırır.", "97"))
    elif secim == 4:
        print(bold_text(color_text("Tool nedir?", "95")))
        print(color_text("Tool (araç), belirli bir görevi yerine getirmek için yazılmış bir programdır. Bu, birden fazla işlevi otomatikleştirmek veya bir görevi daha verimli hale getirmek için kullanılabilir. Örneğin, bir dosya indirme aracı veya veri analiz aracı bir 'tool'dur.", "97"))
    elif secim == 5:
        print(bold_text(color_text("Tool nasıl yapılır?", "95")))
        print(color_text("Tool oluştururken ilk adım, API kullanarak veri çekmektir. Tool, API'den alınan veriyi işler ve bir görevi yerine getirir. API isteğini nasıl yapacağınızı ve çekilen veriyi nasıl işleyip kullanacağınızı bilmeniz önemlidir. Sonrasında bu verileri mantıklı bir şekilde işleyip tool'u tamamlayabilirsiniz.", "97"))
        print(color_text("Adımlar:", "97"))
        print(color_text("1. İlk olarak, çekmek istediğiniz API'yi belirleyin. Örneğin, bir web sitesinden başlıklar çekmek için API'yi kullanabilirsiniz.", "97"))

    elif secim == 6:
        print(bold_text(color_text("Checker nasıl yapılır?", "95")))
        print(color_text("Bir checker, belirli bir kaynağa istek gönderip sonucu doğrulayan bir araçtır. Örneğin, bir hesap checker yapmak için API'ye HTTP isteği gönderilir ve dönen cevap analiz edilerek hesap geçerli mi değil mi kontrol edilir.", "97"))
        print(color_text("Adımlar:", "97"))
        print(color_text("1. Checker yazarken önce hedef sitenin API'sini öğrenin. Hangi isteklerin gönderileceğini ve hangi cevapların dönmesini beklediğinizi anlamalısınız.", "97"))
 
    elif secim == 7:
        print(bold_text(color_text("Checker nasıl yapılır?", "95")))
        print(color_text("Checker, bir API veya kaynağa istek yaparak verilerin doğruluğunu kontrol eder. Checker yazarken, belirli bir siteye ya da API'ye istek gönderir, dönen verileri kontrol ederek doğruluğunu test edersiniz. Başarılı ya da başarısız sonucu döndürmek için sonuçları analiz etmeniz gerekir.", "97"))
        print(color_text("Bir checker yaparken adımlar şunlardır:", "97"))
        print(color_text("1. API'ye doğrulama isteği gönder.", "96"))
        print(color_text("2. API'den gelen sonuçları kontrol et.", "96"))
        print(color_text("3. Doğruysa başarıyı, yanlışsa hatayı döndür.", "96"))
    elif secim == 0:
        print(bold_text(color_text("Programdan çıkılıyor...", "91")))  
    else:
        print(bold_text(color_text("Geçersiz bir seçim yaptınız!", "91")))
    print(color_text("🔷" + "═" * 55, "94"))
    print("")


while True:
    menu()
   
    try:
        secim = int(input(bold_text(color_text("Bir seçim yapın: ", "92"))))
        print("")
        if secim == 0:
            cevaplar(secim)
            break
        else:
            cevaplar(secim)
    except ValueError:
        print(bold_text(color_text("Lütfen geçerli bir sayı girin!", "91")))