from crm.models import Company


class CompanyService:
    
    def update_or_create(self, data):
        try:
            # Block if data object exist, update
            _obj = Company.objects.get(idCompany=data['company-id'])
            _obj.name = data['company-name']
            _obj.address = data['address']
            _obj.status = data['status']
            _obj.set_legal()
            _obj.save()
        except:
            # Block if data object doesn't exist, create new
            self.__create(data)
        

    def __create(self, data):
        super().__init__(
                product_name=data['product-name'], 
                product_code=data['product-code'],
                category=data['category'],
                unit=data['unit'],
                date_in=data['date-in'],
                sender=data['sender'],
                storage_location=data['location']
                )
        self.save()
        
    def update(self):
        pass



def get_legal_type():
    return Company.LEGAL_CHOICES

def get_list():
    list_company = []
    ls = Company.objects.all()
    legal = get_legal_type()
    for company in ls:
        res = {}
        for i in legal:
            if (str(company.legal) == str(i[0])):
                res['idCompany'] = company.idCompany
                res['name'] = company.name
                res['address'] = company.address
                res['legal'] = i[1]
                res['status'] = company.status
                break
            else:
                if (str(i[0]) == '5'):
                    res['idCompany'] = company.idCompany
                    res['name'] = company.name
                    res['address'] = company.address
                    res['legal'] = 0
                    res['status'] = company.status
        list_company.append(res)
    return list_company