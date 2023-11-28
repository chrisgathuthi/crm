from django.test import TestCase
import datetime
from accounts.models import Bandwidth, Client

class TestBandwidthModel(TestCase):

    """Testcases bandwidth model"""

    def setUp(self):
        data = {
            "name":"poa plan",
            "size": 10,
            "expiry": datetime.date.today()
        }
        self.bandwidth = Bandwidth.objects.create(**data)
        return super().setUp()
    
    def test_string_method(self):
        self.assertTrue(self.bandwidth, "10 mbs")
    
    def test_bandwidth_instance(self):
        self.assertTrue(isinstance(self.bandwidth, Bandwidth))
    
    def test_bandwidth_attributes(self):
        self.assertTrue(hasattr(self.bandwidth, "name"))
        self.assertTrue(hasattr(self.bandwidth, "size"))
        self.assertTrue(hasattr(self.bandwidth, "expiry"))


class TestClientModel(TestCase):
    """test client model"""

    def setUp(self):
        data = {
            "name":"poa plan",
            "size": 10,
            "expiry": datetime.date.today()
        }
        self.bandwidth = Bandwidth.objects.create(**data)

        data = {
            "first_name":"lamp",
            "last_name":"lamp",
            "phone_number":"254776082635",
            "password":"helloworld",
            "email":"hello@gmail.com",
            "location":"thika",
            "router":"tenda1",
            "bandwidth": self.bandwidth,
            "service_plan":"PPOE",
            "status":"ACTIVE"
        }
        self.client = Client.objects.create(**data)
        return super().setUp()

    def test_string_method(self):
        self.assertTrue(self.client, "lamp lamp")
    
    def test_bandwidth_client_relation(self):
        self.assertTrue(self.client.bandwidth, self.bandwidth)

    def test_client_attributes(self):
        self.assertTrue(hasattr(self.client, "serial"))
        self.assertTrue(hasattr(self.client, "first_name"))
        self.assertTrue(hasattr(self.client, "last_name"))
        self.assertTrue(hasattr(self.client, "password"))
        self.assertTrue(hasattr(self.client, "email"))
        self.assertTrue(hasattr(self.client, "location"))
        self.assertTrue(hasattr(self.client, "router"))
        self.assertTrue(hasattr(self.client, "bandwidth"))
        self.assertTrue(hasattr(self.client, "service_plan"))
        self.assertTrue(hasattr(self.client, "status"))
        self.assertTrue(hasattr(self.client, "registration_date"))


class FieldWork(TestCase):

    """test fieldwork model"""

    def setUp(self):
        data = {
            
        }
        data = {
            "task_name":"line repair",
            "location":"thika",
            "activities":"line repairs",
            "assignee":"",
            "date":datetime.date.today()
        }
        return super().setUp()
        