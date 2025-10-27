class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor does not have a vaccine record."""
    def __init__(self, message="Visitor is not vaccinated."):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is outdated."""
    def __init__(self, message="Vaccine is outdated."):
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    def __init__(self, message="Visitor is not wearing a mask."):
        super().__init__(message)


