## Описание генератора парсеров Yacc

### Установка
Для использования парсера предварительно требуется установить модуль `PLY`, для подключения генератора `yacc` в начале программы необходимо прописать:
```
from ply import lex
import ply.yacc as yacc
```

### Команда для запуска
Для парсера, написанного на `python3` с лексером в файле `lex.py` и парсером в файле `parser.py`, `lex.py` необходимо импортировать внутрь `parse.py`. Из консоли парсер запускается командой:
```
python3 parse.py <название файла входных данных>
```

### Описание, особенности
`Yacc` -- классический, наиболее известный и достаточно простой генератор парсеров; название получил от сокращения "Yet Another Compiler Compiler".

Сгенерированный парсер рассматривает контекстно-свободные грамматики, используется `LALR`-парсер.

Интуитивно: взаимодействие с `yacc`-ом сводится к описанию пользователем вводимой им лексической структуры, после чего парсер начинает разбивать программу на соответствующие компоненты. Итого в программе должны существовать 3 структурные части -- описания токенов, сами правила задания языка, подпрограммы.

***Особенность***: обязательное требование для парсера, сгенерированного с помощью `yacc`, -- наличие лексического анализатора. Чаще всего в качестве лексеров используются *lex* или *flex*.

#### Описания токенов
В лексере *lex* задается набор токенов (массив-словарь, который обязательно должен иметь имя `tokens`):
```
tokens = [
  'LETTER',
  'NUM',
  'DASH',
  'COMMA',
]
```
Каждый из токенов описывается регулярным выражением, которое может быть оформлено либо в виде строки, либо в виде функции, например:
```
t_DASH = r'--'

def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t
```
Примечательно, что названия функций, задающих регулярные выражения для токенов, начинаются с `t_`.

Затем токены используются в парсере для описания правил языка (грамматики).

#### Структура парсера
Сперва описываются правила грамматики. Названия соответствующих функций должны начинаться с `p_`:
```
def p_expr_plus(p):
    'expr : expr PLUS term'
    p[0] = p[1] + p[3]
```
***Особенность***: можно **обратиться к конкретному элементу правила по его индексу** в строке описания, что является большим преимуществом по сравнению с другими парсерами, где доставать элементы приходится более сложными путями.

Несколько правил грамматики можно объединять в одну функцию. Если какие-либо правила описаны ниже, парсер последовательно спускается до самого нижнего уровня, проверяя соответствия на каждом из них, затем поднимается обратно, либо заматчив строку, либо нет.

Задание лексера и парсера может происходить, к примеру, так:
```
lexer  = lex.lex()       # Return lexer object
parser = yacc.yacc()     # Return parser object
```
Затем в бесконечном цикле считываются строки файла, которые затем поочередно подаются в парсер, где пытаются попасть под какое-либо правило.

### Преимущества
1. `Yacc` отлично справляется с **распознаванием неоднозначностей**. Для этого все правила, описывающие язык, исходно разделяются на 2 типа: свертки и переносы. На случай возникновения конфликта, то есть ситуации, когда к одному выражению можно применить несколько правил, в `yacc`-e четко зафиксированы правила разрешения неоднозначностей и приоритеты операций, поэтому даже на неоднозначной грамматике парсер сможет построить алгоритм разбора.

2. Высокая **скорость работы** парсера.

3. **Понятный** вывод ошибок. `PLY` в случае возникновения ситуаций непопадания под правила, генерирует файл `parsetab.py`, где можно увидеть последовательность проверки функций. Отключить автоматическую генерацию таблицы можно с помощью команды:
```
yacc.yacc(debug=0, write_tables=0)
```

4. Возможность использования различных флагов компиляции, которые могут, например, повысить скорость чтения данных из файла, или перевести пользователя в другой режим.

5. **Удобство** использования -- простота понимания принципов написания функций для разбора правил, быстрое обращение к элементу правила (см. структуру парсера).

6. Понятная документация, большое число источников информации о генераторе.

### Время работы на словах различной длины
Как отмечалось ранее, неоднозначности `yacc` разрешает эффективно, поэтому с увеличением размера входа время растет линейно.

| Длина слова   | Время работы (сек)    | Округление |
| ------------- | ----------------------| -----------|
| 1             | 0.0000777244567871094 | 0.00008    |
| 5             | 0.0001101493835449219 | 0.00011    |
| 10            | 0.0001409053802490234 | 0.00014    |
| 20            | 0.0002460479736328125 | 0.00025    |
| 30            | 0.0003409385681152344 | 0.00034    |
| 40            | 0.0003838539123535156 | 0.00038    |
| 50            | 0.0004680156707763672 | 0.00047    |
| 60            | 0.0005559921264648438 | 0.00056    |
| 70            | 0.0006518363952636719 | 0.00065    |
| 80            | 0.0007410049438476562 | 0.00074    |
| 90            | 0.0013880729675292969 | 0.00139    |
| 100           | 0.0017700195312500000 | 0.00178    |

Тестовый файл *input_time_tests* с примерами можно найти в папке tests.

### Недостатки
Главным недостатком модуля `PLY`, применяемого для использования `yacc`-а, является **отсутствие автоматического построения деревьев обхода** и абстрактных синтаксических деревьев -- нет доступной команды, записывающейся в несколько строчек и позволяющей сформировать наглядное представление дерева разбора грамматики. При необходимости пользователю придется самому рисовать такие деревья.

### Полезные ссылки
* [Документация](https://www.dabeaz.com/ply/ply.html#ply_nn22) `Yacc`
* [Cтатья](https://codecamp.ru/blog/python-python-lex-yacc/) для ознакомления с работой с лексера и парсера PLY
* [Статья]() с описанием методов разрешения неоднозначностей
