import random
from decimal import Decimal
import time

def generate_order_data():
    """Generate random order data."""
    orderid = str(random.randint(1, 10000))  # Random order ID between 1 and 10000
    product_name = random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'])
    quantity = random.randint(1, 5)
    price = Decimal(str(round(random.uniform(10.0, 500.0), 2)))
    
    return {
        'orderid': orderid,
        'product_name': product_name,
        'quantity': quantity,
        'price': price
    }

if __name__ == '__main__':
    try:
        while True:
            data = generate_order_data()
            print("Generated Order Data:", data)
            time.sleep(0.1)  # Sleep for 3 seconds
    except KeyboardInterrupt:
        print("\nScript stopped by manual intervention!")
