class Order:
    def __init__(self, customer_name, category, destination):
        self.customer_name = customer_name
        self.category = category
        self.destination = destination

    def __str__(self):
        return f"{self.customer_name} | {self.category} | Destino: {self.destination}"