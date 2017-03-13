# Kodla

http://www.kodla.co


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


### Gelecekte Eklenecek Özellikler
* Konuşmacı olmak istiyorum özelliği.
* Hackathon başvuru özelliği.
* Hackathon için api.


### Projenin yerelde çalışır hale getirilmesi
```
  $ virtualenv -p python3 Kodla/env
  $ cd Kodla
  $ source env/bin/activate
  $ git clone https://github.com/unicrow/kodla.git source
  $ cd source
  $ pip install -r requirements/base.txt
  $ pip install -r requirements/debug.txt (opsiyonel)
  $ pip install -r requirements/prod.txt  (Eğer postgresql kullanıyorsanız.)  
  $ python manage.py migrate
  $ python manage.py compilemessages
```

**Not**: 
* settings dizini altında **secret.py** adında bir dosya oluşturmanız gerekmektedir.
```python
  # Django
  SECRET_KEY = 'blabla'


  # Google Map (https://github.com/philippbosch/django-geoposition)
  GOOGLE_MAP_API_KEY = 'blabla'


  # ReCaptcha (https://github.com/praekelt/django-recaptcha)
  RECAPTCHA_PUBLIC_KEY = 'blabla'
  RECAPTCHA_PRIVATE_KEY = 'blabla'


  # Twitter (https://github.com/bear/python-twitter)
  TWITTER_CONSUMER_KEY = 'blabla'
  TWITTER_CONSUMER_SECRET = 'blabla'
  TWITTER_ACCESS_TOKEN = 'blabla'
  TWITTER_ACCESS_TOKEN_SECRET = 'blabla'
```
* istediğiniz settings ayarının çalışması için settings dizini altında **__ init __.py** dosyasını değiştirebilirsiniz.
```python
  # Standard Library
  import getpass

  # Local Django
  from source.settings.base import *


  if getpass.getuser() in ['root']:
      from source.settings.prod import *
  elif getpass.getuser() in ['vagrant', 'ubuntu', 'kodla', 'kenan']:
      from source.settings.staging import *
  else:
      from source.settings.dev import *
```
