from domain.event import Event
from repository.repository import Repository

from datetime import timedelta, datetime

import qrcode
import os
from matplotlib import pyplot as plt
from matplotlib import image as mpimg


class EventOrganizerService:
    def __init__(self, repository: Repository):
        """
        Constructor for EventOrganizerService class:
        :param repository: event organizer repository (Repository)
        """
        self.__repository = repository

    # qr_codes
    def generate_qr_code(self, name, website_link):
        """
        Generates a png image of a qr code of an event's website link
        :param name: name of the event (str)
        :param website_link: website link of event (str)
        :return:
        """
        image = qrcode.make(website_link)
        image.save(f'qr_codes/{name}.png')

    def __delete_qr_code(self, name):
        """
        Deletes a png image of a qr code of an event's website link
        :param name: name of the event (str)
        :return:
        """
        os.remove(f'qr_codes/{name}.png')

    def __update_qr_code(self, old_name, new_name, new_website_link):
        """
        Updates a png image of a qr code of an event's website link by deleting the old one and adding a new one
        :param old_name: name of the old event (str)
        :param new_name: name of the new event (str)
        :param new_website_link: new website link of event (str)
        :return:
        """
        os.remove(f'qr_codes/{old_name}.png')
        image = qrcode.make(new_website_link)
        image.save(f'qr_codes/{new_name}.png')

    def show_qr_code(self, name):
        """
        Displays the png image of a qr code of an event's website link by opening Matplotlib graphical format
        :param name: name of the event
        :return:
        """
        plt.title(f'{name}')
        image = mpimg.imread(f'qr_codes/{name}.png')
        plt.imshow(image)
        plt.show()

    # Organizer option-1
    def add_event(self, id, name, city, number_of_participants, max_capacity, start_date, end_date, website_link):
        """
        Adds an event to the list of events if it does not exist already and
        add sits website's qr code to the qr_codes folder
        :param id: id of the event (str)
        :param name: name of event (str)
        :param city: city where event takes place (str)
        :param number_of_participants: number of participants at event (int)
        :param max_capacity: maximum number of participants at event (int)
        :param start_date: start date of the event (str)
        :param end_date: end date of the event (str)
        :param website_link: website link of the event (Str)
        :return:
        """
        event = Event(id, name, city, number_of_participants, max_capacity, start_date, end_date, website_link)
        self.__repository.add(event)
        self.generate_qr_code(name, website_link)

    # Organizer option-2
    def __find_event_by_id(self, id):
        """
        Return an event found by id
        :param id: id to search by (str)
        :return: an event (Event) if it was found, None otherwise
        """
        list_of_events = self.__repository.get_all()
        for event in list_of_events:
            if event.get_id() == id:
                return event
        return None

    def delete_event(self, id):
        """
        Removes an event from the list and its website's qr code if it exists
        :param id: id of the event to be removes (str)
        :return:
        """
        event = self.__find_event_by_id(id)

        if event is None:
            raise Exception("Event doesn't exist!")

        self.__repository.delete(event)
        self.__delete_qr_code(event.get_name())

    # Organizer option-3
    def update_event(self, old_id, name, city, number_of_participants, max_capacity, start_date, end_date,
                     website_link):
        """
        Updates an event from the list with new details if it exists
        :param old_id: the id of the event you want to update (str)
        :param name: new name of the event (str)
        :param city: new city of the event (str)
        :param number_of_participants:  new number of participants at the event (int)
        :param max_capacity: new maximum number of participants at the event (int)
        :param start_date: new start date of event (str)
        :param end_date: new end date of event (str)
        :param website_link: new website link of event (str)
        :return:
        """
        old_event = self.__find_event_by_id(old_id)

        if old_event is None:
            raise Exception("Event doesn't exist!")

        new_event = Event(old_id, name, city, number_of_participants, max_capacity, start_date, end_date, website_link)

        self.__repository.update(old_event, new_event)
        self.__update_qr_code(old_event.get_name(), name, website_link)

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
