from rest_framework import serializers
# here the modelsneed to be  imported
from college.models import Notice


# craeting  the hyperlink serialiser
class NoticeSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        # i am adding  the name of the model which is the model class 
        model=Notice
        # this is to add all the fields of the model
        fields="__all__" 
        