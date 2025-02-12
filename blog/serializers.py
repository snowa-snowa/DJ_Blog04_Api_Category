from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from .models import Comment, Profile, BlogPost, Category



class ProfileSerializer(serializers.ModelSerializer):

    # students = serializers.HyperlinkedIdentityField(view_name='student-detail')
    """можно использовать, но работать будет некорректно, так как HyperlinkedIdentityField предназначен для связи
       моделей OneToOneField. покажет ссылку объекта с тем же id что и у объекта связанного с ним моделя, даже если
       такого объекта не существует он все ровно покажет ссылку"""

    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    """показывает выбранное поле объекта"""

    # students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')
    """показывает ссылки на все объекты"""

    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """показывает id объектов"""

    # students = serializers.StringRelatedField(many=True, read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
       моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = Profile
        fields = ('id', 'user', 'image',  'bio', 'phone_no', 'facebook', 'instagram', 'linkedin')



class BlogPostSerializer(serializers.ModelSerializer):

    # students = serializers.HyperlinkedIdentityField(view_name='student-detail')
    """можно использовать, но работать будет некорректно, так как HyperlinkedIdentityField предназначен для связи
       моделей OneToOneField. покажет ссылку объекта с тем же id что и у объекта связанного с ним моделя, даже если
       такого объекта не существует он все ровно покажет ссылку"""

    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    """показывает выбранное поле объекта"""

    # students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')
    """показывает ссылки на все объекты"""

    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """показывает id объектов"""

    # students = serializers.StringRelatedField(many=True, read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
       моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'author', 'slug', 'content', 'image', 'dateTime')



class CommentSerializer(serializers.ModelSerializer):

    # students = serializers.HyperlinkedIdentityField(view_name='student-detail')
    """можно использовать, но работать будет некорректно, так как HyperlinkedIdentityField предназначен для связи
       моделей OneToOneField. покажет ссылку объекта с тем же id что и у объекта связанного с ним моделя, даже если
       такого объекта не существует он все ровно покажет ссылку"""

    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    """показывает выбранное поле объекта"""

    blog = serializers.SlugRelatedField(read_only=True, slug_field='title')
    """показывает выбранное поле объекта"""

    # students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')
    """показывает ссылки на все объекты"""

    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """показывает id объектов"""

    # students = serializers.StringRelatedField(many=True, read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
       моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'blog', 'parent_comment', 'dateTime')



class CategorySerializer(serializers.ModelSerializer):

    # students = serializers.HyperlinkedIdentityField(view_name='student-detail')
    """можно использовать, но работать будет некорректно, так как HyperlinkedIdentityField предназначен для связи
       моделей OneToOneField. покажет ссылку объекта с тем же id что и у объекта связанного с ним моделя, даже если
       такого объекта не существует он все ровно покажет ссылку"""

    # user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    """показывает выбранное поле объекта"""

    posts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    """показывает выбранное поле объекта"""

    # students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')
    """показывает ссылки на все объекты"""

    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """показывает id объектов"""

    # blogposts = serializers.StringRelatedField(many=True, read_only=True)
    """показывает то что возвращается в admin или (object id). но так как связь OneToOneField и у одного объекта этого 
       моделя не может быть несколько объектов другого моделя, нужно убрать часть кода (many=True)"""

    class Meta:
        model = Category
        fields = ('id', 'name', 'posts')
