from costumer import Costumer
from register import Register
import json

c1 = Costumer("ezra")
c1.add_product()
c1.add_product()
c1.remove_product()


c2 = Costumer("moshe")
c2.add_product()
c2.add_product()
c2.remove_product()


r1 = Register("r1")
r1.checkout_customer(c1)
r1.checkout_customer(c2)
r1.print_summary()


c3 = Costumer("dave")
c3.add_product()
c3.add_product()
c3.remove_product()

r2 = Register("r2")
r2.checkout_customer(c3)
r2.print_summary()


customer_info = [c1.add_json(), c2.add_json(), c3.add_json()]

summary = open("Ezra\supermarket 2.0\summary.json", "w")
summary.write(json.dumps(customer_info))




