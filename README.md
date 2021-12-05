# Параллелизм и асинхронность
## IO-bound

### Синхронное выполнение
#### Нагрузка
![alt tag](https://sun9-23.userapi.com/impg/I4b1sJGYVVbSLHHpkEKZ2bCv2fJLr4GIQ4a4fw/RgqLvyvtKMM.jpg?size=838x588&quality=96&sign=f36200a5ab74630ed7f5c347e54e63f8&type=album)

Минимальная нагрузка
#### Время
![alt_tag](https://sun9-74.userapi.com/impg/4f6no8AKay35fgKYC8hRYuINgtope9L3MXiJQA/vOdZyrB2KnA.jpg?size=1376x59&quality=96&sign=622048419b81a38c1f024a35e3f40e2d&type=album)

Время выполнения составило 1042с

*Здесь и далее время измерялось через PyCharm Profiler*



### • 5 воркеров
![alt_tag](https://sun9-84.userapi.com/impg/8W05A_uWYiHo7mchUqT_etPWQn7OnVlbZWfJpw/cY94JIOhfz4.jpg?size=834x584&quality=96&sign=d89b88eceecf1b66a505684e065c484d&type=album)

**Нагрузка** на ЦП возросла. Максимально доходила до 15%

**Время** уменьшилось до 197с


### • 10 воркеров
![alt_tag](https://sun9-20.userapi.com/impg/FJjDgKgrgSv19ZqGEIgQ99SunNxh8BXVy43YLg/jtoHVqwD6Po.jpg?size=835x589&quality=96&sign=e3c11e8fa9e95b2b8fde7df66dabf754&type=album)

**Нагрузка** на ЦП в начале доходила до 20, далее держалась в районе 10

**Время** уменьшилось до 85с


### • 100 воркеров
![alt_tag](https://sun9-38.userapi.com/impg/p7txLrHKBBiRu9PsOh_SjF0WIpaqNeLNTUou-g/BvFUDxNnOcM.jpg?size=837x588&quality=96&sign=54daae55f4705b36e1e6f7e7b9cb8fe2&type=album)

**Нагрузка** на ЦП держалась в районе 40

**Время** уменьшилось до 24с

### Вывод
C повышением количества воркеров ускоряется работа программы, но увеличивается нагрузка на ЦП

## CPU-bound
### • 1 ядро
### • 2 ядро
### • 4 ядро
### • 5 ядро
### • 10 ядро
### • 100 ядро
