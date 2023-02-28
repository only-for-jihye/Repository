import re


if __name__ == '__main__':
    excldPattern = re.compile("^.*60MIN.*$|.*Downlink Resource.*")

    msg = "5MIN/20230220/0620-0625-Downlink Resource Allocation per Slot and Table"

    if excldPattern.match(msg):
        print("true")
    else:
        print("false")