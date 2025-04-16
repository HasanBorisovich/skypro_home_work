from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(num_for_mask: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.

    :param num_for_mask: Тип и номер карты или счета.
    :return: Строка с замаскированным номером.
    """

    num_for_mask_split = num_for_mask.split()
    if "Счет" in num_for_mask_split:
        return f"Счет {get_mask_account(num_for_mask_split[1])}"
    else:
        card_num = []
        card_name = []
        for i in num_for_mask_split:
            if i.isdigit():
                card_num.append(i)
            if i.isalpha():
                card_name.append(i)
        str_card_num = " ".join(card_num)
        str_card_name = " ".join(card_name)
        return f"{str_card_name} {get_mask_card_number(str_card_num)}"


def get_date(inp_inf: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")

    :param inp_inf: Вводимая дата.
    :return: Строка содержащая дату в формате "ДД.ММ.ГГГГ"
    """

    date_inf = datetime.strptime(inp_inf[:10], "%Y-%m-%d")
    return f"{date_inf.day:02}:{date_inf.month:02}:{date_inf.year}"


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
    print(mask_account_card("Счет 73654108430135874305"))
