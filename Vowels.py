name = str(input('Enter name: '))

weight = int(input('Enter weight(kg): '))

height = eval(input('Enter height(m²): '))

upremark = "you're underweight!"

remark = "you're overweight!"

bmi_calc = (weight/height)

if bmi_calc < 25:
  print('weight(kg): ' + str(weight))
  print('height(m²): ' + str(height))
  print('BMI: ' + str(bmi_calc))
  print('Hey ' + name + ', '+ upremark)
  
if bmi_calc >= 25:
  print('weight(kg): ' + str(weight))
  print('height(m²): ' + str(height))
  print('BMI: ' + str(bmi_calc)+' Kg/m²')
  print('Hey ' + name + ', '+ remark)
      