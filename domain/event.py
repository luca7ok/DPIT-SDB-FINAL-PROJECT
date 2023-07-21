class Event:
    def __init__(self, id, name, city, number_of_participants, max_capacity, start_date, end_date, website_link):
        """
        Constructor function for Event class
        :param id: id of event (str)
        :param name: name of event (str)
        :param city: city in which event takes place (str)
        :param number_of_participants: number of participants at event (int)
        :param max_capacity: maximum number of participants at event (int)
        :param start_date: start date of event (str)
        :param end_date: end date of event (str)
        :param website_link: website link of event (str)
        """
        self.__id = id
        self.__name = name
        self.__city = city
        self.__number_of_participants = number_of_participants
        self.__max_capacity = max_capacity
        self.__start_date = start_date
        self.__end_date = end_date
        self.__website_link = website_link

    def get_id(self):
        """
        Getter function that returns the id of an event
        :return: id of an event (str)
        """
        return self.__id
    def get_name(self):
        """
        Getter function that return the name of an event
        :return: name of an event (str)
        """
        return self.__name
    def get_city(self):
        """
        Getter function that returns the city an event takes place in
        :return: citi an event takes place in (str)
        """
        return self.__city

    def get_number_of_participants(self):
        """
        Getter function that returns the number of participants at an events
        :return: number of participants at an events (int)
        """
        return self.__number_of_participants

    def get_max_capacity(self):
        """
        Getter function that returns the maximum capacity of an event
        :return: maximum capacity of an event (int)
        """
        return self.__max_capacity

    def get_start_date(self):
        """
        Getter function that returns the start date of an event
        :return: start date of an event (str)
        """
        return self.__start_date

    def get_end_date(self):
        """
        Getter function that returns the end date of an event
        :return: end date of an event (str)
        """
        return self.__end_date
    def get_website_link(self):
        """
        Getter function that return the website link of an event
        :return: website link of an event (str)
        """
        return self.__website_link
    def set_name(self, new_name):
        """
        Setter function that changes the name of an event
        :param new_name: new name (str)
        :return:
        """
        self.__name = new_name

    def set_city(self, new_city):
        """
        Setter function that changes the city an event takes place in
        :param new_city: new city (str)
        :return:
        """
        self.__city = new_city

    def set_number_of_participants(self, new_number_of_participants):
        """
        Setter function that changes the number of participants at an events
        :param new_number_of_participants: new number of participants (int)
        :return:
        """
        self.__number_of_participants = new_number_of_participants

    def set_max_capacity(self, new_max_capacity):
        """
        Setter function that changes the maximum capacity of an event
        :param new_max_capacity: new maximum capacity (int)
        :return:
        """
        self.__max_capacity = new_max_capacity

    def set_start_date(self, new_start_date):
        """
        Setter function that changes the start date of an event
        :param new_start_date: new start date (str)
        :return:
        """
        self.__start_date = new_start_date

    def set_end_date(self, new_end_date):
        """
        Setter function that changes the end date of an event
        :param new_end_date: new end date (str)
        :return:
        """
        self.__end_date = new_end_date

    def set_website_link(self, new_website_link):
        """
        Setter function that changes the website link of an event
        :param new_website_link: new website link (str)
        :return:
        """
        self.__website_link = new_website_link

    def __str__(self):
        """
        Returns the details of an event
        :return: details of an event (str)
        """
        return f"ID: {self.__id}\n" \
               f"Name: {self.__name}\n" \
               f"City: {self.__city}\n" \
               f"Number of participants: {self.__number_of_participants}\n" \
               f"Max capacity: {self.__max_capacity}\n" \
               f"Start date: {self.__start_date}\n" \
               f"End date: {self.__end_date}\n" \
               f"Website link: {self.__website_link}\n"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Verifies if two events are the same by checking their id
        :param other: another event (Event)
        :return: True of they are the same, False otherwise
        """
        return self.get_id() == other.get_id()
