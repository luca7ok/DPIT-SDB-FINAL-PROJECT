from service.event_organizer_service import EventOrganizerService
from service.participant_service import ParticipantService
from service.statistics_service import StatisticsService

from datetime import datetime

import os
import validators


class ConsoleUI:
    def __init__(self, event_organizer_service: EventOrganizerService, participant_service: ParticipantService,
                 statistics_service: StatisticsService):
        self.__event_organizer_service = event_organizer_service
        self.__participant_service = participant_service
        self.__statistics_service = statistics_service

    def __print_main_menu(self):
        print("Please select your role:\n"
              "1. Organizer\n"
              "2. Participant\n"
              "0. Exit")

    def __print_organizer_menu(self):
        print("ORGANIZER MODE\n"
              "Please select one of the options:\n"
              "1. Add an event to the list\n"
              "2. Delete an event from the list\n"
              "3. Update an event from the list\n"
              "4. View all event\n"
              "5. View events from a certain city\n"
              "6. View participants from an event\n"
              "7. View events sorted descended by their number of participants if they have any\n"
              "0. Back to main menu")

    def __print_participant_menu(self):
        print("PARTICIPANT MODE\n"
              "Please select one of the options:\n"
              "1. View all events\n"
              "2. Sign up for an event\n"
              "3. View events that start in the next 7 days, sorted ascended by their maximum number of participants\n"
              "4. View events that start in a certain month, sorted descended by their duration\n"
              "5. View all participants\n"
              "0. Back to main menu")

    def __valid_number_of_participants(self, number_of_participants: str):
        try:
            int(number_of_participants)
        except Exception:
            raise ValueError("\nNumber of participants is not a number!\n")

    def __valid_max_capacity(self, max_capacity: str):
        try:
            int(max_capacity)
        except Exception:
            raise ValueError("\nMaximum capacity is not a number!\n")

    def __valid_start_date(self, start_date: str):
        date_format = '%d/%m/%Y'
        try:
            datetime.strptime(start_date, date_format).date()
        except Exception:
            raise ValueError("\nStart date is not a valid date!\n")

    def __valid_end_date(self, end_date: str):
        date_format = '%d/%m/%Y'
        try:
            datetime.strptime(end_date, date_format).date()
        except Exception:
            raise ValueError("\nEnd date is not a valid date!\n")

    def __valid_website_link(self, website_link: str):
        if not website_link.startswith('https://'):
            website_link = f'https://{website_link}'

        valid = validators.url(website_link)
        if not valid:
            raise Exception("\nWebsite link is not valid!\n")

    # Organizer option-1
    def __add_event(self):
        print("Please add the details of the event you want to add to the list: ")

        id = input("ID: ")
        name = input("Name: ")
        city = input("City: ")
        number_of_participants = input("Number of participants: ")
        max_capacity = input("Max capacity: ")
        start_date = input("Start date: ")
        end_date = input("End date: ")
        website_link = input("Website link: ")

        self.__valid_number_of_participants(number_of_participants)
        self.__valid_max_capacity(max_capacity)
        self.__valid_start_date(start_date)
        self.__valid_end_date(end_date)
        self.__valid_website_link(website_link)

        self.__event_organizer_service.add_event(id, name, city, number_of_participants, max_capacity, start_date,
                                                 end_date, website_link)

    # Organizer option-2
    def __delete_event(self):
        id = input("ID of event to delete: ")
        self.__event_organizer_service.delete_event(id)

    # Organizer option-3
    def __update_event(self):
        old_id = input("ID of event you want to update: ")
        name = input("Event changes\nName: ")
        city = input("City: ")
        number_of_participants = input("Number of participants: ")
        max_capacity = input("Max capacity: ")
        start_date = input("Start date: ")
        end_date = input("End date: ")
        website_link = input("Website link: ")

        self.__valid_number_of_participants(number_of_participants)
        self.__valid_max_capacity(max_capacity)
        self.__valid_start_date(start_date)
        self.__valid_end_date(end_date)
        self.__valid_website_link(website_link)

        self.__event_organizer_service.update_event(old_id, name, city, number_of_participants, max_capacity,
                                                    start_date, end_date, website_link)

    # Organizer option-4 / Participant option-1
    def __show_all_events(self):
        print()
        list_of_events = self.__event_organizer_service.get_all_events()

        if not len(list_of_events):
            raise Exception("There are no events!")

        for event in list_of_events:
            print(event)
            self.__event_organizer_service.show_qr_code(event.get_name())

    # Organizer option-5
    def __show_events_from_city(self):
        city = input("City in which events take place: ")
        print()
        events_in_city = self.__event_organizer_service.events_in_city(city)

        if not len(events_in_city):
            raise Exception(f"There are no events in the city {city}!")

        for event in events_in_city:
            print(event)

    # Organizer option-6
    def __show_participants_from_event(self):
        id = input("Event ID: ")
        print()
        participants_from_event = self.__participant_service.participants_to_event(id)

        if not len(participants_from_event):
            raise Exception("There are no participants at this event!")

        for participant in participants_from_event:
            print(participant)

    # Organizer option-7
    def __show_events_with_participants(self):
        print()
        events_with_participants = self.__event_organizer_service.events_with_participants()

        if not len(events_with_participants):
            raise Exception("The events have no participants or there are no events!")

        for event in events_with_participants:
            print(event)

    # Participant-2
    def __sign_up_participant(self):
        id = input("ID of the event you want to sign up for: ")
        name = input("Participant's name: ")
        picture_link = input("Participant's picture: ")

        self.__statistics_service.sign_up_participant(id, name, picture_link)

    # Participant option-3
    def __show_events_next_week(self):
        print()
        events_next_week = self.__event_organizer_service.events_next_week()

        if not len(events_next_week):
            raise Exception("There are no events this week or there are no events!")

        for event in events_next_week:
            print(event)

    # Participant option-4
    def __show_events_in_month(self):
        month = input("Month in which events start: ")

        print()
        events_in_month = self.__event_organizer_service.events_in_month(month)

        if not len(events_in_month):
            raise Exception(f"There are no events in that month or there are no events")

        for event in events_in_month:
            print(event, end='')
            print("Duration:", datetime.strptime(event.get_end_date(), "%d/%m/%Y")
                            - datetime.strptime(event.get_start_date(), "%d/%m/%Y"), '\n')

    # Participant option-5
    def __show_all_participants(self):
        print()
        list_of_participants = self.__participant_service.get_all_participants()
        if not len(list_of_participants):
            raise Exception("There are no participants!")

        for participant in list_of_participants:
            print(participant)

    # qr codes
    def __delete_all_qr_codes(self):
        for file in os.listdir('qr_codes'):
            os.remove(os.path.join('qr_codes', file))

    def __initial_qr_codes(self):
        event_list = self.__event_organizer_service.get_all_events()
        for event in event_list:
            self.__event_organizer_service.generate_qr_code(event.get_name(), event.get_website_link())

    def run(self):
        self.__delete_all_qr_codes()
        self.__initial_qr_codes()

        while True:
            self.__print_main_menu()
            try:
                command = int(input("Choose your role: ").strip())
                if command == 0:
                    break
                elif command == 1:
                    os.system('cls')
                    while True:
                        self.__print_organizer_menu()
                        try:
                            command = int(input("Choose an option: ").strip())
                            if command == 0:
                                os.system('cls')
                                break
                            elif command == 1:
                                self.__add_event()
                            elif command == 2:
                                self.__delete_event()
                            elif command == 3:
                                self.__update_event()
                            elif command == 4:
                                self.__show_all_events()
                            elif command == 5:
                                self.__show_events_from_city()
                            elif command == 6:
                                self.__show_participants_from_event()
                            elif command == 7:
                                self.__show_events_with_participants()
                        except Exception as error:
                            print(error)

                elif command == 2:
                    os.system('cls')
                    while True:
                        self.__print_participant_menu()
                        try:
                            command = int(input("Choose an option: ").strip())
                            if command == 0:
                                os.system('cls')
                                break
                            elif command == 1:
                                self.__show_all_events()
                            elif command == 2:
                                self.__sign_up_participant()
                            elif command == 3:
                                self.__show_events_next_week()
                            elif command == 4:
                                self.__show_events_in_month()
                            elif command == 5:
                                self.__show_all_participants()
                        except Exception as error:
                            print(error)

            except Exception as error:
                print(error)
