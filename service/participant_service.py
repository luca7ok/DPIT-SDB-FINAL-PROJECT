from repository.repository import Repository


class ParticipantService:
    def __init__(self, repository: Repository):
        """
        Constructor for ParticipantService class
        :param repository: participant repository (Repository)
        """
        self.__repository = repository

    # Organizer option-6
    def __verify_participant_to_event(self, participant, id):
        """
        Verifies if a participants goes to a certain event
        :param participant: participant to check (Participant)
        :param id: id of the event to check (str)
        :return: True if the participant goes to the event, False otherwise
        """
        events_participant_attends = participant.get_list_of_events()

        if not len(events_participant_attends):
            raise Exception("Participant doesn't go to any event!")

        for event_id in events_participant_attends:
            if event_id == id:
                return True

        return False

    def participants_to_event(self, id):
        """
        Return a list of all the participants that attend a certain event
        :param id: id of event to check (str)
        :return: list of mall the participants that attend the event (list)
        """
        list_of_participants = self.__repository.get_all()
        participants_to_event = []

        for participant in list_of_participants:
            if self.__verify_participant_to_event(participant, id):
                participants_to_event.append(participant)

        return participants_to_event

    # Participant option-5
    def get_all_participants(self):
        """
        Returns a list of all the participants
        :return: list of all the participants (list)
        """
        return self.__repository.get_all()
