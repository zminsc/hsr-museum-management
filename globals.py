from exhibition_area import ExhibitionArea
from assistant import Assistant


assistants = [
    Assistant("Serval", 68, 57, 10),
    Assistant("Peak", 44, 54, 10),
    Assistant("Rossy", 54, 54, 0),
    Assistant("Cunning Child", 8, 58, 42),
    Assistant("Julian", 52, 20, 36),
    Assistant("Gilbert", 36, 40, 20),
    Assistant("Lila", 52, 14, 30),
    Assistant("Fersman", 50, 29, 17),
    Assistant("Pela", 30, 30, 30),
    Assistant("Amo", 40, 8, 30),
    Assistant("Elaine", 26, 26, 26),
    Assistant("Serval's Fanatic Fan", 20, 44, 14),
    Assistant("Clara", 15, 75, 78),
    Assistant("Perkins", 42, 22, 65),
    Assistant("Natasha", 56, 15, 64),
    Assistant("Gertie", 10, 66, 50),
    Assistant("Fidora", 63, 0, 63),
    Assistant("Hook", 80, 0, 76),
    Assistant("Manya", 66, 60, 15),
    Assistant("Eric", 78, 9, 39),
    Assistant("Wallace", 56, 72, 40),
    Assistant("Bronya", 48, 23, 85),
    Assistant("Nika", 64, 80, 18),
    Assistant("Findie", 10, 58, 73),
    Assistant("Alina", 54, 16, 71),
    Assistant("Gepard", 5, 80, 83),
    Assistant("Eunice", 94, 86, 0),
    Assistant("Old Goethe", 12, 62, 88),
    Assistant("Dunn", 64, 20, 78),
    Assistant("Mr. Cold Feet", 93, 93, 0),
    Assistant("Seele", 88, 72, 26),
    Assistant("Oleg", 18, 80, 82),
    Assistant("Svarog", 60, 32, 88),
]


exhibition_areas = [
    ExhibitionArea(
        name="General Hall - Exterior",
        req_tour_duration=375,
        req_educational_value=295,
        req_visitor_appeal=460,
        base_tour_duration=220,
        base_educational_value=220,
        base_visitor_appeal=220,
    ),
    ExhibitionArea(
        name="General Hall - Interior",
        req_tour_duration=460,
        req_educational_value=380,
        req_visitor_appeal=280,
        base_tour_duration=220,
        base_educational_value=220,
        base_visitor_appeal=220,
    ),
    ExhibitionArea(
        name="Industrial Hall",
        req_tour_duration=280,
        req_educational_value=437,
        req_visitor_appeal=400,
        base_tour_duration=210,
        base_educational_value=210,
        base_visitor_appeal=210,
    ),
    ExhibitionArea(
        name="History-Culture Hall",
        req_tour_duration=385,
        req_educational_value=385,
        req_visitor_appeal=365,
        base_tour_duration=240,
        base_educational_value=240,
        base_visitor_appeal=240,
        tour_duration_mul=1.05,
        educationa_value_mul=1.05,
        visitor_appeal_mul=1.05,
    ),
]
