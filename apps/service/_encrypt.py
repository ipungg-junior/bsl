import hashlib

class HashTokenAccess():

    @staticmethod
    def generate_hash(phone_number):
        phone_number_byte = (phone_number+':systema').encode('utf-8')
        sha2_hash = hashlib.sha256(phone_number_byte).hexdigest()
        return sha2_hash