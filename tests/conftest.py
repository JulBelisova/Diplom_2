import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest 
from ..methods.create_user_methods import CreateUserMethods

@pytest.fixture
def created_user():
    user_data = CreateUserMethods.register_new_user_and_return_login_password()
    return user_data