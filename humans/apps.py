from django.apps import AppConfig


class HumansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'humans'

    def ready(self):
        from humans.services import create_humans_by_cnt

        try:
            create_humans_by_cnt(cnt=1000)
        except Exception as e:
            print("Таблица ещё не готова.")
