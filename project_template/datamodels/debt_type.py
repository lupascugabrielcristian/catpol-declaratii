from enum import Enum


class DebtType(Enum):
    DEBIT = "DEBIT"
    MORTGAGE = "IPOTECA"
    ISSUED_GARANTIES = "GARANTII EMISE"
    LEASING_ACQUIRED_GOODS = "BUNURI ACHIZIONATE LEASING"
