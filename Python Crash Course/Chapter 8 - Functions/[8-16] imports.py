
# 1. import module_name
import modules.car_module

car1 = modules.car_module.make_car('subaru', 'outback', color='blue')
print(car1)

# 2. from module_name import function_name
from modules.car_module import make_car

car2 = make_car('honda', 'civic', color='red')
print(car2)

# 3. from module_name import function_name as fn
from modules.car_module import make_car as mc

car3 = mc('ford', 'mustang', color='yellow')
print(car3)

# 4. import module_name as mn
import modules.car_module as cm

car4 = cm.make_car('toyota', 'corolla', color='black')
print(car4)

# 5. from module_name import *
from modules.car_module import *

car5 = make_car('tesla', 'model 3', color='white')
print(car5)