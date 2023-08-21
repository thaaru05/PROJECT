import phonenumbers
from test import test_abstract_numbers


from phonenumbers import geocoder
number=int(input('Enter the number:'))
ch_nmber=phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(ch_nmber,'en'))

from phonenumbers import carrier
service_nmber=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_nmber,'en'))