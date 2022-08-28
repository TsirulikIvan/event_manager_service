# Менеджер для создания мероприятий

## Описание

Цель просто упростить создания выездных или квартирных ивентов, рассылки информации определнным людям и бла-бла-бла

## Установка
Я заморочился поэтому использую Poetry

### Подготовка окружения

1. Установить питон 3.10
2. Установить Poetry (https://python-poetry.org/)

### Непосредственно установка
```shell
git clone https://github.com/TsirulikIvan/event_manager_service.git

poetry install
```


## Советы

Перед тем как пушить лучше удостовериться что код корректно отформатирован, есть 2 опции

1. Запустить Makefile

*Ubuntu*

```shell
make .
```

*Windows*

```shell
nmake -f Makefile.win
```

2. Делать через ряд команд

```shell
black app tests
isort app tests
mypy app tests
pylint app tests
pytest -v --cov=app tests
```

