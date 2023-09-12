# from rest_framework import serializers
# from .models import Book

# class BookSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    author = serializers.CharField()
#    title = serializers.CharField()
#    genre = serializers.CharField()
#    number_of_pages = serializers.IntegerField()
   
#    def create(self, data):
#        return Book.objects.create(**data)

#    def update(self, instance, data):
#         instance.author = data.get('author', instance.author)
#         instance.title = data.get('title', instance.title)
#         instance.genre = data.get('genre', instance.genre)
#         instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        
#         instance.save()
#         return instance



from rest_framework import serializers
from .models import Book
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    # description = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = "__all__" 

    def validate_title(self, value):
        if value == "Land of Mordor":
            raise ValidationError("No Land of Mordor please")
        return value

    def validate(self, data):
        if data["number_of_pages"] > 400 and data["quantity"] > 400:
            raise ValidationError("Too heavy for inventory")
        return data

    # def get_description(self, data):
    #     return "This book is called " + data.title + " and it is " + str(data.number_of_pages) + " pages long."
