
import sqlite3
from datetime import datetime

from sklearn.ensemble import RandomForestRegressor


DATABASE_NAME = "queue.db"


def get_service_code(service):
    services = {
        "General Enquiry": 1,
        "Account Service": 2,
        "Customer Support": 3,
        "Document Verification": 4
    }
    return services.get(service, 0)


def load_training_data():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT service, created_at, started_at, completed_at
        FROM tokens
        WHERE status = 'Completed'
          AND started_at IS NOT NULL
          AND completed_at IS NOT NULL
    """)

    records = cursor.fetchall()
    connection.close()

    features = []
    targets = []

    for service, created_at, started_at, completed_at in records:
        try:
            start = datetime.fromisoformat(started_at)
            end = datetime.fromisoformat(completed_at)
            created = datetime.fromisoformat(created_at)

            duration = (end - start).total_seconds() / 60

            if duration <= 0 or duration > 240:
                continue

            features.append([
                created.hour,
                get_service_code(service)
            ])
            targets.append(duration)

        except (ValueError, TypeError):
            continue

    return features, targets


def get_prediction_details(people_ahead, service_time=5, counters=2,
                           service="General Enquiry"):

    people_ahead = max(0, int(people_ahead))
    counters = max(1, int(counters))

    features, targets = load_training_data()

    if len(features) >= 5:
        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        model.fit(features, targets)

        predicted_service_time = float(
            model.predict([[
                datetime.now().hour,
                get_service_code(service)
            ]])[0]
        )

        model_name = "Random Forest ML"

    else:
        predicted_service_time = float(service_time)
        model_name = "Formula fallback (insufficient history)"

    predicted_service_time = max(1.0, predicted_service_time)

    waiting_minutes = (
        people_ahead * predicted_service_time
    ) / counters

    return {
        "waiting_minutes": round(waiting_minutes, 2),
        "predicted_service_time": round(predicted_service_time, 2),
        "model": model_name
    }


def predict_waiting_time(people_ahead, service_time=5, counters=2,
                         service="General Enquiry"):

    result = get_prediction_details(
        people_ahead,
        service_time,
        counters,
        service
    )

    return result["waiting_minutes"]
