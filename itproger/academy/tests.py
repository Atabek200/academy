from django.test import TestCase
from .models import Ticket, Masters, Status


class TicketModelTest(TestCase):
    def setUp(self):
        self.master = Masters.objects.create(name="Test Masters", email="test@masters.com")
        self.status = Status.objects.create(name="Open")
        self.ticket = Ticket.objects.create(
            title="Test Ticket",
            description="This is a test ticket",
            master=self.master,
            status=self.status
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.title, "Test Ticket")
        self.assertEqual(self.ticket.description, "This is a test ticket")
        self.assertEqual(self.ticket.master.name, "Test Master")
        self.assertEqual(self.ticket.status.name, "Open")

