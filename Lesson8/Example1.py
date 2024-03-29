lcdm_year = 13800*10 ** 9
max_year = 9999


class Date:
    def __init__(self, str_dd_mm_yyyy):
        self.str_dd_mm_yyyy = str_dd_mm_yyyy
        self.dig_dd = None
        self.dig_mm = None
        self.dig_yyyy = None

    @classmethod
    def date_to_dig(cls, str_dd_mm_yyyy):
        try:
            dig_dates = map(int, str_dd_mm_yyyy.split('-'))
            date_obj = cls(str_dd_mm_yyyy)
            date_obj.dig_dd, date_obj.dig_mm, date_obj.dig_yyyy = dig_dates
            if Date.check_date_items(date_obj.dig_dd, date_obj.dig_mm, date_obj.dig_yyyy):
                print(f'Формат даты {str_dd_mm_yyyy} правильный')
                return date_obj
            else:
                print(f'Формат даты {str_dd_mm_yyyy} не правильный')
        except ValueError as e:
            print(f'Ошибка в формате даты {str_dd_mm_yyyy}, ERROR {e}')
        except Exception as e:
            print(f'ERROR {e} in Date.date_to_dig')

    @staticmethod
    def check_date_items(day, month, year):
        return 1 <= day <= 31 and 1 <= month <= 12 and -lcdm_year < year < max_year


if __name__ == '__main__':
    my_date_1 = Date.date_to_dig('1-01-2022')
    my_date_2 = Date.date_to_dig('1-01-99998')
    my_date_3 = Date.date_to_dig('1-012022')
    my_date_4 = Date.date_to_dig('1-x-2022')
    my_date_5 = Date.date_to_dig('33-12-2022')