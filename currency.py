rawValue = input("Input the value of the money you wish to withdraw in dollars and cents:")
r_hundreds = round(float(rawValue)%100,2)
hundreds = round((float(rawValue)-r_hundreds)/100)
r_fifties = round(float(rawValue)%50,2)
fifties = round(r_hundreds-r_fifties)/50
r_twenties = round(float(rawValue)%20,2)
twenties = round(r_fifties-r_twenties)/20
r_tens = round(float(rawValue)%10,2)
tens = round(r_twenties-r_tens)/10
r_ones = round(float(rawValue)%1,2)
ones = round(r_tens-r_ones)/1

print(rawValue,"can be made with:",hundreds,"hundred dollar bill(s)")
print(fifties,"fifty dollar bill(s)")
print(twenties,"twenty dollar bill(s)")
print(tens,"ten dollar bill(s)")
print(ones,"one dollar bill(s)")
print("and",r_ones,"cents")

