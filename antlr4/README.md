## Установка
```
OS X
$ cd /usr/local/lib
$ sudo curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'

LINUX
$ cd /usr/local/lib
$ wget https://www.antlr.org/download/antlr-4.9.2-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.9.2-complete.jar'
$ alias grun='java org.antlr.v4.gui.TestRig'

Windows
1. Download https://www.antlr.org/download/antlr-4.9.2-complete.jar.
2. Add antlr4-complete.jar to CLASSPATH, either:
    2.1. Permanently: Using System Properties dialog > Environment variables > Create or append to CLASSPATH variable
    2. Temporarily, at command line:
        SET CLASSPATH=.;C:\Javalib\antlr4-complete.jar;%CLASSPATH%
3. Create batch commands for ANTLR Tool, TestRig in dir in PATH
    antlr4.bat: java org.antlr.v4.Tool %*
    grun.bat:   java org.antlr.v4.gui.TestRig %*
```

## Описание функциональности
У парсера очень большая функциональность, которая описана в отдельной книге. Коротко о самых важных вещах:

Грамматику надо описывать в файле `*.g4`. C помощью команды `antlr4` можно собрать parser/lexer/listener + visitor
```
$ antrl4 -Dlanguage=Python3 MyGrammer.g4 //создаст все необходимые файлы на языке python
// если не указывать ключ -Dlanguage, то будет собираться под Java
```
Можно собирать все генерируемые файлы в отдельную директорию
```
$ antlr4 -Dlanguage=Python3 MyGrammer.g4 -o dist_python
```
Можно также создать `visitor`, который пользователь потом может переопределить для своих нужд ([пример](https://github.com/alexbuyan/fl-2021-hse-win/blob/proj/antlr4/main.py))
```
$ antlr4 -Dlanguage=Python3 MyGrammer.g4 -visitor -o dist_python
```

Графическое представление деревьев можно реализовать только при сборке под Java:
```
$ antlr4 MyGrammer.g4 -o dist_java
$ cd dist_java
$ javac MyGrammer*.java
$ grun MyGrammer s -gui
aaaaa                // вводим строчку
^D (^Z for Windows)  // обязательно нажимаем, чтобы запустился TestRig
```
С другими языками доступен вывод дерева в виде строки
```
$ python main.py
>>> aaaa
(s (s a) (s (s a) (s a)) (s a))
```

## Преимущества парсера
Парсер достаточно прост в использовании и быстро пишется (так как не надо самому создавать `parser` и `lexer`, `ANTLR` все сделает сам). 

Одним из преимуществ является `visitor` и его переопределение. Это помогает быстро написать функции проверки принадлежности введенного слова нашему языку
```
$ python main.py
>>> aaaa
True
(s (s a) (s (s a) (s a)) (s a))
>>> abab
False
(s (s a) (s (s b) (s a)) (s b))
```

## Недостатки парсера
Главным недостатком является скорость работы парсера на неоднозначных грамматиках. В отличие от GLR он не умеет сам разбираться с конфликтами, либо делает это очень плохо, поэтому время работы растет эскпоненциально

Размер ввода (количество символов)| Время работы
------------- | -------------
5 | 0.017
10 | 0.263
15 | 2.460
20 | 33.994
... | ...
25 | 274.650