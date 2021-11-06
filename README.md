# anicli-ru
___
Небольшой скрипт для поиска и просмотра аниме из терминала с русской озвучкой для *unix систем, написанный на python.

Парсит аниме с сайта [animego.org](https://animego.org/) 

Видеоплеер kodik **не поддерживает**, так как у него запросы с видео шифруется **AES**, 
поэтому не все сериалы в нужном дубляже получится посмотреть.
___
# Dependencies:
* mpv или видеоплеер, поддерживающий __hls__ и __cli__ команды
* python 3.5+
* requests
___
# Install:

```
git clone https://github.com/vypivshiy/ani-cli-ru.git
cd ani-cli-ru
sudo make
```
___
# Usage:
`anicli-ru`
___
# Commands:
```
q [q]uit - выход из программы
b [b]ack next step - возвратиться на предыдущий шаг
h [h]elp - вывод списка команд
f [f]ind anime by name - поиск аниме по названию (или при нахождении в главном меню "m >" сразу вводить название)
c [c]lear - очистить консоль
o [o]ngoing print - напечатать недавно вышедшие онгоинги
```
# Optional arguments:
**-p --proxy** - опциональный аргумент на установку прокси. Если просмотр аниме (или некоторых тайтлов) 
запрещен в вашей стране, то это поможет обойти ограничения (Только на получение видеоплеера, сама загрузка видео будет 
идти без прокси)

**-v --videoplayer** - опциональный аргумент выбора видеоплеера. По умолчанию mpv

**-hc --headers-command** - опциональный аргумент команды установки заголовка headers в выбранном плеере.
По умолчанию --http-header-fields (как в mpv)

https: `anicli-ru --proxy https://192.168.0.1:8080`

socks4: `anicli-ru --proxy socks4://192.168.0.1:8888`

socks5: `anicli-ru --proxy socks5://192.168.0.1:8888`
___
![test](https://i.imgur.com/BgUS2GO.png)
___
# ROADMAP:

- [x] добавить поддержку proxy;
- [ ] выбор качества видео;
- [x] вывод вышедших на сегодняшнюю дату онгоингов;
___
Для использования скрипта в windows необходимо установить python 3.5+ версии 
~~и заменить в коде плеер, например, на vlc~~ 
передать нужные аргументы видеоплеера и команду установки headers
