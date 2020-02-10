class DailyActivityLog:
    id = None
    person_id = None
    date = None
    water_intake_oz = None
    did_use_face_mask = False
    did_exfoliate = False

    def __init__(self, id, person_id, date, water_intake_oz, did_use_face_mask, did_exfoliate):
        self.id = id
        self.person_id = person_id
        self.date = date
        self.water_intake_oz = water_intake_oz
        self.did_use_face_mask = did_use_face_mask
        self.did_exfoliate = did_exfoliate
    