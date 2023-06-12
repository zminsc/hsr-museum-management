import numpy as np


class Assistant:
    def __init__(
        self,
        name: str,
        tour_duration: np.int32,
        educational_value: np.int32,
        visitor_appeal: np.int32,
    ) -> None:
        self.name = name
        self.tour_duration = tour_duration
        self.educational_value = educational_value
        self.visitor_appeal = visitor_appeal
