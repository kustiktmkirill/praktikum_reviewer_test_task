import datetime as dt

# TODO: Желательно использовать типизацию для входных данных методов.


class Record:
    # TODO: отсутствуют докстринги.
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # TODO: Перенос усложнает читаемость кода. Можно сократить условие.
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    # TODO: отсутствуют докстринги.
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # TODO: Согласно стандарту PEP8 переменные стоит
        #  называть со строчной буквы. Может запутать других разработчиков.
        # TODO: Переопределение имени Record (ранее Record являлось классом).
        for Record in self.records:
            # TODO: Лучше вынести dt.datetime.now().date() в отдельную
            #  переменную за пределами цикла. Таким образом можем
            #  избавиться от лишних повторных операций.
            if Record.date == dt.datetime.now().date():
                # TODO: Лучше использовать краткую форму записи с помощью +=
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # TODO: Переносы усложняют читаемость кода.
            #  Также можно сократить условие: 0 <= (today - record.date).days < 7
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # TODO: отсутствуют докстринги
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # TODO: Нужно дать переменной x корректное название.
        #  Перменная x не несёт в своём названии никакой информации
        #  о её предназначении.
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            # TODO: Можно обойтись без else, т.к присутствует return
            # TODO: Необязательные скобки в return, можно без них.
            return('Хватит есть!')


class CashCalculator(Calculator):
    # TODO: отсутствуют докстринги.
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):

        # TODO: Необязательное объявление переменных USD_RATE и EURO_RATE
        #  Можно обращаться через self.USD_RATE и self.EURO_RATE соответственно.
        #  Это избавит нас ещё от переноса (ограничено до 79 симвоов).
        # TODO: Также переменные стоит называть со строчной буквы.
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            # TODO: Необязательные скобки в return
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # TODO: Для обращения отрицательной переменной cash_remained
            #  лучше использовать функцию abs()
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    # TODO: Лишнее переопределение родительской функции get_week_stats()
    def get_week_stats(self):
        super().get_week_stats()
