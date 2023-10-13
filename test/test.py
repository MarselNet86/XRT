import datetime

lines = [{'CRM': 'CRM-3ыsыs14868505', 'CITY': 'Нефтеюганск', 'WORKSITE_SHORT_NAME': 'ХТ_sИычыыНСТ. + 3 ЛТsыП_Нефтеюганск', 'ASSIGNEE_NAME': 'Бабаев Э.А.', 'OPEN_DATE': datetime.datetime(2023, 7, 26, 9, 9, 35), 'CREATE_KI': datetime.datetime(2023, 7, 26, 9, 9, 36), 'START_KI': datetime.datetime(2023, 7, 26, 19, 0), 'STOP_KI': datetime.datetime(2023, 7, 26, 21, 0), 'CLOSE_KI': None, 'KS_3': datetime.datetime(2023, 7, 27, 5, 9, 36), 'KS_23': datetime.datetime(2023, 7, 27, 9, 9, 35), 'COMMENTARY': None, 'LOGIN': 'HM_BABAEV-EA_', 'DATE_CLOSE': datetime.datetime(2018, 7, 30, 19, 0), 'INTERVAL': '2023-07-26 19:00:00-21:00:00', 'STATUS': 1, 'MESSAGE_TYPE': 'request_change'}]
rows = [{'email': None, 'fk_user_id': 1455408286, 'bot_all': False, 'bot_new_request': True, 'bot_request_change': False, 'bot_change_interval': False, 'email_all': False, 'email_new_request': False, 'email_request_change': True, 'email_change_interval': False}, {'email': 'n-i-2017@mail.ru', 'fk_user_id': 762832075, 'bot_all': False, 'bot_new_request': False, 'bot_request_change': False, 'bot_change_interval': False, 'email_all': False, 'email_new_request': False, 'email_request_change': True, 'email_change_interval': True}]

user_notices = []
for row in rows:
    user_notices.clear()
    user_notices.extend([row['email'], row['fk_user_id']])
    for key, value in row.items():
        if value is True:
            user_notices.extend([key.replace('bot_', '').replace('email_', '')])

    for line in lines:
        if line['MESSAGE_TYPE'] in user_notices:
            print('вах новый смска', user_notices[:2])
            if user_notices[0] is not None:
                print('НА почта тоже отправить', user_notices[:2])

