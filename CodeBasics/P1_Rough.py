import re


def range_to_average(x):
    min_max =str(x).split('-')
    convert=str(x).split('Sq. ')

    if len(min_max)==2:
        return (float(min_max[0])+float(min_max[1]))/2

    elif convert[-1].lower() == "meter":
        return float(convert[0])*10.763

    elif convert[-1].lower() == "yards":
        return float(convert[0]) * 9

    elif len(x) >2:
        num=re.findall(r'\d+', x)
        return float(num[0])
    else:
        return float(x)


# print(range_to_average('24Ghjnnjnj65'))