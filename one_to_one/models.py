from django.db import models


class Place(models.Model):
    address = models.CharField('주소', max_length=200)

    def __str__(self):
        return f'Place (address: {self.address})'


class Restaurant(models.Model):
    place = models.OneToOneField(Place, verbose_name='장소', on_delete=models.CASCADE)
    # instagram_user = models.ForeignKey(InstagramUser) import하면 다른 app에서 가져올 수 있음
    # instagram_user = models.ForeignKey('many_to_many.InstagramUser') 문자열형식으로 가져올 경우
    name = models.CharField('식당명', max_length=30)
    rating = models.IntegerField('평점', default=0)

    def __str__(self):
        return f'{self.name} (평점: {self.rating})'
