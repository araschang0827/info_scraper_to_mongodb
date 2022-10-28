from get_info.main import get_information
import requests

# use Selenium to get data
with get_information(teardown=True) as bot:
    bot.land_on_first_page()
    bot.login_page()
    bot.user_password('username', 'password')
    bot.login_button()
    bot.land_on_home_page()
    name = bot.find_name()
    ID = bot.find_ID()
    DEPT = bot.find_DEPT()

# api urls storage
base_URL_1 = 'http://127.0.0.1:5000/infos'
base_URL_2 = 'http://127.0.0.1:5000/info'

# get the qty of the database to create new _id
data_qty = len(requests.get(base_URL_1).json())

# assembling new data
post_data = {
    '_id': data_qty + 1,
    'name': name,
    'ID': ID,
    'DEPT': DEPT,
}

# post new data to the database by the rest api
result = requests.post(base_URL_1, json=post_data)
print(result)
print(result.json())
