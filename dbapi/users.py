import pandas as pd
from dbapi.db_connection import conn
import datetime


def getOfflineUsers():
    sql_query = ' SELECT id, email, name, surname, lastname, phone, birthday, sector, role, place_of_work, work_position, country, region, city, online, forum_themes, photo, promo, source, accept_policy, subscribe, password, is_blocked, app_role, remember_token, deleted_at, created_at, updated_at, academic_degree, academic_degree_other, pay_order_id, pay_status, locale, is_vip ' +\
        "           FROM public.users                              " +\
        "           where deleted_at is null and online = 'false'; "

    return pd.read_sql(sql_query, conn)


def getTatarstanUsers(offset=0, limit=10):
    sql_query = ' SELECT id, email, name, surname, lastname, phone, birthday, sector, role, place_of_work, work_position, country, region, city, online, forum_themes, photo, promo, source, accept_policy, subscribe, password, is_blocked, app_role, remember_token, deleted_at, created_at, updated_at, academic_degree, academic_degree_other, pay_order_id, pay_status, locale, is_vip ' +\
        "            FROM public.users                           " +\
        "            where deleted_at is null and                " +\
        "                  online = 'true' and  (                " + \
        "                      city ilike '%Агрыз%'  or          " +\
        "                      city ilike '%Азнакаево%'       or " +\
        "                      city ilike '%Альметьевск%'     or " +\
        "                      city ilike '%Аксубаево%'       or " +\
        "                      city ilike '%Актаныш%'         or " +\
        "                      city ilike '%Алексеевское%'    or " +\
        "                      city ilike '%Апастово%'        or " +\
        "                      city ilike '%Матаки%'          or " +\
        "                      city ilike '%Арск%'            or " +\
        "                      city ilike '%Атня%'            or " +\
        "                      city ilike '%Бавлы%'           or " +\
        "                      city ilike '%Болгар%'          or " +\
        "                      city ilike '%Балтаси%'         or " +\
        "                      city ilike '%Бугульма%'        or " +\
        "                      city ilike '%Буинск%'          or " +\
        "                      city ilike '%Услон%'           or " +\
        "                      city ilike '%Высокая Гора%'    or " +\
        "                      city ilike '%Дрожжаное%'       or " +\
        "                      city ilike '%Елабуга%'         or " +\
        "                      city ilike '%Заинск%'          or " +\
        "                      city ilike '%Зеленодольск%'    or " +\
        "                      city ilike '%Дрожжаное%'       or " +\
        "                      city ilike '%Кайбицы%'         or " +\
        "                      city ilike '%Камское Устье%'   or " +\
        "                      city ilike '%Иннополис%'       or " +\
        "                      city ilike '%Казань%'          or " +\
        "                      city ilike '%Кукмор%'          or " +\
        "                      city ilike '%Лаишево%'         or " +\
        "                      city ilike '%Лениногорск%'     or " +\
        "                      city ilike '%Мамадыш%'         or " +\
        "                      city ilike '%Менделеевск%'     or " +\
        "                      city ilike '%Мензелинск%'      or " +\
        "                      city ilike '%Муслюмово%'       or " +\
        "                      city ilike '%челны%'           or " +\
        "                      city ilike '%Нижнекамск%'      or " +\
        "                      city ilike '%Новошешминск%'    or " +\
        "                      city ilike '%Чистополь%'       or " +\
        "                      city ilike '%Пестрецы%'        or " +\
        "                      city ilike '%Рыбная Слобода%'  or " +\
        "                      city ilike '%Богатые Сабы%'    or " +\
        "                      city ilike '%Сарманово%'       or " +\
        "                      city ilike '%Нурлат%'          or " +\
        "                      city ilike '%Тюлячи%'          or " +\
        "                      city ilike '%Черемшан%'        or " +\
        "                      city ilike '%Уруссу%'          or " +\
        "                      city ilike '%Тетюши%')            " +\
        f"        LIMIT {limit} OFFSET {offset}                  "

    return pd.read_sql(sql_query, conn)


def getCountrisStatistic():
    sql_query = " SELECT  country, COUNT(*) " +\
        "           FROM public.users       " +\
        "           GROUP BY country;       "
    return pd.read_sql(sql_query, conn)


def getTotalRegistrationCount(start_date, end_date):
    sql_query = "SELECT COUNT(*) AS regs, " +\
                "       sum(case when  online = 'true' then 1 else 0 end) as reg_online," +\
                "       sum(case when  online = 'false' then 1 else 0 end) as reg_offline," +\
                "       sum(case when  role = '2' then 1 else 0 end) as speaker," +\
                "       sum(case when  role = '2' AND state = 3 then 1 else 0 end) as accepted_speaker," +\
                "       sum(case when  role = '2' AND state = 3 AND online = 'true' then 1 else 0 end) AS accepted_speaker_online," +\
                "       sum(case when  role = '2' AND state = 3 AND online = 'false' then 1 else 0 end) AS accepted_speaker_offline" +\
                " FROM users left join speaker_user_reports on users.id = speaker_user_reports.user_id" +\
                " WHERE deleted_at IS null AND " +\
               f"       public.users.created_at > '{start_date} 00:00:01' AND " +\
               f"	    public.users.created_at <'{end_date} 23:59:59'" 

    return pd.read_sql(sql_query, conn)


def getRegisterationCount(start_date, end_date, page_num=0, limit=10):
    '''
        Возвращает статистику зарегистрированных по дням начиная со стартовой даты(start_date) до конечной(end_date)
    '''
    sql_query = "SELECT to_char(public.users.created_at, 'yyyy.mm.dd') as date, COUNT(*) AS regs, " +\
                "       sum(case when  online = 'true' then 1 else 0 end) as reg_online," +\
                "       sum(case when  online = 'false' then 1 else 0 end) as reg_offline," +\
                "       sum(case when  role = '2' then 1 else 0 end) as speaker," +\
                "       sum(case when  role = '2' AND state = 3 then 1 else 0 end) as accepted_speaker," +\
                "       sum(case when  role = '2' AND state = 3 AND online = 'true' then 1 else 0 end) AS accepted_speaker_online," +\
                "       sum(case when  role = '2' AND state = 3 AND online = 'false' then 1 else 0 end) AS accepted_speaker_offline" +\
                " FROM users left join speaker_user_reports on users.id = speaker_user_reports.user_id" +\
                " WHERE deleted_at IS null AND " +\
               f"       public.users.created_at > '{start_date} 00:00:01' AND " +\
               f"	    public.users.created_at <'{end_date} 23:59:59'" +\
                " GROUP BY 1" +\
                " ORDER BY 1 DESC                                                          " +\
               f" OFFSET {page_num * limit + 1}                                            " +\
               f" LIMIT {limit}                                                            "

    print(sql_query)
    return pd.read_sql(sql_query, conn)


def getLocationStatistic(start_date, end_date):
    tatarstan = " (city ilike '%Агрыз%'  " +\
                " or city ilike '%Азнакаево%' " +\
                " or city ilike '%Альметьевск%' " +\
                " or city ilike '%Аксубаево%' " +\
                " or city ilike '%Актаныш%' " +\
                " or city ilike '%Алексеевское%' " +\
                " or city ilike '%Апастово%' " +\
                " or city ilike '%Матаки%' " +\
                " or city ilike '%Арск%' " +\
                " or city ilike '%Атня%' " +\
                " or city ilike '%Бавлы%' " +\
                " or city ilike '%Болгар%' " +\
                " or city ilike '%Балтаси%' " +\
                " or city ilike '%Бугульма%' " +\
                " or city ilike '%Буинск%' " +\
                " or city ilike '%Услон%' " +\
                " or city ilike '%Высокая Гора%' " +\
                " or city ilike '%Дрожжаное%' " +\
                " or city ilike '%Елабуга%' " +\
                " or city ilike '%Заинск%' " +\
                " or city ilike '%Зеленодольск%' " +\
                " or city ilike '%Дрожжаное%' " +\
                " or city ilike '%Кайбицы%' " +\
                " or city ilike '%Камское Устье%' " +\
                " or city ilike '%Иннополис%' " +\
                " or city ilike '%Казань%' " +\
                " or city ilike '%Кукмор%' " +\
                " or city ilike '%Лаишево%' " +\
                " or city ilike '%Лениногорск%' " +\
                " or city ilike '%Мамадыш%' " +\
                " or city ilike '%Менделеевск%' " +\
                " or city ilike '%Мензелинск%' " +\
                " or city ilike '%Муслюмово%' " +\
                " or city ilike '%челны%' " +\
                " or city ilike '%Нижнекамск%' " +\
                " or city ilike '%Новошешминск%' " +\
                " or city ilike '%Чистополь%' " +\
                " or city ilike '%Пестрецы%' " +\
                " or city ilike '%Рыбная Слобода%' " +\
                " or city ilike '%Богатые Сабы%' " +\
                " or city ilike '%Сарманово%' " +\
                " or city ilike '%Нурлат%' " +\
                " or city ilike '%Тюлячи%' " +\
                " or city ilike '%Черемшан%' " +\
                " or city ilike '%Уруссу%' " +\
                " or city ilike '%Тетюши%')"

    sql_query = "SELECT " +\
                "       COALESCE(sum(case when country not in('россия', 'Россия', 'russia', 'Russia') and not " +\
               f"		              {tatarstan} then 1 else 0 end), 0) as world, " +\
               f"	   COALESCE(sum(case when {tatarstan} then 1 else 0 end), 0) as tatarstan, " +\
                "		COALESCE(sum(case when country in('россия', 'Россия', 'russia', 'Russia')  " +\
               f"			   and not {tatarstan} then 1 else 0 end), 0) as russia " +\
                "        FROM public.users " +\
                "        where deleted_at is null and " +\
               f"        	  created_at > '{start_date} 00:00:01' AND       " +\
               f"        	  created_at <'{end_date} 23:59:59'"

    return pd.read_sql(sql_query, conn)