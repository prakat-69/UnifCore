from django.test import TestCase

from core.core_auth.models import User

from core.core_auth.services import (
    register_user,
    login_user,
    logout_user,
    get_user_profile,
    update_user_profile,
    delete_user,
)


class AccountServiceTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email="test@example.com",
            password="123456"
        )

    # -----------------------------
    # REGISTER
    # -----------------------------

    def test_register_user_success(self):
        user, error = register_user(
            username="newuser",
            email="new@example.com",
            password="password123"
        )

        self.assertIsNone(error)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "newuser")

    def test_register_user_duplicate_username(self):
        user, error = register_user(
            username="testuser",
            email="another@example.com",
            password="password123"
        )

        self.assertIsNone(user)
        self.assertEqual(error, "Username already exists")

    # -----------------------------
    # LOGIN
    # -----------------------------

    def test_login_user_success(self):
        user, error = login_user(
            username="testuser",
            password="123456"
        )

        self.assertIsNone(error)
        self.assertEqual(user.username, "testuser")

    def test_login_user_wrong_password(self):
        user, error = login_user(
            username="testuser",
            password="wrongpassword"
        )

        self.assertIsNone(user)
        self.assertEqual(error, "Invalid password")

    def test_login_user_not_found(self):
        user, error = login_user(
            username="unknown",
            password="123"
        )

        self.assertIsNone(user)
        self.assertEqual(error, "User not found")

    # -----------------------------
    # PROFILE
    # -----------------------------

    def test_get_user_profile_success(self):
        user, error = get_user_profile(self.user.id)

        self.assertIsNone(error)
        self.assertEqual(user.username, "testuser")

    def test_get_user_profile_not_found(self):
        user, error = get_user_profile(999)

        self.assertIsNone(user)
        self.assertEqual(error, "User not found")

    # -----------------------------
    # UPDATE
    # -----------------------------

    def test_update_user_profile_success(self):
        user, error = update_user_profile(
            self.user.id,
            username="updateduser",
            email="updated@example.com"
        )

        self.assertIsNone(error)
        self.assertEqual(user.username, "updateduser")
        self.assertEqual(user.email, "updated@example.com")

    def test_update_user_profile_not_found(self):
        user, error = update_user_profile(
            999,
            username="ghost"
        )

        self.assertIsNone(user)
        self.assertEqual(error, "User not found")

    # -----------------------------
    # DELETE
    # -----------------------------

    def test_delete_user_success(self):
        success, error = delete_user(self.user.id)

        self.assertTrue(success)
        self.assertIsNone(error)

    def test_delete_user_not_found(self):
        success, error = delete_user(999)

        self.assertFalse(success)
        self.assertEqual(error, "User not found")

    # -----------------------------
    # LOGOUT
    # -----------------------------

    def test_logout_user_success(self):
        success, error = logout_user(self.user.id)

        self.assertTrue(success)
        self.assertIsNone(error)

    def test_logout_user_not_found(self):
        success, error = logout_user(999)

        self.assertFalse(success)
        self.assertEqual(error, "User not found")