import re


# if __name__ == '__main__':
#     excldPattern = re.compile("^.*60MIN.*$|.*Downlink Resource.*")

#     msg = "5MIN/20230220/0620-0625-Downlink Resource Allocation per Slot and Table"

#     if excldPattern.match(msg):
#         print("true")
#     else:
#         print("false")


if __name__ == '__main__':
    # element = 'RAN-EMS0054'
    # if element.startswith('RAN-EMS') and (element.endswith('_3G') or element.endswith('_5G')):
    #     print('yes')
    # else:
    #     print('no')
    # name = '1815-1820-ABC-AMF-22.A.0.csv'
    # split = name.split('-')
    # org = split[len(split)-1]
    # print(org)

    # pkgVer = '23.03.08'

    # st = re.fullmatch('(\d{2}).(\d{2}).(\d{2})', pkgVer)

    # if st:
    #     print('yes')
    # else:
    #     print('no')
    # print(st)
    
    name = 'ALARM.22'
    arg = ' '
    ver = name.split(arg)
    print(ver)

    if len(ver) > 1:
        print(ver)
    else:
        print('no')