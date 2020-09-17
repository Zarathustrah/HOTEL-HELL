# pylint: disable=no-member, no-self-use
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Place
from .serializers import PlaceSerializer

class PlaceListView(APIView):

  permission_classes = (IsAuthenticatedOrReadOnly, )

  def get(self, _request):
      places = Place.objects.all()
      serialized_places = PlaceSerializer(places, many=True)
      return Response(serialized_places.data, status=status.HTTP_200_OK)

  def post(self, request):
      new_place = PlaceSerializer(data=request.data)
      if new_place.is_valid():
          new_place.save()
          return Response(new_place.data, status=status.HTTP_201_CREATED)
      return Response(new_place.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class PlaceDetailView(APIView):

  # def get(self, _request, pk):
  #       place = Place.objects.get(pk=pk)
  #       serialized_place = PlaceSerializer(place)
  #       return Response(serialized_place.data, status=status.HTTP_200_OK)


    permission_classes = (IsAuthenticatedOrReadOnly, )


    def get_place(self, pk):
        try:
            return Place.objects.get(pk=pk)
        except Place.DoesNotExist:
            raise NotFound()

    def is_place_owner(self, place, user):
        if place.owner.id != user.id:
            raise PermissionDenied()

    def get(self, _request, pk):
        place = self.get_place(pk)
        serialized_place = PlaceSerializer(place)
        return Response(serialized_place.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        place_to_update = self.get_place(pk=pk) 
        updated_place = PlaceSerializer(place_to_update, data=request.data) 
        if updated_place.is_valid(): 
            updated_place.save() 
            return Response(updated_place.data, status=status.HTTP_202_ACCEPTED) 
        return Response(updated_place.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY) 

    def delete(self, _request, pk):
        place_to_delete = self.get_place(pk=pk)
        place_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







