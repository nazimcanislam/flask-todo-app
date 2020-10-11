# Flask Todo Uygulaması

---

Python'ın **Flask** kütüphanesi sayesinde çok kolay bir şekilde web uygulamaları geliştirmek mümkün. Ve bu projede basit bir **todo** uygulaması yaptım.

![Genel ekran](static/images/image1.png)
![Detay ekranı](static/images/image2.png)

### Todo Uygulamanın Özellikleri
* Yeni todo ekleme
* Todo silme
* Düzenleme
* Değiştirme
* Oluşturma tarihi ve bitirme tarihi
* Bootstrap4 ile zenginleştirilmiş arayüz

### Kullanım
`Windows kullanıcıları için...`
```bash
python app.py
```

`Linux veya MacOS kullanıcı python3 ile kullanmalı.`
```bash
python3 app.py
```

Daha sonra istediğiniz web tarayıcısını açın ve URL kısmına bunu yazın:
```bash
localhost:5000
```

Uygulama çalıştığı sürece yerelinizde (localhost) 5000 portunu kullanacaktır. Eğer bu portu değiştirmek isterseniz (ya da değiştirmeniz gerekiyorsa) `app.py` dosyasının en altında ki port numarasınız değiştiriniz.

`app.py`
```python
if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

### Kullanılan Teknolojiler
* Python3
* Flask
* SQLAlchemy
* HTML5
* Bootstrap4 (CND)
* JavaScript (Vanilla)
* JQuery3
* Ve tabii ki de 10 hızlı parmak 😃

### Gerekli Python Sürümü ve Kütüphaneleri
* python==3.8.2
* flask==1.1.2
* flask-SQLAlchemy==2.4.3
