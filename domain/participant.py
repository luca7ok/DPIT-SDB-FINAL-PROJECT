class Participant:
    def __init__(self, name, picture_link, list_of_events):
        self.__name = name
        self.__picture_link = picture_link
        self.__list_of_events = list_of_events

    def get_name(self):
        return self.__name

    def get_picture(self):
        return self.__picture_link

    def get_list_of_events(self):
        return self.__list_of_events

    def append_list_of_events(self, event):
        self.__list_of_events = self.__list_of_events + [event]
        return self.__list_of_events

    def __str__(self):
        return f"Name: {self.__name}\n" \
               f"Picture: {self.__picture_link}\n" \
               f"List of events: {self.__list_of_events}\n"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_name() == other.get_name() and self.get_picture() == other.get_picture()
