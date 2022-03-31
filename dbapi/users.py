import pandas as pd
from dbapi.db_connection import conn
import logging


def getOfflineUsers():
    '''
        Возвращает список людей, которые будут учавствовать offline
    '''
    sql_query = ' SELECT id, email, name, surname, lastname, phone, birthday, sector, role, place_of_work, work_position, country, region, city, online, forum_themes, photo, promo, source, accept_policy, subscribe, password, is_blocked, app_role, remember_token, deleted_at, created_at, updated_at, academic_degree, academic_degree_other, pay_order_id, pay_status, locale, is_vip ' +\
        "           FROM public.users                              " +\
        "           where deleted_at is null and online = 'false'; "
    logging.info(f'DBAPI getOfflineUsers: {sql_query}')

    return pd.read_sql(sql_query, conn)


def getTatarstanUsers(offset=0, limit=10):
    '''
        Возвращает список людей, которые из Татарстана
    '''
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

    logging.info(f'DBAPI getTatarstanUsers: {sql_query}')

    return pd.read_sql(sql_query, conn)


def getCountryStatistic():
    '''
        Возвращает список стран участников
    '''
    sql_query = " SELECT  country, COUNT(*) " +\
        "           FROM public.users       " +\
        "           GROUP BY country;       "

    logging.info(f'DBAPI getCountrisStatistic: {sql_query}')

    return pd.read_sql(sql_query, conn)


def getTotalRegistrationCount(start_date, end_date):
    '''
        Возвращает за выбранный период количество:
             1. участников
             2. участников оffline
             3. спикеров
             4. подтвержденных спикеров
             5. подтвержденных спикеров online
             6. подтвержденных спикеров offline
    '''
    sql_query = "SELECT COUNT(*) AS regs, " +\
                "       sum(case when  online = 'true' then 1 else 0 end) as reg_online," +\
                "       sum(case when  online = 'false' then 1 else 0 end) as reg_offline," +\
                "       sum(case when  role_id = '2' and year = date_part('year', users.created_at) then 1 else 0 end) as speaker," +\
                "       sum(case when  role_id = '2' AND state = 4 and year = date_part('year', users.created_at) then 1 else 0 end) as accepted_speaker," +\
                "       sum(case when  role_id = '2' AND state = 4 and year = date_part('year', users.created_at) AND online = 'true' then 1 else 0 end) AS accepted_speaker_online," +\
                "       sum(case when  role_id = '2' AND state = 4 and year = date_part('year', users.created_at) AND online = 'false' then 1 else 0 end) AS accepted_speaker_offline" +\
                " FROM users left join roles on users.id = roles.user_id" +\
                " WHERE deleted_at IS null AND " +\
        f"       public.users.created_at > '{start_date} 00:00:01' AND " +\
        f"	    public.users.created_at <'{end_date} 23:59:59'"

    logging.info(f'DBAPI getTotalRegistrationCount: {sql_query}')

    return pd.read_sql(sql_query, conn)


def getRegisterationCount(start_date, end_date, page_num=0, limit=10):
    '''
        Возвращает статистику зарегистрированных по дням начиная со стартовой даты(start_date) до конечной(end_date)
    '''
    sql_query = "SELECT to_char(public.users.created_at, 'yyyy.mm.dd') as date, COUNT(*) AS regs, " +\
                "       sum(case when  online = 'true' then 1 else 0 end) as reg_online," +\
                "       sum(case when  online = 'false' then 1 else 0 end) as reg_offline," +\
                "       sum(case when  role_id = '2' AND year = date_part('year', users.created_at) then 1 else 0 end) as speaker," +\
                "       sum(case when  role_id = '2' AND state = 4 AND year = date_part('year', users.created_at) then 1 else 0 end) as accepted_speaker," +\
                "       sum(case when  role_id = '2' AND state = 4 AND year = date_part('year', users.created_at) AND online = 'true' then 1 else 0 end) AS accepted_speaker_online," +\
                "       sum(case when  role_id = '2' AND state = 4 AND year = date_part('year', users.created_at) AND online = 'false' then 1 else 0 end) AS accepted_speaker_offline" +\
                " FROM users join roles on users.id = roles.user_id" +\
                " WHERE deleted_at IS null AND " +\
        f"       public.users.created_at > '{start_date} 00:00:01' AND " +\
        f"	    public.users.created_at <'{end_date} 23:59:59'" +\
                " GROUP BY 1" +\
                " ORDER BY 1 DESC                                                          " +\
        f" OFFSET {page_num * limit + 1}                                            " +\
        f" LIMIT {limit}                                                            "

    logging.info(f'DBAPI getRegisterationCount: {sql_query}')

    return pd.read_sql(sql_query, conn)


def getLocationStatistic(start_date, end_date):
    '''
        Возвращает количество участников из:
            1. Мира, но не России
            2. России, но не Татарстана
            3. Татарстана
    '''
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
    logging.info(f'DBAPI getLocationStatistic: {sql_query}')

    return pd.read_sql(sql_query, conn)


def getYearStatistic():
    '''
        Возвращает количество участников зарегистрированных в каждом месяце за последние два года:
            в прошлом году и текущем
    '''
    months = "        COALESCE(sum(case when to_char(created_at, 'MM') = '01' then 1 else 0 end), 0) as  январь, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '02' then 1 else 0 end), 0) as  февраль, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '03' then 1 else 0 end), 0) as  март, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '04' then 1 else 0 end), 0) as  апрель, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '05' then 1 else 0 end), 0) as  май, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '06' then 1 else 0 end), 0) as  июнь, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '07' then 1 else 0 end), 0) as  июль, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '08' then 1 else 0 end), 0) as  август, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '09' then 1 else 0 end), 0) as  сентябрь, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '10' then 1 else 0 end), 0) as  октябрь, " +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '11' then 1 else 0 end), 0) as  ноябрь," +\
             "        COALESCE(sum(case when to_char(created_at, 'MM') = '12' then 1 else 0 end), 0) as  декабрь "
    sql_query = f" SELECT {months}"+\
                 " FROM  public.users  " +\
                f" WHERE deleted_at IS null AND " +\
                f"       public.users.created_at > '2021-01-01 00:00:00' AND " +\
                f"       public.users.created_at < '2021-12-31 23:59:59' " +\
                 " UNION  " +\
                f" SELECT   {months}" +\
                 " FROM  public.users  " +\
                f" WHERE deleted_at IS null AND " +\
                f"       public.users.created_at > '2022-01-01 00:00:00' AND " +\
                f"       public.users.created_at < '2022-12-31 23:59:59' "

    logging.info(f'DBAPI getTwoYearStatistic: {sql_query}')

    return pd.read_sql(sql_query, conn)


def getLastAndCurrentYearStatistic(currentYear: int):
    '''
        Возвращает количество участников 
            1. За предыдущий год
            2. За предыдущий год спикеров
            3. За текущий год
            4. За текущий год спикеров
    '''
    sql_query = f"SELECT sum(case when users.created_at >= '{currentYear - 1}-01-01' AND " +\
		   		f"	                  users.created_at <= '{currentYear - 1}-12-31' then 1 else 0 end) AS last_year_users, " +\
                f"        sum(case when users.created_at >= '{currentYear - 1}-01-01' AND " +\
                f"                        users.created_at <= '{currentYear - 1}-12-31' AND " +\
                f"                        role = '2' AND state = 3 then 1 else 0 end) AS last_year_speacers, " +\
                f"        sum(case when access_tokens.created_at >= '{currentYear}-01-01' AND " +\
                f"                        access_tokens.created_at <= '{currentYear}-12-31' AND " +\
                f"                        users.created_at < '{currentYear}-01-01' OR " +\
                f"                        users.created_at >= '{currentYear}-01-01' AND " +\
                f"                        users.created_at <= '{currentYear}-12-31' then 1 else 0 end) AS current_year_users, " +\
                f"        sum(case when (access_tokens.created_at >= '{currentYear}-01-01' AND " +\
                f"                        access_tokens.created_at <= '{currentYear}-12-31' AND " +\
                f"                        users.created_at < '{currentYear}-01-01' OR " +\
                f"                        users.created_at >= '{currentYear}-01-01' AND " +\
                f"                        users.created_at <= '{currentYear}-12-31') AND " +\
                 "                        role = '2' AND state = 3 then 1 else 0 end) AS current_year_speacers " +\
                 "    FROM users users " +\
                 "        LEFT JOIN speaker_user_reports reports ON (users.id = reports.user_id) " +\
                 "        LEFT JOIN oauth_access_tokens access_tokens ON (users.id = access_tokens.user_id) " +\
                 "    WHERE  deleted_at IS null AND " +\
                 "        access_tokens.created_at = (SELECT max(oauth_access_tokens.created_at)  " +\
                 "                                    FROM oauth_access_tokens  " +\
                 "                                    WHERE oauth_access_tokens.user_id = users.id) " +\
                 "    OR access_tokens.created_at is null;"

    logging.info(f'DBAPI getLastAndCurrentYearStatistic: {sql_query}')

    return pd.read_sql(sql_query, conn)
