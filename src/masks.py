def get_mask_card_number(card_num: str) -> str:
    """
    Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX.

    :param card_num: Номер карты, состоящий из 16 цифр.
    :return: Замаскированный номер карты.
    :raises ValueError: Если номер карты не состоит из 16 цифр или содержит недопустимые символы.
    """
    if not card_num.isdigit() or len(card_num) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_number = f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"

    return masked_number


def get_mask_account(account_num: str) -> str:
    """Возвращает замаскированный номер счета в формате **XXXX.
    :param account_num: Номер счета, состоящий из 20 цифр.
    :return: Замаскированный номер счета.
    :raises ValueError: Если номер счета не состоит из 20 цифр или содержит недопустимые символы.
    """
    if not account_num.isdigit() or len(account_num) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр.")

    account_masked = f"**{account_num[-4:]}"

    return account_masked


if __name__ == "__main__":
    card_number = "7000792289606361"
    account_number = "73654108430135874305"
    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)
    print(masked_card)
    print(masked_account)
