from django.db import models

# Create your models here.
from django.contrib.auth.models import User
"""
기존에 모델을 확장(필드를 추가)하려면 모델 소스코드를 변경하는데,
애시당초 모델을 만들 때는 models.Model을 상속받는다.
* 모델은 어떤 모델을 상속받아서 확장할 수도 있다.

기존 User 모델은 AbstractUser라는 모델을 상속받아서 구현된다.
AbstractUser모델은 AbastractBaseUser라는 모델을 상속받아서 구현된다.
* Abstract : 추상이라고 해석되는 단어인데, 모델의 설정값에 Abstract라는 값을 설정할 수 있다.
Abstract가 설정되어 있으면, 실제 모델로 사용 불가

1) 기존 User 모델은 AbastractUser라는 모델을 상속받아서 필수 필드들이 이미 구현이 되어 있는 상태이다.
- 우리가 익히 보던 기본 필드들과, 권한 관련 기능 등 장고에서 유저에게 기능적으로 필요한 기능이 구현되어있다.
- 추가 필드가 필요한 경우에는 AbstractUser 모델을 상속받아 구현하는 것이 제일 편하다.

2) AbstractBaseUser로 구현해야 되는 경우
- 모든 필드 구조를 변경할 필요가 있을 때
- 퍼미션 기능 등 장고에서 사용하는 유저 기본 기능 전체를 뜯어 고치고 싶을 때
- Backend를 새로 구현해줘야 한다.

3) 기존 User 모델을 상속받거나, 확장해서 사용하는 경우
- User + AdditionalInfo(생일, 주소, 주민번호)
- 회원 수정 페이지 AdditionalInfoForm 추가로 출력


1번을 제일 권장하는 확장 방식 - 프로젝트 시작 시점에 고려, (* 기존 데이터 유지 불가)
3번은 사이트를 운영 중에 확장을 고려해야 할 때 선택 가능, 기존 User 데이터 그대로 존재 + 추가 테이블 
* OneToOne필드(이 유저가 한 필드랑만 일치한다)

swappable은 AUTH_USER_MODEL 값에 설정된 모델과 교체 가능하다고 미리 설정해 둔것
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
"""


from django.contrib.auth.models import AbstractUser

class User(AbstractUser): # 클래스 이름 다른 것 해도 상관없다.
    message = models.TextField(blank=True)
    profile = models.ImageField(upload_to='user_images/profile/%Y/%m/%d', blank=True)
