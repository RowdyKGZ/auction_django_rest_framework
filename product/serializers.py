from rest_framework import serializers

from product.models import Product, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер к категориям"""
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер к категориям"""
    author = serializers.CharField(read_only=True)
    create_at = serializers.DateTimeField(read_only=True)
    Product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер к продукту и вывод несколько картинок"""
    class Meta:
        model = Product
        fields = '__all__'

    def _get_image_url(self, obj):
        request = self.context.get('request')
        image_obj = obj.images.first()
        if image_obj is not None and image_obj.image:
            url = image_obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
            return url
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        representation['categories'] = CategorySerializer(instance.category.all(), many=True).data
        representation['comments'] = CommentSerializer(instance.category.all(), many=True).data
        return representation


class ProductListSerializer(serializers.ModelSerializer):
    """Продукт сериалайзер и вывод дочерних подклассов с картинкой"""
    class Meta:
        model = Product
        exclude = ('description',)

    def _get_image_url(self, obj):
        request = self.context.get('request')
        image_obj = obj.images.first()
        if image_obj is not None and image_obj.image:
            url = image_obj.image.url
            if request is not None:
                url = request.build_absolute_uri(url)
            return url
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        representation['categories'] = CategorySerializer(instance.category.all(), many=True).data
        return representation


class CreateUpdateProductSerializer(serializers.ModelSerializer):
    """Сериалайзер для апдейт и криейт продукта"""
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'category')
