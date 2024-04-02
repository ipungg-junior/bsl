from crm.models import ContactPerson

def get_contact_type():
    return ContactPerson.TYPE_CHOICES

def get_list():
    return ContactPerson.objects.all()

def create_new(name, phone, email, legal):
    new_person = ContactPerson(name=name, phone_number=phone)
    new_person.set_legal(legal)
    new_person.save()