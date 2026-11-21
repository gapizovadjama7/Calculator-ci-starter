class Calculator:
def add(self, a: float, b: float) -&gt; float:
&quot;&quot;&quot;Возвращает сумму двух чисел.&quot;&quot;&quot;
return a + b

def subtract(self, a: float, b: float) -&gt; float:
&quot;&quot;&quot;Возвращает разность двух чисел (a - b).&quot;&quot;&quot;
# БАГ ДЛЯ СТУДЕНТОВ: Неверный порядок вычитания
return b - a

def multiply(self, a: float, b: float) -&gt; float:
&quot;&quot;&quot;Возвращает произведение двух чисел.&quot;&quot;&quot;
# БАГ ДЛЯ СТУДЕНТОВ: Захардкоженный результат
return 4.0

def divide(self, a: float, b: float) -&gt; float:
&quot;&quot;&quot;Возвращает частное от деления a на b.
При делении на ноль должен выбрасывать ValueError.
&quot;&quot;&quot;
# БАГ ДЛЯ СТУДЕНТОВ: Вместо исключения возвращает 0
if b == 0:
return 0.0
return a / b
