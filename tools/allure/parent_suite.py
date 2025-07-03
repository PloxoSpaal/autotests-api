from enum import Enum


class AllureParentSuite(str, Enum):
    LMS = "LMS service"
    STUDENT = "Student service"
    ADMINISTRATION = "Administration service"