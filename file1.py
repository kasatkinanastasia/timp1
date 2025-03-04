def add(x, y):
  """Сложение"""
  return x + y

def subtract(x, y):
  """Вычитание"""
  return x - y

def multiply(x, y):
  """Умножение"""
  return x * y

def divide(x, y):
  """Деление"""
  if y == 0:
    return "Ошибка! Деление на ноль."
  else:
    return x / y

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

while True:
  try:
    choice = input("Введите номер операции (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
      print("Неверный ввод. Пожалуйста, введите число от 1 до 4.")
      continue  # Перезапуск цикла

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

    # Просим пользователя, хочет ли он выполнить еще одну операцию
    # или выйти из программы
    next_calculation = input("Хотите выполнить еще одну операцию? (да/нет): ")
    if next_calculation.lower() == "нет":
      break
    elif next_calculation.lower() == "да":
      continue  # Начинаем новый цикл
    else:
        print("Неверный ввод. Завершение программы.")
        break
  except ValueError:
    print("Неверный ввод. Пожалуйста, введите число.")
  except Exception as e:
    print(f"Произошла ошибка: {e}")  # Обработка других возможных ошибок
