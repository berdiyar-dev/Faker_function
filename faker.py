from faker import Faker
import random
fake = Faker()
res = ''
for i in range(20):
    id = random.randint(1, 20)
    fname = "'" + fake.name() + "'"
    email = "'" + fake.email() + "'"
    country = "'" + fake.country() + "'"
    res += f"INSERT INTO public.deletes (id, fname, email, country) VALUES({id}, {fname}, {email},{country}); \n"
print(res)