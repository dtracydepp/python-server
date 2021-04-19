class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, firstName, lastName, email, password,status):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.status = status

new_customer = Customer(1, "Ava", "Marie", "ava@me.com", "ava1", "active")