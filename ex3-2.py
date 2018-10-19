dayup,dayfactor=1.0,0.01
for i in range(365):
    if i% 7 not in [3,4,5,6]:
        dayup=dayup*(1+dayfactor)
print("前三天的能力值，第四天到第七天为前一天的1%的力量：{:.2f}".format(dayup))
