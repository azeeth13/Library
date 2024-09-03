from rest_framework.serializers import ModelSerializer, SerializerMethodField
from blog.models import *

class KitoblarSer(ModelSerializer):
    # category = SerializerMethodField()
    # def get_category(self, obj):
    #     return obj.category.name()
    
    class Meta:
        model = Book
        fields = '__all__'

class CategSer(ModelSerializer):
    # category = SerializerMethodField()
    # def get_category(self, obj):
    #     return obj.category.name()
    
    class Meta:
        model = Category
        fields = '__all__'
