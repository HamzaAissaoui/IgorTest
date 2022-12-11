import enum

class Category(enum.Enum):

    ALL_STUDENTS = "All Students"
    ATTEND_SCHOOL_OUTSIDE_DISCRICT_OF_RESIDENCE = "Attend school outside district of residence"
    ENGLISH_LANGUAGE_LEARNERS = "English Language Learners"
    POVERTY = "Poverty"
    RESIDE_IN_TEMPORARY_HOUSING = "Reside in temporary housing"
    STUDENTS_WITH_DISABILITIES = "Students with Disabilities"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
