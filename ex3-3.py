dayup,dayfactor=1.0,0.01
for i in range(365):
    #day=(day+1)%11
    if i% 10 in[4,5,6,7]:
        dayup=dayup*(1+dayfactor)
    print("{}:天的能力{}".format(i+i,dayup))
print("连续三天，从第四天到第七天每天增长前一天的1%，每十天休息一天:{:.2f}".format(dayup))
