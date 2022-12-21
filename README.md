# Алгоритм Фано

Алгоритм Ше́ннона — Фанó — один из первых алгоритмов сжатия, который впервые сформулировали американские учёные Клод Шеннон и Роберт Фано. Данный метод сжатия имеет большое сходство с алгоритмом Хаффмана, который появился на несколько лет позже и является логическим продолжением алгоритма Шеннона. Алгоритм использует коды переменной длины: часто встречающийся символ кодируется кодом меньшей длины, редко встречающийся — кодом большей длины. Коды Шеннона — Фано — префиксные, то есть никакое кодовое слово не является префиксом любого другого. Это свойство позволяет однозначно декодировать любую последовательность кодовых слов.

### Основные этапы

1. Символы первичного алфавита m1 выписывают по убыванию вероятностей.
2. Символы полученного алфавита делят на две части, суммарные вероятности символов которых максимально близки друг другу.
3. В префиксном коде для первой части алфавита присваивается двоичная цифра «0», второй части — «1».
4. Полученные части рекурсивно делятся, и их частям назначаются соответствующие двоичные цифры в префиксном коде.

Когда размер подалфавита становится равен нулю или единице, то дальнейшего удлинения префиксного кода для соответствующих ему символов первичного алфавита не происходит, таким образом, алгоритм присваивает различным символам префиксные коды разной длины.

---

### Временная сложность

O(n logn)

---

### Пример

Исходные символы:

1. A (частота встречаемости 50)
2. B (частота встречаемости 39)
3. C (частота встречаемости 18)
4. D (частота встречаемости 49)
5. E (частота встречаемости 35)
6. F (частота встречаемости 24)

![](https://upload.wikimedia.org/wikipedia/ru/1/17/%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE_%D0%A8%D0%B5%D0%BD%D0%BD%D0%BE%D0%BD%D0%B0.PNG)

Полученный код: A — 11, B — 101, C — 100, D — 00, E — 011, F — 010.

При построении кода Шеннона — Фано разбиение множества элементов может быть произведено, вообще говоря, несколькими способами. Выбор разбиения на уровне n может ухудшить варианты разбиения на следующем уровне (n + 1) и привести к неоптимальности кода в целом. Другими словами, оптимальное поведение на каждом шаге пути ещё не гарантирует оптимальности всей совокупности действий. Поэтому код Шеннона — Фано не является оптимальным в общем смысле, хотя и дает оптимальные результаты при некоторых распределениях вероятностей. Для одного и того же распределения вероятностей можно построить, вообще говоря, несколько кодов Шеннона — Фано, и все они могут дать различные результаты. Если построить все возможные коды Шеннона — Фано для данного распределения вероятностей, то среди них будут находиться и все коды Хаффмана, то есть оптимальные коды.

### Запуск

Создать файл data.txt, в который передать 1 строкой символы, 2 строкой их вероятности, 3 строкой сообщение

Пример

```
a b c d e
0.2 0.1 0.3 0.2 0.2
abbdeecacbdddee
```

Команда для запуска

```
python fano.py
```

# Преобразование Барроуза-Уилера

Преобразование Барроуза — Уилера — это алгоритм, используемый в техниках сжатия данных для преобразования исходных данных.

---

### Основные этапы

1. Составляется таблица всех циклических сдвигов входной строки.
2. Производится лексикографическая (в алфавитном порядке) сортировка строк таблицы.
3. В качестве выходной строки выбирается последний столбец таблицы преобразования и номер строки, совпадающей с исходной.

Декодирование:

Выпишем в столбик нашу преобразованную последовательность символов.
Запишем её как последний столбик предыдущей матрицы (при прямом
преобразовании Барроуза — Уилера), при этом все предыдущие столбцы
оставляем пустыми. Далее построчно отсортируем матрицу, затем в
предыдущий столбец запишем преобразованную последовательность.
Опять построчно отсортируем матрицу. Продолжая таким образом, можно
восстановить полный список всех циклических сдвигов строки, которую
нам надо найти. Выстроив полный отсортированный список сдвигов,
выберем строку с номером, который нам был изначально дан.

---

### Временная сложность

O(N^2\*logN)

---

### Пример

![](https://www.pvsm.ru/images/2014/09/04/algoritmy-sjatiya-dannyh-bez-poter-chast-2.png)

### Запуск

Передать в функцию bw_restore первым аргументов - индекс, вторым аргументов - закодированное сообщение

Пример

```
bw_restore(24, 'styssesvmrgath  ceiis eee r')
```

Команда для запуска

```
python bwt.py
```

# Алгоритм LZW

Алгори́тм Ле́мпеля — Зи́ва — Уэлча (Lempel-Ziv-Welch, LZW) — это универсальный алгоритм сжатия данных без потерь, созданный Авраамом Лемпелем (англ. Abraham Lempel), Яаковом Зивом (англ. Jacob Ziv) и Терри Велчем (англ. Terry Welch).

---

### Основные этапы

1. Все возможные символы заносятся в словарь. Во входную фразу X заносится первый символ сообщения.
2. Считать очередной символ Y из сообщения.
3. Если Y — это символ конца сообщения, то выдать код для X, иначе:
   Если фраза XY уже имеется в словаре, то присвоить входной фразе значение XY и перейти к Шагу 2 ,
   Иначе выдать код для входной фразы X, добавить XY в словарь и присвоить входной фразе значение Y. Перейти к Шагу 2.
   Конец.

Декодирование

Декодер LZW сначала считывает индекс (целое число), ищет этот индекс в
словаре и выводит подстроку, связанную с этим индексом. Первый символ
этой подстроки конкатенируется с текущей рабочей строкой. Эта новая
конкатенация добавляется в словарь (подобно тому, как подстроки были
добавлены во время сжатия). Затем декодированная строка становится
текущей рабочей строкой (текущий индекс, т.е. подстрока, запоминается),
и процесс повторяется.

---

### Временная сложность

O(n), так как каждый байт читается только один раз, а сложность операции для каждого символа константна.

---

### Пример

![](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/lempel%E2%80%93ziv%E2%80%93welch-compression-technique.png)

### Запуск

Пример

```
compressed = compress('TOBEORNOTTOBEORTOBEORNOT')
print(compressed)
decompressed = decompress(compressed)
print(decompressed)
```

Результат

```
[84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260, 265, 259, 261, 263]
TOBEORNOTTOBEORTOBEORNOT
```

Команда для запуска

```
python lzw.py
```
