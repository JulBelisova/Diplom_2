class UrL:
    BASE_URL = "https://stellarburgers.education-services.ru"
    CREATE_USER_ENDPOINT = f"{BASE_URL}/api/auth/register"
    LOGIN_ENDPOINT = f"{BASE_URL}/api/auth/login"
    ORDER_ENDPOINT = f"{BASE_URL}/api/orders"
url = UrL()