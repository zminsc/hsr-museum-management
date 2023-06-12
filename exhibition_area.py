from typing import List

import numpy as np
from assistant import Assistant


class ExhibitionArea:
    def __init__(
        self,
        name: str,
        req_tour_duration: np.int32,
        req_educational_value: np.int32,
        req_visitor_appeal: np.int32,
        base_tour_duration: np.int32,
        base_educational_value: np.int32,
        base_visitor_appeal: np.int32,
        tour_duration_mul: np.float64 = 1.0,
        educationa_value_mul: np.float64 = 1.0,
        visitor_appeal_mul: np.float64 = 1.0,
    ) -> None:
        self.name = name
        self.req_tour_duration = req_tour_duration
        self.req_educational_value = req_educational_value
        self.req_visitor_appeal = req_visitor_appeal
        self.base_tour_duration = base_tour_duration
        self.base_educational_value = base_educational_value
        self.base_visitor_appeal = base_visitor_appeal
        self.tour_duration_mul = tour_duration_mul
        self.education_value_mul = educationa_value_mul
        self.visitor_appeal_mul = visitor_appeal_mul

    def calc_loss(self, assistants: List[Assistant]) -> np.int32:
        tour_duration = (
            np.sum([assistant.tour_duration for assistant in assistants])
            + np.floor(self.base_tour_duration * self.tour_duration_mul)
        )
        educational_value = (
            np.sum([assistant.educational_value for assistant in assistants])
            + np.floor(self.base_educational_value * self.education_value_mul)
        )
        visitor_appeal = (
            np.sum([assistant.visitor_appeal for assistant in assistants])
            + np.floor(self.base_visitor_appeal * self.visitor_appeal_mul)
        )

        tour_duration_loss = max(self.req_tour_duration - tour_duration, 0)
        educational_value_loss = max(self.req_educational_value - educational_value, 0)
        visitor_appeal_loss = max(self.req_visitor_appeal - visitor_appeal, 0)

        return tour_duration_loss + educational_value_loss + visitor_appeal_loss
