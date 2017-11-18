from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Post

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Post(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Post.objects.count()
        self.bucketlist.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)