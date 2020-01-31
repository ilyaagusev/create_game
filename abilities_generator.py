import random
from faker import Faker

import text_templates as tt


def generate_number():
    number = random.randint(8, 14)
    return number


def transliterate_skill(skill):
    transliterated_letters = []
    for letter in skill:
        runic_letter = letter.replace(letter, tt.letters_mapping[letter])
        transliterated_letters.append(runic_letter)
    transliterated_to_runic = ''.join(transliterated_letters)
    return transliterated_to_runic


def generate_abilities():
    fake = Faker('ru_Ru')
    first_name = fake.first_name_male()
    last_name = fake.last_name_male()
    job = fake.job()
    city = fake.city()

    strength = generate_number()
    agility = generate_number()
    endurance = generate_number()
    intelligence = generate_number()
    luck = generate_number()

    random_skills = random.sample(tt.skills, 3)
    runic_skills = []
    for skill in random_skills:
        skill = transliterate_skill(skill)
        runic_skills.append(skill)

    abilities = {
        'first_name': first_name,
        'last_name': last_name,
        'job': job,
        'town': city,
        'strength': strength,
        'agility': agility,
        'endurance': endurance,
        'intelligence': intelligence,
        'luck': luck,
        'skill_1': runic_skills[0],
        'skill_2': runic_skills[1],
        'skill_3': runic_skills[2],
        }

    return abilities
