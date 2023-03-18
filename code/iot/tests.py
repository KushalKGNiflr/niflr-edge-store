from django.test import TestCase
from .video_pipeline import mapping
import environ
# import .vid
env = environ.Env(
    DEBUG=(bool, False)
)

class FxnTestCase(TestCase):
    def test_fxn(self):
        # Test your function here
        folder_path='.vid'
        result = mapping(folder_path)
        print(result)
        # self.assertEqual(result, expected_result)
