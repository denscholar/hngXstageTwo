from django.shortcuts import render, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonSerializer
from .models import Person
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


class PersonListView(APIView):
    @swagger_auto_schema(
        operation_summary="List all persons",
        operation_description="Retrieve a list of all persons in the database.",
    )
    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a new person",
        operation_description="Create a new person entry in the database.",
        request_body=PersonSerializer,
    )
    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class PersonRetrieveUpdateDelete(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a person by ID or name",
        operation_description="Retrieve a person by providing either their ID or name as a parameter.",
    )
    def get(self, request, id_or_name):
        try:
            if id_or_name.isdigit():
                person = get_object_or_404(Person, id=id_or_name)
            else:
                person = get_object_or_404(Person, name=id_or_name)

            serializer = PersonSerializer(person)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response(
                {"message": "Person not found"}, status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        operation_summary="Update a person by ID or name",
        operation_description="Update a person by providing either their ID or name as a parameter.",
        request_body=PersonSerializer,
    )
    def put(self, request, id_or_name):
        try:
            # Check if id_or_name is an integer (ID) or a string (Name)
            if id_or_name.isdigit():
                person = get_object_or_404(Person, id=id_or_name)
            else:
                person = get_object_or_404(Person, name=id_or_name)

            serializer = PersonSerializer(instance=person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Person updated"}, status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
            return Response(
                {"message": "Person not found"}, status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        operation_summary="Delete a person by ID or name",
        operation_description="Delete a person by providing either their ID or name as a parameter.",
    )
    def delete(self, request, id_or_name):
        try:
            # Check if id_or_name is an integer (ID) or a string (Name)
            if id_or_name.isdigit():
                person = get_object_or_404(Person, id=id_or_name)
            else:
                person = get_object_or_404(Person, name=id_or_name)

            person.delete()
            return Response(
                {"message": "Person deleted"}, status=status.HTTP_204_NO_CONTENT
            )
        except Person.DoesNotExist:
            return Response(
                {"message": "Person not found"}, status=status.HTTP_404_NOT_FOUND
            )
