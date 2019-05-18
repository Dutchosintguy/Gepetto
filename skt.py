from faker import Faker # get it ? ... *sigh*
import random

# uses faker to create fake personnal data
# fake.simple_profile(sex=None) or fake.profile(fields=none, sex=None) can be used
# but are really messy
# edit : only some fields can be generated with .profile() so I didn't have a choice

def faker_info(gender,age):
    fake = Faker()
    if gender == "male" :
        print("\n\t\tM. " + fake.name_male())
    else :
        print("\n\t\tMs. " + fake.name_female())

    a = fake.profile(fields="residence,blood_group")
    print(
        "Personnal info : ",
        "\n\tUsername :" + fake.user_name(),
        "\n\tBirthdate : " + str(fake.date_of_birth(tzinfo=None, minimum_age=age, maximum_age=age)),
        "\n\tBlood group :" + a["blood_group"],
        "\n\tNationality : " + fake.bank_country(),
        "\n\tAddress : " + a["residence"],
        "\n\tSSN : " + fake.ssn(),
        "\n\tLicense plate : " + fake.license_plate(),

        "\nWork : ",
        "\n\tCompany : " + fake.company() + " " + fake.company_suffix(),
        "\n\tJob : " + fake.job(),

        "\nBanking : ",
        "\n\t" + fake.credit_card_provider(card_type=None),
        ":\n\t" + fake.credit_card_number(card_type=None),
        "\n\t" + fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
        "\t" + fake.credit_card_security_code(card_type=None),
        "\n\tBBAN : " + fake.bban(),
        "\n\tIBAN : " + fake.iban(),
    )
