from django.apps import AppConfig
import redis


class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        import news.signals

red = redis.Redis(
    host='redis-16707.c54.ap-northeast-1-2.ec2.cloud.redislabs.com',
    port='16707',
    password='49yFCATjG4vXzZD0IcWDM6CcvoOEahOk'
)






