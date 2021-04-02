# espanso
Конфигурационные файлы для клавиатурного расширения с помощью espanso

## Общая идея использования

Конфигурационные файлы храним здесь (в гите). Кроме конфигурационных файлов храним также общие скрипты и "документы" (типа мини хелпов). Тогда за счет гита получаем на всех компьютерах одинаковые возможности.

Что хочется попробовать сделать (с помощью еспансо)

### Клавиатурное расширение

Это понятно, это его прямая функция. Можно будет меньше писать

### Наиболее часто выполняющиеся команды

Хранить в конфигах наиболее часто выполняющиеся команды с тем, чтобы каждый раз их не вспоминать и не набирать

Примеры

* history | grep 
* ssh korolmi@saptesting.ru
* source ~/local/go_sand.sh

и т.п.

Чем хранить эти команды в эспанос лучше, чем в алиасах или еще что-то: с посмощью эспансо это делаем централизованно, все храним в эспансо, его возможности по показу списков и наши дополнения (см. ниже про них) делают это удобным.

### Основные команды какой-нибудь подисистемы или утилиты

Тот же гит или опенвипиэн - ну долго это набирать и не все хочется помнить. Тогда мы пишем это в user файл, по умолчанию не включаем, если нужно включить - редактируем соответствующий user файл (espanso edit userfile) и все...

## Помощь по эспансо

Чего не хватает - возможности посмотреть

* список доступных команд
* описание конкретной команды

Список - это espanso match list (зашить в хелп и какой-то триггер)

Описание конкретной команды - пока это можно делать просто показом целого файла (хотя не сложно обрамлять какими-нибудь комментами и тогда можно просто отгрепить или еще что-то - отпитонить)


