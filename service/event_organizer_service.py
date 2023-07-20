from domain.event import Event
from repository.repository import Repository

from datetime import timedelta, datetime


class EventOrganizerService:
    def __init__(self, repository: Repository):
        """
        Constructor for EventOrganizerService class:
        :param repository: event organizer repository (Repository)
        """
        self.__repository = repository

    # Organizer option-1
    def add_event(self, id, name, city, number_of_participants, max_capacity, start_date, end_date):
        """
        Adds an event to the list of events if it does not exist already
        :param id: id of the event (str)
        :param name: name of event (str)
        :param city: city where event takes place (str)
        :param number_of_participants: number of participants at event (int)
        :param max_capacity: maximum number of participants at event (int)
        :param start_date: start date of the event (str)
        :param end_date: end date of the event (str)
        :return:
        """
        event = Event(id, name, city, number_of_participants, max_capacity, start_date, end_date)
        self.__repository.add(event)

    # Organizer option-2
    def delete_event(self, id):
        """
        Removes an event from the list if it exists
        :param id: id of the event to be removes (str)
        :return:
        """
        event = Event(id, "", "", "", "", "", "")
        self.__repository.delete(event)

    # Organizer option-3
    def update_event(self, old_id, name, city, number_of_participants, max_capacity, start_date, end_date):
        """
        Updates an event from the list with new details if it exists
        :param old_id: the id of the event you want to update (str)
        :param name: new name of the event (str)
        :param city: new city of the event (str)
        :param number_of_participants:  new number of participants at the event (int)
        :param max_capacity: new maximum number of participants at the event (int)
        :param start_date: new start date of event (str)
        :param end_date: new end date of event (str)
        :return:
        """
        old_event = Event(old_id, "", "", "", "", "", "")
        new_event = Event(old_id, name, city, number_of_participants, max_capacity, start_date, end_date)
        self.__repository.update(old_event, new_event)

    # Organizer option-4 / Participant option-1
    def get_all_events(self):
        """
        Returns a list of all the events
        :return: list of all events (list)
        """
        return self.__repository.get_all()

    # Organizer option-5
    def events_in_city(self, city):
        """
        Return a list of all the events that take place in a certain city if there are any
        :param city: the city where events take place (str)
        :return: list of all the events that take place in a certain city (list)
        """
        events_in_city = []
        list_of_events = self.__repository.get_all()

        for event in list_of_events:
            if event.get_city() == city:
                events_in_city.append(event)

        return events_in_city

    # Organizer option-7
    def events_with_participants(self):
        """
        Returns a descended sorted by number of participants list of all the events that have any participants
        :return: descended sorted by number of participants list of all the events that have any participants (list)
        """
        list_of_events = self.__repository.get_all()
        events_with_participants = []

        for event in list_of_events:
            if event.get_number_of_participants():
                events_with_participants.append(event)

        events_with_participants.sort(key=lambda x: x.get_number_of_participants(), reverse=True)
        return events_with_participants

    # Participant option-3
    def events_next_week(self):
        """
        Return an ascended sorted by max capacity list of all events that take place the next 7 days if there are any
        :return: ascended sorted by max capacity list of all events that take place the next 7 days (list)
        """
        list_of_events = self.__repository.get_all()
        events_next_week = []

        for event in list_of_events:
            if datetime.strptime(event.get_start_date(), "%d/%m/%Y").date() >= datetime.today().date() \
                    and datetime.strptime(event.get_start_date(), "%d/%m/%Y").date() <= \
                    (datetime.today() + timedelta(days=7)).date():
                events_next_week.append(event)

        events_next_week.sort(key=lambda x: x.get_max_capacity())
        return events_next_week

    # Participant option-4
    def events_in_month(self, month):
        """
        Returns a descended sorted by duration list of all the events that take place in a certain month if there are any
        :param month: month in which events take place (str)
        :return: descended sorted by duration list of all the events that take place in a certain month (list)
        """
        list_of_events = self.__repository.get_all()
        events_in_month = []

        try:
            int(month)
            month = int(month)
        except:
            month = datetime.strptime(month, '%B').month

        for event in list_of_events:
            if datetime.strptime(event.get_start_date(), "%d/%m/%Y").month == month:
                events_in_month.append(event)

        events_in_month.sort(
            key=lambda x: datetime.strptime(x.get_end_date(), "%d/%m/%Y")
                          - datetime.strptime(x.get_start_date(), "%d/%m/%Y"), reverse=True)

        return events_in_month
