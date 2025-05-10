from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers from UserSerializer


#get all users
@api_view('GET')
def getUsers(request)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# get single user
@api_view('GET')
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

# create user
@api_view('POST')
def addUser(resquest):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view('DELETE')
def deleteUser(request, pk):
    user = user.objects.get(id=pk)
    user.delete()
    return Response('User successfully deleted')

