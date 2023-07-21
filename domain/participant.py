class Participant:
    def __init__(self, name, picture_link, list_of_events):
        """
        Constructor for Participant class
        :param name: name of the participant (str)
        :param picture_link: picture link of participant (str)
        :param list_of_events: list of events the participant attends (list)
        """
        self.__name = name
        self.__picture_link = picture_link
        self.__list_of_events = list_of_events

    def get_name(self):
        """
        Getter function that returns the name of a participant
        :return: name of a participant (str)
        """
        return self.__name

    def get_picture(self):
        """
        Getter function that returns the picture link of a participant
        :return: picture link of a participant (str)
        """
        return self.__picture_link

    def get_list_of_events(self):
        """
        Getter function that returns the list of events that a participant attends
        :return: list of events that a participant attends (list)
        """
        return self.__list_of_events

    def append_list_of_events(self, event):
        """
        Adds an event to the participant's list of events and returns the list
        :param event: event to be added (str)
        :return: list of events that a participant attends (list)
        """
        self.__list_of_events = self.__list_of_events + [event]
        return self.__list_of_events

    def __str__(self):
        """
        Returns the details of a participant
        :return: details of a participant (str)
        """
        return f"Name: {self.__name}\n" \
               f"Picture: {self.__picture_link}\n" \
               f"List of events: {self.__list_of_events}\n"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Verifies if two participants are the same by comparing their name and their picture link
        :param other: another participant (Participant)
        :return: True if they are the same, False otherwise
        """
        return self.get_name() == other.get_name() and self.get_picture() == other.get_picture()
