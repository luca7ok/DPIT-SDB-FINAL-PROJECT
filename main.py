from domain.event import Event
from domain.participant import Participant

from service.event_organizer_service import EventOrganizerService
from service.participant_service import ParticipantService
from service.statistics_service import StatisticsService

from repository.repository import Repository

from ui.console import ConsoleUI

from datetime import timedelta, datetime

event_repository = Repository(
    [Event("#321", "Untold", "Cluj-Napoca", 2, 5, "03/08/2023", "06/08/2023", "https://untold.com/"),
     Event("#123", "Electric Castle", "Cluj-Napoca", 1, 4,
           (datetime.today() + timedelta(days=3)).strftime("%d/%m/%Y"),
           (datetime.today() + timedelta(days=10)).strftime("%d/%m/%Y"), "https://electriccastle.ro/"),

     Event("#000", "Oktoberfest", "Munich", 0, 5,
           datetime.today().strftime("%d/%m/%Y"),
           (datetime.today() + timedelta(days=8)).strftime("%d/%m/%Y"), "https://www.oktoberfest.de/en")])

participant_repository = Repository(
    [Participant("Luca", "prnt.sc/5152", ["#321", "#123"]), Participant("Tudor", "prnt.sc/123", ["#321"])])

event_organizer_service = EventOrganizerService(event_repository)
participant_service = ParticipantService(participant_repository)
statistics_service = StatisticsService(participant_repository, event_repository)

ui = ConsoleUI(event_organizer_service, participant_service, statistics_service)

ui.run()
