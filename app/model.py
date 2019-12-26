import random
from typing import Dict, Any


class Model:
    def __init__(self):
        pass

    def predict(self, dd: Dict[str, Any]):
        score = 0

        # dd = {'document': {'issue_date': '2014-01-22',
        #                     'issue_unit': 'МВД РК',
        #                     'number': '21482148',
        #                     'series': '4821',
        #                     'type': 'passport_inter',
        #                     'unit_code': '1234'},
        #         'info': {'city_fact': '623',
        #                 'city_options': None,
        #                 'city_reg': None,
        #                 'city_reg_check': True,
        #                 'city_work': None,
        #                 'city_work_fact_check': True,
        #                 'city_work_reg_check': True,
        #                 'cnt_children': '2',
        #                 'cnt_fam_members': '8',
        #                 'cred_sum': '200600',
        #                 'cred_type': 'cred_nal',
        #                 'credit_date': '2019-12-26',
        #                 'credit_purpose': 'Everyday expenses',
        #                 'edu_type': 'Higher education',
        #                 'email': '23423@',
        #                 'flag_own_car': True,
        #                 'flag_own_realty': True,
        #                 'goods_sum': '',
        #                 'home_phone': '4837598273',
        #                 'main_income': '100500',
        #                 'mobile': '81234567890',
        #                 'mobile_check': True,
        #                 'name_family_status': 'married',
        #                 'name_housing_type': 'house_apartment',
        #                 'obl_fact': 'moscow',
        #                 'obl_options': None,
        #                 'obl_reg': None,
        #                 'obl_reg_check': True,
        #                 'obl_work': None,
        #                 'obl_work_fact_check': True,
        #                 'obl_work_reg_check': True,
        #                 'organization_type': 'type 2',
        #                 'own_car_age': '10',
        #                 'own_forepass': True,
        #                 'own_inn': True,
        #                 'own_ndfl': True,
        #                 'own_prev_app': False,
        #                 'own_snils': True,
        #                 'position_cat': 'IT staff',
        #                 'second_income': '500',
        #                 'test': None,
        #                 'work_exp': '4',
        #                 'work_phone': '9871237821',
        #                 'work_status': 'Working'},
        #         'user': {'address': 'г.Москва, пр-кт 60-летия Октября, д.11, кв.1616',
        #                 'birthdate': '1996-01-22',
        #                 'citizenship': 'Казахстан',
        #                 'gender': 'male',
        #                 'name': 'Никита',
        #                 'patronymic': 'Юрьевич',
        #                 'surname': 'Туркин'},
        #         'user_hash': 'c659fe96d0bdd814eec1ecd28cab6c6db617d85e682f5a2542b5d8811e35c28f'}
        if dd['info']['flag_own_car']:
            score += 0.1
        if dd['info']['flag_own_realty']:
            score += 0.1
        if dd['info']['work_status'] == 'contract':
            score += 0.1
        if int(dd['info']['work_exp']) >= 24:
            score += 0.1
        if dd['info']['edu_type'] in {'Higher education', 'Academic degree'}:
            score += 0.1
        if not dd['info']['own_prev_app']:
            score += 0.1
        if dd['info']['cred_type'] != 'cred_vozob':
            score += 0.1
        if float(dd['info']['main_income']) > 75000:
            score += 0.1
        if dd['document']['type'] == 'passport_rf':
            score += 0.1
        if dd['info']['name_family_status'] != 'Married':
            score += 0.1

        if score >= 0.5:
            new_score = random.uniform(score, 1)
        else:
            new_score = random.uniform(0, score)
        return new_score


MODEL = Model()
