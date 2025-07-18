from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Port
from .serializers import PortSerializer
from django.shortcuts import get_object_or_404
from datetime import date
import searoute as sr

class PortList(APIView):
    def get(self, request):
        ports = Port.objects.all()
        serializer = PortSerializer(ports, many=True)
        return Response(serializer.data)

class TrajetEstimate(APIView):
    def get(self, request):
        depart_code = request.GET.get('depart')
        arrivee_code = request.GET.get('arrivee')
        print(depart_code, arrivee_code)
        

        if not depart_code or not arrivee_code:
            return Response({"error": "Paramètres 'depart' et 'arrivee' requis."}, status=status.HTTP_400_BAD_REQUEST)

        port_depart = get_object_or_404(Port, code=depart_code)
        port_arrivee = get_object_or_404(Port, code=arrivee_code)
        
        origin = [ port_depart.longitude,port_depart.latitude]    # Marseille
        destination = [ port_arrivee.longitude, port_arrivee.latitude]
        
        route = sr.searoute(origin, destination)
        
                # Afficher la longueur
        # print(f"Distance : {route.properties['length']} {route.properties['units']}")

        # Afficher les coordonnées du trajet
        # for coord in route.geometry['coordinates']:
        #     print(coord)

        print(route.geometry["coordinates"])
        
        

        from math import radians, sin, cos, sqrt, atan2

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371
            dlat = radians(lat2 - lat1)
            dlon = radians(lon2 - lon1)
            a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            return R * c

        #dist_km = haversine(port_depart.latitude, port_depart.longitude, port_arrivee.latitude, port_arrivee.longitude)
        dist_km = route.properties["length"]
        vitesse_moyenne = 40
        duree_estimee = round(dist_km / vitesse_moyenne)
        emission_co2 = round(dist_km * 3)

        # trajet_data = {
        #     "port_depart": PortSerializer(port_depart).data,
        #     "port_arrivee": PortSerializer(port_arrivee).data,
        #     "date_depart": date.today(),
        #     "duree_estimee": duree_estimee,
        #     "emission_co2": emission_co2
        # }
        path = [[lat, lon] for lon, lat in route.geometry["coordinates"]]

        trajet_data= {
            "date_depart": date.today(),
            "duree_estimee": duree_estimee,
            "emission_co2": emission_co2,
            "length": route.properties["length"],
            "units": route.properties["units"],
            "path": path
            
        }

        return Response(trajet_data)
