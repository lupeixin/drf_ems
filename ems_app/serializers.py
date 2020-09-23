from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
from rest_framework_jwt.settings import api_settings

from ems_app.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "real_name", "password", "gender", "status")

        extra_kwargs = {
            "username": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            }
        }

    def validate_username(self, attrs):
        user = User.objects.filter(username=attrs).first()

        if user:
            raise exceptions.ValidationError("用户名已存在")

        return attrs


class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        extra_kwargs = {
            "emp_name": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            }
        }


# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#
#
# class TokenSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "password", ]
#         extra_kwargs = {
#             "username": {
#                 "read_only": True,
#             },
#             "password": {
#                 "read_only": True,
#             }
#         }
#
#     # 完成token的生成
#     def validate(self, attrs):
#         print(attrs)
#         print(self.context.get('name'))
#         account = self.context.get('name')
#         pwd = attrs.get("password")
#         user_obj = User.objects.filter(username=account).first()
#
#         if user_obj and user_obj.check_password(pwd):
#             # 签发token
#             payload = jwt_payload_handler(user_obj)  # 生成载荷
#             token = jwt_encode_handler(payload)  # 生成token
#             self.token = token
#             self.obj=user_obj
#             return attrs
#
#         raise exceptions.ValidationError('用户名密码错误。不签发Token')

