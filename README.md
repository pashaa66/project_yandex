# **Игра-приключение "Побег из Леска"**
### *Цель - найти выход из Леска*
#### Данный проект представляет собой игру-приключение, в которой игроку придётся найти выход из Леска, минуя все его трудности
# **Техническое задание**
* Идея и оформление
    + Разработать историю для игры
    + Подобрать или разработать самому оформление для игры(дизайн локаций, модель главного героя, модели враждебных и мирных существ, предметы)
    + Проработать локации(расположение предметов, мирных и враждебных существ, препятствий)
    + Схемы локаций будут записаны в txt файлах
* Реализация
    + Создать базу данных
      - Создать таблицу player_statistics с полями: id, player_name, game_result, score
      - Результат прохождения, очки и имя игрока будут записываться в базу данных
    + Создать начальное окно, на котором будет название игры, кнопка _"Начать игру"_
    + После того как пользователь нажмёт на кнопку, его преместит на окно, в котором ему нужно будет придумать имя для персонажа
    + Реализовать основное окно игры:
      - В левом верхнем углу будет располагаться индикатор здровья и заряда фонарика
      - В правом верхнем углу будет находиться счётчик очков
      - Всё остальное пространство экрана будет занято самой игрой
    + В конце игры, в зависимости от результата прохождения, будет появляться финальное окно с подсчётом очков
# **Пояснительная записка**
* Название проекта: Игра-приключение "Побег из Леска"
* Автор проекта: Петров Павел.
* Данный проект представляет собой игру-приключение, в которой игроку придётся найти выход из Леска, минуя все его трудности
* Реализация
    + Классы:
      - Button - отвечает за создание кнопок
      - Camera - отвечает за создание камеры
      - LevelBuilder - класс, в котором обрабатываются картинки, загружаемые в игру, и уровни игры
      - InputBox - класс, который отвечает за создание поля для ввода текста
      - EscapeFromForest - класс, который собирает игру(добавляет кнопки и поля для ввода на экранб выводит уровни на экран)
    + Библиотеки необходимые для запуска:
      - pygame
      - sys
        
