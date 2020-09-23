from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin

from ems_app.models import User, Employee
from ems_app.serializers import UserModelSerializer, EmployeeModelSerializer
from utils.response import APIResponse


class UserAPIView(APIView):

    def post(self, request, *args, **kwargs):
        """
        处理用户注册逻辑
        :param request: 前端传递的用户的数据
        :return:  注册成功与否
        """

        request_data = request.data
        serializer = UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        data = UserModelSerializer(user_obj).data

        return APIResponse(200, True, results=data)

    def get(self, request, *args, **kwargs):
        """
        用户的登录请求
        :param request:
        :return:
        """
        username = request.query_params.get("username")
        password = request.query_params.get("password")

        user_obj = User.objects.filter(username=username, password=password).first()
        if user_obj:
            data = UserModelSerializer(user_obj).data
            return APIResponse(200, True, results=data)

        return APIResponse(400, False)


class EmployeeGenericAPIView(ListModelMixin, CreateModelMixin, GenericAPIView, DestroyModelMixin, UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)

        return APIResponse(200, True, results=response.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        emp = self.create(request, *args, **kwargs)

        return APIResponse(200, True, results=emp.data)

    def delete(self, request, *args, **kwargs):
        print(request.data)
        del_emp = self.destroy(request, *args, **kwargs)
        return APIResponse(200, True, results=del_emp.data)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        updata_emp = self.partial_update(request, *args, **kwargs)
        return APIResponse(200, True, results=updata_emp.data)


class TokenAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = TokenSerializer(data=request.data, context={"name": request.data['username']})
        serializer.is_valid(raise_exception=True)
        data = TokenSerializer(serializer.obj).data

        return APIResponse(data_message="OK", token=serializer.token, results=data)
