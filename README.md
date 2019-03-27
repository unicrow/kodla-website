# Kodla

Production : https://www.kodla.co <br>
Staging    : https://www.kodla.unicrow.com


### Kodla nedir?
Popüler yazılım dilleri ve popüler donanımlar hakkında teknik seminerlerin düzenlendiği bilişim etkinliğidir.


### Kimlere hitap ediyor?
* Hacker ve maker meraklılarına
* Açık kaynaklı yazılım ve donanıma ilgi duyan insanlara
* Karadeniz Bölgesi’nde bulunan üniversiteler başta olmak üzere ülke genelindeki bütün üniversite öğrencilerine
* Bilişim sektörü çalışanları ve meraklılarına


### Proje Özellikleri
* Etkinliğin tüm içeriği admin panelinden girilerek yeni yıl için etkinlik oluşturulabiliyor.
* Etkinliğe özel logo ayarlanabiliyor.
* Etkinliğe özel harita özelliği mevcut.
* Admin panelinde içeriklerin daha kapsamlı yazılabilmesi için editör mevcut.
* Etkinliğe özel sınırsız sayıda akış oluşturulabiliyor.
* Sosyal hesaplarda sıralama özelliği mevcut. (Konuşmacı, Etkinlik)
* Konuşmacılar arasında sıralama özelliği mevcut. (Etkinliğe özel sıralama şuan için yok.)
* Sponsorlar etkinliğe özel sıralabiliyor.
* Sponsor logoları etkinliğe özel boyutlandırılabiliyor.
* Twitter'da etkinlik ile ilgili atılan tweetler gösteriliyor.
* Program içeriğine sunum linki ve sunum dosyası eklendi.
* Konuşmacı olmak istiyorum özelliği.
* Etkinliğe kayıt olma özelliği eklendi.
* İletişim formu doldurulduğunda sistem yöneticilerine email gönderiliyor.
* Kayıt formu duldurulduğunda sistem yöneticilerine email gönderiliyor.


### Projenin yerelde çalışır hale getirilmesi
* Setup
```
  cp kodla/settings/local-dist.py kodla/settings/local.py
  touch kodla/settings/secrets.py # secret.py içeriği aşağıda mevcut.
```

* Build
```
  docker-compose -p kodla -f docker/docker-compose.yml -f docker/docker-compose.dev.yml build
```

* Start
```
  docker-compose -p kodla -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up -d
```

* Logs
```
  docker-compose -p kodla -f docker/docker-compose.yml -f docker/docker-compose.dev.yml logs -f --tail 50
```

* Status
```
  docker-compose -p kodla -f docker/docker-compose.yml -f docker/docker-compose.dev.yml ps
```

* Restart
```
  docker-compose -p kodla -f docker/docker-compose.yml -f docker/docker-compose.dev.yml restart
```

* Stop
```
  docker-compose -p kodla -f docker/docker-compose.yml -f docker/docker-compose.dev.yml stop
```

* Container
```
  docker exec -it kodla_backend_1 /bin/bash
  > python manage.py migrate
```


**Not**:
* settings dizini altında **secrets.py** adında bir dosya oluşturmanız gerekmektedir.
```python
  # Django
  SECRET_KEY = 'blabla'


  # Email
  EMAIL_HOST_USER = 'blabla'
  DEFAULT_FROM_EMAIL = 'blabla'
  EMAIL_HOST_PASSWORD = 'blabla'


  # Google Map (https://github.com/philippbosch/django-geoposition)
  GOOGLE_MAPS_API_KEY = 'blabla'


  # ReCaptcha (https://github.com/praekelt/django-recaptcha)
  RECAPTCHA_PUBLIC_KEY = 'blabla'
  RECAPTCHA_PRIVATE_KEY = 'blabla'


  # Twitter (https://github.com/bear/python-twitter)
  TWITTER_CONSUMER_KEY = 'blabla'
  TWITTER_CONSUMER_SECRET = 'blabla'
  TWITTER_ACCESS_TOKEN = 'blabla'
  TWITTER_ACCESS_TOKEN_SECRET = 'blabla'


  # Disqus
  DISQUS_API_KEY = 'blabla'
  DISQUS_WEBSITE_SHORTNAME = 'blabla'
```
