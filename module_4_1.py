from fake_math import div as fake_div
from true_math import div as true_div

result_fake = fake_div(10,2)
print("Результат деления с fake_math", result_fake)

result_true = true_div(10, 0)
print("Результат деления с true_math:", result_true)