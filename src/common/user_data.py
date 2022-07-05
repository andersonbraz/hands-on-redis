from faker import Faker

fake = Faker("pt_BR")


def get_user():

    return {
        "name": fake.name(),
        "address": fake.address(),
        "postcode": fake.postcode(),
        "phone_number": fake.phone_number(),
        "ssn": fake.ssn(),
    }


if __name__ == "__main__":
    print(get_user())
