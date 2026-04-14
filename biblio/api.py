from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from typing import List, Optional, Union, Literal
import datetime
 
from .models import *

 
api = NinjaAPI()
 
class LlibreOut(Schema):
    id: int
    titol: str
    autor: str
    data_edicio: Optional[date] = None
    resum: Optional[str]
 
@api.get("/llibres", response=List[LlibreOut])
@api.get("/llibres/", response=List[LlibreOut])
def obtenir_libres(request):
    qs = Llibre.objects.all()
    return qs