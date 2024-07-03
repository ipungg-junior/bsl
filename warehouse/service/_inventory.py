from warehouse import models

class InventoryService(models.Inventory):

    def update_or_create(self, data):
        try:
            # Block if data object exist, update
            _obj = models.Inventory.objects.get(product_code=data['product-code'])
            _obj.product_name = data['product-name']
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

    def get_item(self, product_code):
        item = models.Inventory.objects.filter(product_code=product_code)
        regex_item = {
            'product_code': item[0].product_code,
            'product_name': item[0].product_name,
            'category': item[0].category,
            'date_in': item[0].date_in,
            'sender': item[0].sender,
            'storage_location': item[0].storage_location
        }
        regex_item['storage_location'] = item[0].get_location(regex_item['storage_location'])
        return regex_item

    def get_all(self):
        data = models.Inventory.objects.all()
        return data

    def get_location(self):
        _m = models.Inventory()
        return _m.get_location()
    
    def get_category_type(Self):
        return models.Inventory().CATEGORY_CHOICES
    
    def location_options(Self):
        return models.Inventory().LOCATION_CHOICES