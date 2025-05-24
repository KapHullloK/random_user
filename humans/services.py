import requests
from django.urls import reverse

from humans.models import Human


def get_random_humans(cnt: int):
    data = []
    cnt_humans_in_request = 1000
    for i in range((cnt // cnt_humans_in_request) + 1):
        try:
            url = f"https://randomuser.me/api/?results={cnt_humans_in_request}"
            response = requests.get(url)
            json_response = response.json()
            data.extend(json_response['results'])
        except Exception as e:
            pass

    return data


def load_human(data) -> None:
    for new_human in data:
        human = Human.objects.create(
            gender=new_human["gender"],
            first_name=new_human["name"]["first"],
            last_name=new_human["name"]["last"],
            phone_number=new_human["phone"],
            email=new_human["email"],
            avatar=new_human["picture"]['large'],
            street=new_human["location"]['street']['name'] + " " + str(new_human["location"]['street']['number']),
            city=new_human["location"]['city'],
            country=new_human["location"]['country'],
        )

        human.link_to_details = reverse('humans:detail-humans', args=[human.pk])
        human.save(update_fields=['link_to_details'])


def create_humans_by_cnt(cnt: int) -> None:
    cur_cnt = Human.objects.all().count()

    if cnt > cur_cnt:
        data = get_random_humans(cnt - cur_cnt)
        load_human(data)
