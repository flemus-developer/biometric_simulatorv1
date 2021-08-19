from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from registration.models import Register
from registration.api.serializers import RegisterSerializer, RegisterListSerializer

#Métodos donde se podrá utilizar la función
@api_view(['GET','POST'])
#Se define la función como un request
def register_api_view(request):

    # list
    if request.method == 'GET':
        # queryset con los valores o atributos que se desean mostrar
        registers = Register.objects.all().values('id','date','time','fingerprint')
        registers_serializer = RegisterListSerializer(registers,many = True)
        return Response(registers_serializer.data,status = status.HTTP_200_OK)

    #Si es un método POST se procesará como un Create
    elif request.method == 'POST':
        #Convertir un json a un modelo
        registers_serializer = RegisterSerializer(data = request.data)

        #Validar que sea un objeto valido
        if registers_serializer.is_valid():
            registers_serializer.save()
            return Response({'message':'Registro creado exitosamente!'},status = status.HTTP_201_CREATED)

        return Response(registers_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def register_detail_api_view(request,pk=None):
    # queryset para buscar el registro que concuerde con el id que se está mandado
    register = Register.objects.filter(id = pk).first()

    #Se valida que la variable register no este vacía
    if register:

        #Retornar los datos del objeto pero serializado en formato json
        if request.method == 'GET':
            register_serializer = RegisterSerializer(register)
            return Response(register_serializer.data,status = status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            register_serializer = RegisterSerializer(register,data = request.data)
            if register_serializer.is_valid():
                register_serializer.save()
                return Response(register_serializer.data,status = status.HTTP_200_OK)
            return Response(register_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            register.delete()
            return Response({'message':'Registro eliminado exitosamente!'},status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado un registro con estos datos'},status = status.HTTP_400_BAD_REQUEST)