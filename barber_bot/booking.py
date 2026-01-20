from datetime import datetime, timedelta
from sheets import get_records

WORK_START = 10
WORK_END = 22

def get_free_slots(barber, date_str, service_duration):
    records = get_records()

    busy = []
    for r in records:
        if r["Барбер"] == barber and r["Дата"] == date_str:
            start = datetime.strptime(r["Время"], "%H:%M")
            dur = int(r["Длительность_мин"])
            busy.append((start, start + timedelta(minutes=dur)))

    free = []
    day = datetime.strptime(date_str, "%d.%m.%Y")
    current = day.replace(hour=WORK_START, minute=0)

    end_day = day.replace(hour=WORK_END, minute=0)

    while current + timedelta(minutes=service_duration) <= end_day:
        slot_end = current + timedelta(minutes=service_duration)

        overlap = any(
            current < b_end and slot_end > b_start
            for b_start, b_end in busy
        )

        if not overlap:
            free.append(current.strptime("%H:%M"))

        current += timedelta(minutes=30)

    return free