from rest_framework.serializers import ModelSerializer
from telegram.models import Country
from datetime import datetime
class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = ("name","new","deaths","recovered","active","total","date",)
    
    def to_internal_value(self,data):
        name = data.pop("Country,Other").lower()
        if type(data.get("NewCases"))==float:
            new = int(data.pop("NewCases"))
        else:
            new = int(data.pop("NewCases").replace(",",""))
        deaths = int(data.pop("TotalDeaths"))
        recovered = int(data.pop("TotalRecovered"))
        active = int(data.pop("ActiveCases"))
        total = int(data.pop("TotalCases"))
        date = datetime.now()
        
        if not total == active+recovered+deaths:
            total = active+recovered+deaths

        internal_data={
        "name" : name,
        "new" : new,
        "deaths" : deaths,
        "recovered" : recovered,
        "active" : active,
        "total" : total,
        "date" : date
        }
        return super().to_internal_value(internal_data)

    def to_representation(self,instance):
        instance.date = instance.date.strftime("%d-%b-%Y  %H:%M")
        return super().to_representation(instance)