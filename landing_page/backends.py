from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(UserModel.objects.all())
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            print(user.password)
            print(password  )
            print(user.check_password(password))
            # if user.check_password(password):
            if password == user.password:
                print("password")
                return user
        return None