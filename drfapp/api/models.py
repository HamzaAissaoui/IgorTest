from django.db import models
from . import enums

class Demography(models.Model):
    id = models.AutoField(primary_key=True)
    dbn = models.CharField(max_length=10)
    school_name = models.CharField(max_length=300)
    category = models.CharField(
        max_length=100,
        choices=enums.Category.choices,
        default=enums.Category.ALL_STUDENTS,
    )
    total_enrollment = models.IntegerField(max_length=6, null=True)

    grade_k = models.IntegerField(max_length=6)
    grade_1 = models.IntegerField(max_length=6)
    grade_2 = models.IntegerField(max_length=6)
    grade_3 = models.IntegerField(max_length=6)
    grade_4 = models.IntegerField(max_length=6)
    grade_5 = models.IntegerField(max_length=6)
    grade_6 = models.IntegerField(max_length=6)
    grade_7 = models.IntegerField(max_length=6)
    grade_8 = models.IntegerField(max_length=6)

    female_number = models.IntegerField(max_length=6)
    female_percentage = models.FloatField(max_length=16)

    male_number = models.IntegerField(max_length=6)
    male_percentage = models.FloatField(max_length=16)

    asian_number = models.IntegerField(max_length=6)
    asian_percentage = models.FloatField(max_length=16)
    
    black_number = models.IntegerField(max_length=6)
    black_percentage = models.FloatField(max_length=16)

    hispanic_number = models.IntegerField(max_length=6)
    hispanic_percentage = models.FloatField(max_length=16)

    other_number = models.IntegerField(max_length=6)
    other_percentage = models.FloatField(max_length=16)

    white_number = models.IntegerField(max_length=6)
    white_percentage = models.FloatField(max_length=16)

    """Ell tests"""
    ell_spanish_number = models.IntegerField(max_length=6)
    ell_spanish_percentage = models.FloatField(max_length=16)

    ell_chinese_number = models.IntegerField(max_length=6)
    ell_chinese_percentage = models.FloatField(max_length=16)

    ell_bengali_number = models.IntegerField(max_length=6)
    ell_bengali_percentage = models.FloatField(max_length=16)

    ell_arabic_number = models.IntegerField(max_length=6)
    ell_arabic_percentage = models.FloatField(max_length=16)

    ell_haitian_creole_number = models.IntegerField(max_length=6)
    ell_haitian_creole_percentage = models.FloatField(max_length=16)

    ell_french_number = models.IntegerField(max_length=6)
    ell_french_percentage = models.FloatField(max_length=16)

    ell_russian_number = models.IntegerField(max_length=6)
    ell_russian_percentage = models.FloatField(max_length=16)


    ell_korean_number = models.IntegerField(max_length=6)
    ell_korean_percentage = models.FloatField(max_length=16)

    ell_urdu_number = models.IntegerField(max_length=6)
    ell_urdu_percentage = models.FloatField(max_length=16)

    ell_other_number = models.IntegerField(max_length=6)
    ell_other_percentage = models.FloatField(max_length=16)

    """Ela test takers"""
    ela_test_takers_number = models.IntegerField(max_length=6)

    ela_level_1_number = models.IntegerField(max_length=6)
    ela_level_1_percentage = models.FloatField(max_length=16)

    ela_level_2_number = models.IntegerField(max_length=6)
    ela_level_2_percentage = models.FloatField(max_length=16)

    ela_level_3_number = models.IntegerField(max_length=6)
    ela_level_3_percentage = models.FloatField(max_length=16)

    ela_level_4_number = models.IntegerField(max_length=6)
    ela_level_4_percentage = models.FloatField(max_length=16)

    ela_level_3_4_number = models.IntegerField(max_length=6)
    ela_level_3_4_percentage = models.FloatField(max_length=16)


    """Math test takers"""
    math_test_takers_number = models.IntegerField(max_length=6)

    math_level_1_number = models.IntegerField(max_length=6)
    math_level_1_percentage = models.FloatField(max_length=16)

    math_level_2_number = models.IntegerField(max_length=6)
    math_level_2_percentage = models.FloatField(max_length=16)

    math_level_3_number = models.IntegerField(max_length=6)
    math_level_3_percentage = models.FloatField(max_length=16)

    math_level_4_number = models.IntegerField(max_length=6)
    math_level_4_percentage = models.FloatField(max_length=16)

    math_level_3_4_number = models.IntegerField(max_length=6)
    math_level_3_4_percentage = models.FloatField(max_length=16)

    def __str__(self):
       return self.id


class Chart(models.Model):
    """we get the chart image by its int ID"""
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
       return self.id