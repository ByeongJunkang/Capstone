
import jwt, json, requests

from functools              import wraps
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .settings import SECRET_KEY
from common.models import User



def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access = request.COOKIES['access']
            payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
            request.user = User.objects.get(id=payload['user_id'])

            return func(self, request, *args, **kwargs)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=400)
            
        except jwt.DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'}, status=400)

        except jwt.ExpiredSignatureError:
            return JsonResponse({"message": "EXPIRED_TOKEN"}, status = 400)

    return wrapper