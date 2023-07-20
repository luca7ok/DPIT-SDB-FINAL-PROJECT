from repository.repository import Repository
from domain.participant import Participant


class StatisticsService:
    def __init__(self, participant_repository: Repository, event_organizer_repository: Repository):
        """
        Constructor for StatisticsService class
        :param participant_repository: participant repository (Repository)
        :param event_organizer_repository: event organizer repository (Repository)
        """
        self.__participant_repository = participant_repository
        self.__event_organizer_repository = event_organizer_repository

    # Participant option-2

    def __verify_participant_event(self, participant, id):
        """
        Verifies if the participant goes to a certain event
        :param participant: participant to check (Participant)
        :param id: id of the event to check (str)
        :return:
        """
        events_participant_attends = participant.get_list_of_events()
        for event_attended in events_participant_attends:
            if event_attended == id:
                raise Exception("Participant already goes to this event!")

    def sign_up_participant(self, id, name, picture_link):
        """
        Will sign up a participant to an event and increase the event's number of participants, if the event exists or if
        it hasn't reached maximum capacity.
        If the participant is already signed for other events then it will just add the event's id to the participant's
        list of events he attends, if he doesn't already attend this event, otherwise a new participant will be created
        and added to the list of participants

        :param id: id of the event to sign up for (str)
        :param name: name of the participant (str)
        :param picture_link: picture link of the participant (str)
        :return:
        """
        list_of_events = self.__event_organizer_repository.get_all()
        list_of_participants = self.__participant_repository.get_all()

        new_participant = Participant(name, picture_link, [])

        valid_event = False
        for event in list_of_events:
            if event.get_id() == id:
                valid_event = True
                if event.get_number_of_participants() + 1 <= event.get_max_capacity():
                    event.set_number_of_participants(event.get_number_of_participants() + 1)

                    valid_participant = False
                    for participant in list_of_participants:
                        if participant == new_participant:
                            self.__verify_participant_event(participant, id)

                            participant.append_list_of_events(event.get_id())
                            valid_participant = True

                    if not valid_participant:
                        self.__participant_repository.add(Participant(name, picture_link, [id]))
                else:
                    raise Exception("The event has reached its maximum capacity!")
        if not valid_event:
            raise Exception("The event doesn't exist!")
