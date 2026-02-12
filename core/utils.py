import random
import string
from datetime import datetime

def generate_order_number():
    date_part = datetime.now().strftime('%Y%m%d')
    random_part = ''.join(random.choices(string.digits, k=4))
    return f"ORD-{date_part}-{random_part}"