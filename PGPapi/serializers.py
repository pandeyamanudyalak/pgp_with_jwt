from rest_framework import serializers
from .models import *

class userLoginSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=200)

    class Meta:
        model = CustomUser
        fields= ['id','name','email','password']

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class userLocationSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=200)
    class Meta:
        model = userLocation
        fields=['id','location']

    def create(self, validated_data):
        return userLocation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.location = validated_data.get('location',instance.location)
        instance.save()
        return instance

class userRoleSerializer(serializers.ModelSerializer):
    # user_role = serializers.PrimaryKeyRelatedField(read_only=False,
    #                                                queryset=userDetails.objects.all())
    roleName = serializers.CharField(max_length=200)
    class Meta:
        model = userRole
        fields=['id','roleName']

    def create(self, validated_data):
        return userRole.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.roleName = validated_data.get('roleName',instance.roleName)
        instance.save()
        return instance 

class userDetailSerializer(serializers.ModelSerializer):
    userName = serializers.SlugRelatedField(read_only=False,slug_field="name",
                                                   queryset=CustomUser.objects.all())
    userLocation = serializers.SlugRelatedField(read_only=False,slug_field="location",
                                                   queryset=userLocation.objects.all())
    userRole = serializers.SlugRelatedField(read_only=False,slug_field="roleName",
                                                   queryset=userRole.objects.all())

    class Meta:
        model = userDetails
        fields=('id','userName','userLocation','userRole')
        depth=1

    def create(self, validated_data):
        return userDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userName = validated_data.get('userName',instance.userName)
        instance.userLocation = validated_data.get('userLocation', instance.userLocation)
        instance.userRole = validated_data.get('userRole', instance.userRole)
        instance.save()
        return instance

class issueAgencySerializer(serializers.ModelSerializer):
    agencyName = serializers.CharField(max_length=200)
    class Meta:
        model = issueAgency
        fields = ('id', 'agencyName')

    def create(self, validated_data):
        return issueAgency.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.agencyName = validated_data.get('agencyName',instance.agencyName)
        instance.save()
        return instance

class formDataSerializer(serializers.ModelSerializer):
    loggedPerson = serializers.SlugRelatedField(read_only=False,slug_field="name",
                                                   queryset=CustomUser.objects.all())
    date = serializers.DateField()
    typeOfWork = serializers.CharField(max_length=500)
    numberOfPerson = serializers.IntegerField()
    startTime = serializers.TimeField()
    endTime = serializers.TimeField()
    location = serializers.SlugRelatedField(read_only=False,slug_field="location",
                                                   queryset=userLocation.objects.all())
    equipment = serializers.CharField(max_length=200)
    toolRequired = serializers.CharField(max_length=200)
    workingAgency = serializers.SlugRelatedField(read_only=False,slug_field="agencyName",
                                                   queryset=issueAgency.objects.all())
    workDescription = serializers.CharField(max_length=500)
    ppeRequired = serializers.CharField(max_length=200)
    person1 = serializers.SlugRelatedField(read_only=False,slug_field="name",
                                                   queryset=CustomUser.objects.all())
    person2 = serializers.SlugRelatedField(read_only=False,slug_field="name",
                                                   queryset=CustomUser.objects.all())
    notifyflagPerson1 = serializers.BooleanField(default=False)
    notifyflagPerson2 = serializers.BooleanField(default=False)
    newFlag = serializers.BooleanField(default=False)
    oldFlag = serializers.BooleanField(default=False)
    closeFlag = serializers.BooleanField(default=False)
    completedFlag = serializers.BooleanField(default=False)

    class Meta:
        model = formData
        fields = ('id','loggedPerson','date','typeOfWork','numberOfPerson','startTime','endTime','location',
                 'equipment','toolRequired','workingAgency','workDescription','ppeRequired','person1','person2',
                 'notifyflagPerson1','notifyflagPerson2','newFlag','oldFlag','closeFlag','completedFlag','closedByLoggedUser','closedByPerson1','verified_by_person1','verified_by_person2')

    def create(self, validated_data):
        return formData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date',instance.date)
        instance.typeOfWork = validated_data.get('typeOfWork', instance.typeOfWork)
        instance.numberOfPerson = validated_data.get('numberOfPerson', instance.numberOfPerson)
        instance.startTime = validated_data.get('startTime', instance.startTime)
        instance.endTime = validated_data.get('endTime', instance.endTime)
        instance.location = validated_data.get('location', instance.location)
        instance.equipment = validated_data.get('equipment', instance.equipment)
        instance.toolRequired = validated_data.get('toolRequired', instance.toolRequired)
        instance.workingAgency = validated_data.get('workingAgency', instance.workingAgency)
        instance.ppeRequired = validated_data.get('ppeRequired', instance.ppeRequired)
        instance.person1 = validated_data.get('person1', instance.person1)
        instance.person2 = validated_data.get('person2', instance.person2)
        instance.newFlag = validated_data.get('newFlag', instance.newFlag)
        instance.oldFlag = validated_data.get('oldFlag', instance.oldFlag)
        instance.closeFlag = validated_data.get('closeFlag', instance.closeFlag)
        instance.completedFlag = validated_data.get('completedFlag', instance.completedFlag)
        instance.notifyflagPerson1 = validated_data.get('notifyflagPerson1', instance.notifyflagPerson1)
        instance.notifyflagPerson2 = validated_data.get('notifyflagPerson2', instance.notifyflagPerson2)
        instance.closedByLoggedUser = validated_data.get('closedByLoggedUser', instance.closedByLoggedUser)
        instance.closedByPerson1 = validated_data.get('closedByPerson1', instance.closedByPerson1)
        instance.verified_by_person1 = validated_data.get('verified_by_person1', instance.verified_by_person1)
        instance.verified_by_person2 = validated_data.get('verified_by_person2', instance.verified_by_person2)
       
        instance.save()
        return instance



class personSerializer(serializers.Serializer):
   person = serializers.SlugRelatedField(read_only=False,slug_field="name", queryset=CustomUser.objects.all())
   form = serializers.SlugRelatedField(read_only=False,slug_field="id", queryset=formData.objects.all())
   new_notification = models.BooleanField(default=False)

