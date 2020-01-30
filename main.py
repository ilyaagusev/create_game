from faker import Faker
import file_operations as fo

text = {
    'first_name': 'ilya',
    'last_name': 'gusev'
}


#fo.render_template('charsheet.svg', 'charsheet1.svg', text)


fake = Faker('ru_Ru')
print(fake.name())
