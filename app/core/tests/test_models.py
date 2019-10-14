from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test create user with email address successful"""
        email = "aeiou@gmail.com"
        password = "hello123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test new user email is normalized"""
        email = 'aeiou@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'abc123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if new user email is valid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'abc123')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        email = 'aeiou@gmail.com'
        user = get_user_model().objects.create_superuser(email, 'abc123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
