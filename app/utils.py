from datetime import datetime

def datetime_delta_from_now_in_days(string):
    date = tuple(map(int, string.split('-')))
    return datetime.now() - datetime(*date)

def convert_string_to_01(string):
    if len(string) > 0:
        return 1
    return 0

# cols = [
# 'OWN_CAR_AGE',
# 'CNT_CHILDREN',
# 'CNT_FAM_MEMBERS',
# 'AMT_INCOME_TOTAL',
# 'AMT_CREDIT',
# 'AMT_GOODS_PRICE',
# 'DAYS_BIRTH',
# 'DAYS_EMPLOYED',
# 'DAYS_ID_PUBLISH',
# 'NAME_CONTRACT_TYPE',
# 'CODE_GENDER',
# 'FLAG_OWN_CAR',
# 'FLAG_OWN_REALTY',
# 'NAME_INCOME_TYPE',
# 'NAME_EDUCATION_TYPE',
# 'NAME_FAMILY_STATUS',
# 'NAME_HOUSING_TYPE',
# 'FLAG_MOBIL',
# 'FLAG_WORK_PHONE',
# 'FLAG_CONT_MOBILE',
# 'FLAG_PHONE',
# 'FLAG_EMAIL',
# 'OCCUPATION_TYPE',
# 'WEEKDAY_APPR_PROCESS_START',
# 'REG_REGION_NOT_LIVE_REGION',
# 'REG_REGION_NOT_WORK_REGION',
# 'LIVE_REGION_NOT_WORK_REGION',
# 'REG_CITY_NOT_LIVE_CITY',
# 'REG_CITY_NOT_WORK_CITY',
# 'LIVE_CITY_NOT_WORK_CITY',
# 'FLAG_DOCUMENT_2',
# 'FLAG_DOCUMENT_3',
# 'FLAG_DOCUMENT_4',
# 'FLAG_DOCUMENT_5',
# 'NAME_CASH_LOAN_PURPOSE',
# 'CREDIT_ACTIVE',
# ]