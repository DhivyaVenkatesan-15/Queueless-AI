
from ml_prediction import (
    predict_waiting_time,
    get_prediction_details
)


def get_prediction(people_ahead, service_time=5, counters=2,
                   service="General Enquiry"):

    return predict_waiting_time(
        people_ahead,
        service_time,
        counters,
        service
    )
