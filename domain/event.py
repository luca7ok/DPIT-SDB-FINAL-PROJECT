class Event:
    def __init__(self, id, name, city, number_of_participants, max_capacity, start_date, end_date):
        self.__id = id
        self.__name = name
        self.__city = city
        self.__number_of_participants = number_of_participants
        self.__max_capacity = max_capacity
        self.__start_date = start_date
        self.__end_date = end_date

    def get_id(self):
        return self.__id

    def get_city(self):
        return self.__city

    def get_number_of_participants(self):
        return self.__number_of_participants

    def get_max_capacity(self):
        return self.__max_capacity

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def set_name(self, new_name):
        self.__name = new_name

    def set_city(self, new_city):
        self.__city = new_city

    def set_number_of_participants(self, new_number_of_participants):
        self.__number_of_participants = new_number_of_participants

    def set_max_capacity(self, new_max_capacity):
        self.__max_capacity = new_max_capacity

    def set_start_date(self, new_start_date):
        self.__start_date = new_start_date

    def set_end_date(self, new_end_date):
        self.__end_date = new_end_date

    def __str__(self):
        return f"ID: {self.__id}\n" \
               f"Name: {self.__name}\n" \
               f"City: {self.__city}\n" \
               f"Number of participants: {self.__number_of_participants}\n" \
               f"Max capacity: {self.__max_capacity}\n" \
               f"Start date: {self.__start_date}\n" \
               f"End date: {self.__end_date}\n"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_id() == other.get_id()
