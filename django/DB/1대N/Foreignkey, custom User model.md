## DB

#### Foreign key

> RDBMS에서 한 테이블으 필드 중 다른 테이블의 행(row)을 식별할 수 있는 키

* 참조하는 테이블의 1개의 키에 해당하고 이는 참조되는 측의 테이블의 기본 키를 가리킴
* 하나의 테이블이 여러 개의 외래 키를 포함할 수 있음

* 참조하는 테이블의 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
* 참조하는 테이블과 참조되는 테이블이 동일할 수 있음(재귀적 외래 키) - 댓댓글

**특징**

- 키를 사용하여 부모 테이블의 유일할 값을 참조 (참조 무결성)
- 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일해야 함



'' `참조 무결성` '' : 무결성의 법칙 중 하나, 외래 키의 개념. 외래 키 값이 데이터베이스의 특정 테이블의 기본 키 값을 참조하는 것(pk), 이따금 외래키가 기본키가 아닐 수도 있다.



#### Django : ForeignKey()

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

##### ForignKey's Arguments - on_delete

* CASCADE : 부모 객체가 삭제 되었을 때 이를 참조하는 객체도 삭제
* PROTECT
* SET_NULL
* SET_DEFAULT
* SET()
* DO_NOTHING
* RESTRICT



##### ForignKey's Arguments - related_name

> django가 기본적으로 만들어주는 _set manager을 변경할 이름 설정
>
> M:N 관계에서 반드시 사용해야 하는 상황이 발생!



##### 1:N model manager

* Comment(N)이 Article(1)을 참조

  > comment.article

* Article(1)이 Comment(N)을 참조( 역참조 )

  > article.comment_set.all()





#### Substituting a custom User model (커스텀 유저 모델로 대체하기)

* django는 custom model을 참조하는 AUTH_USER_MODEL 설정을 제공하여 기본 user model을 재정의 (override) 할 수 있도록 함
* 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, 커스텀 유저 모델을 설정하는 것을 강력하게 권장
* 커스텀 유저 모델은 기본 사용자 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
* **단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야함**

**[참고] ** https://docs.djangoproject.com/en/3.1/topics/auth/customizing/



### AUTH_USER_MODEL

* User를 나타내는데 사용하는 모델
* 기본 값은 'auth.User'
* 프로젝트가 진행되는 동안 변경할 수 없음
* 프로젝트 시작 시 설정 바람.

#### AbstractBaseUser

* 기본적으로 password, last_login만 제공
* 자유도 높지만 다른 필드 모두 직접 작성

#### AbstractUser

* 관리자 권한과 함께 완전한 기능을 갖춘 사용자 모델을 구현하는 기본 클래스



##### accounts/models.py

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

##### crud/setting.py

```python
AUTH_USER_MODEL = 'accounts.User'
```



UserCreationForm

UserChangeForm

이 form들은 유저 재정의를 해야한다.

##### accounts/forms.py

```python
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustromUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```



#### Referencing the User model (유저 모델 참조하기)

##### settings.AUTH_USER_MODEL

* 유저 모델에 대한 외래키 또는 M:N관계를 정의할 때 사용
* models.py에서 유저 모델을 참조할 떄 사용

##### articles/models.py

```python
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ...
```

##### get_user_model()

* django는 User 모델을 직접 참조하는 대신 get_user_model()을 사용하여 사용자 모델 참조하라고 권장
* 현재 활성화된 유저모델 (지정된 커스텀 유저 모델, 그렇지 않은 경우 User) 을 반환
* models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용


