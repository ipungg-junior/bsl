import re
from apps.service import _encrypt
from apps.models import UserBsl

def has_symbol(text):
    # Pola regex untuk mendeteksi simbol
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?\/\\|~-]'

    # Mencocokkan pola regex dengan string
    if re.search(pattern, text):
        return True
    else:
        return False

class UserAccount:

    @staticmethod
    def create(dataform):
        _h = _encrypt.HashTokenAccess().generate_hash((dataform["phone"] + ':systema'))
        print(has_symbol(dataform['username']))
        if (dataform['phone'] == ''):
            return (None, {'status': 400, 'message':'Isi nomor Anda!'})
        if (dataform['username'] == ''):
            return (None, {'status': 400, 'message':'Isi username Anda!', 'form':{'phone':dataform['phone']}})
        if (has_symbol(dataform['username'])):
            return (None, {'status': 400, 'message':'Dilarang menggunakan karakter untuk username', 'form':{'phone':dataform['phone'], 'username': dataform['username']}})
        if (dataform['password'] == ''):
            return (None, {'status': 400, 'message':'Isi password Anda!', 'form':{'phone':dataform['phone'], 'username': dataform['username']}})

        # Checking confirm password
        if (dataform['password'] == dataform['password-confirmation']):
            print(dataform['password'])
            new_user = UserBsl()
            new_user.phone_number = dataform['phone']
            new_user.uid = _h
            new_user.username = dataform['username']
            new_user.set_password(dataform['password'])
            new_user.save()
            print('sukses buat akun baru')
            return (True, new_user)
        else:
            return (None, {'status': 401, 'message':'Password tidak cocok!.'})