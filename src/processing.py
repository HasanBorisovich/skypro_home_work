from typing import Any, Dict, List
from datetime import datetime

transactions_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

def filter_by_state(_list: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция отфильтровывает список транзакций по заданному состоянию."""
    return [item for item in _list if item.get("state") == state]

def sort_by_date(_list: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция возвращает список, отсортированный по дате."""
    # Для корректной сортировки преобразуем строку даты в объект datetime
    return sorted(_list, key=lambda x: datetime.fromisoformat(x.get("date")), reverse=reverse)

if __name__ == "__main__":
    print(filter_by_state(transactions_list, "EXECUTED"))
    print(sort_by_date(transactions_list))
