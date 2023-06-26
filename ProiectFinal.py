import requests
from time import sleep

API_URL = 'https://api.publicapis.org'


class TestPublicapisApi:
    def test_health(self):
        raspuns = requests.get(f"{API_URL}/health")
        assert raspuns.status_code == 200
        assert len(raspuns.json()) > 0
        assert raspuns.json()["alive"]

    def test_categories(self):
        raspuns = requests.get(f"{API_URL}/categories")
        assert raspuns.status_code == 200
        assert len(raspuns.json()) > 0
        nr_categorii = raspuns.json()['count']
        assert type(nr_categorii) == int
        categorii = raspuns.json()['categories']
        assert categorii
        assert nr_categorii == len(categorii)


    def test_random(self):
        raspuns = requests.get(f"{API_URL}/random")
        assert raspuns.status_code == 200
        assert len(raspuns.json()) > 0
        nr_intrari = raspuns.json()['count']
        assert type(nr_intrari) == int
        assert nr_intrari == 1
        intrari = raspuns.json()['entries']
        assert len(intrari) == 1
        intrare_random = intrari[0]
        assert type(intrare_random) == dict
        cheie_dict = intrare_random['API']
        assert type(cheie_dict) == str
        cheie_dict = intrare_random['Description']
        assert type(cheie_dict) == str
        cheie_dict = intrare_random['Auth']
        assert type(cheie_dict) == str
        cheie_dict = intrare_random['HTTPS']
        assert type(cheie_dict) == bool
        cheie_dict = intrare_random['Cors']
        assert type(cheie_dict) == str
        cheie_dict = intrare_random['Link']
        assert type(cheie_dict) == str
        cheie_dict = intrare_random['Category']
        assert type(cheie_dict) == str

    def test_entries(self):
        raspuns = requests.get(f"{API_URL}/entries")
        assert raspuns.status_code == 200
        assert len(raspuns.json()) > 0
        nr_intrari = raspuns.json()['count']
        assert type(nr_intrari) == int
        intrari = raspuns.json()['entries']
        assert nr_intrari == len(intrari)
        for intrare in intrari:
            cheie_dict = intrare['API']
            assert type(cheie_dict) == str
            cheie_dict = intrare['Description']
            assert type(cheie_dict) == str
            cheie_dict = intrare['Auth']
            assert type(cheie_dict) == str
            cheie_dict = intrare['HTTPS']
            assert type(cheie_dict) == bool
            cheie_dict = intrare['Cors']
            assert type(cheie_dict) == str
            cheie_dict = intrare['Link']
            assert type(cheie_dict) == str
            cheie_dict = intrare['Category']
            assert type(cheie_dict) == str

test = TestPublicapisApi()
test.test_health()
print("test_health\t\tOK")
sleep(0.5)
test.test_categories()
print("test_categories\tOK")
sleep(0.5)
test.test_random()
print("test_random\t\tOK")
sleep(0.5)
test.test_entries()
print("test_entries\tOK")
