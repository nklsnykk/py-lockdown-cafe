import datetime
from .errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get('name', 'Unknown')} is not vaccinated.")

        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f"{visitor.get('name', 'Unknown')}'s vaccine is outdated.")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f"{visitor.get('name', 'Unknown')} is not wearing a mask.")

        return f"Welcome to {self.name}"
