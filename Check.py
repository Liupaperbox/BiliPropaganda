import os,re
#python3 Check.py
pattern = "/dev/sda"
place = "/Kodtata"

def checkdisk(pattern,place):
    def mount(disk,place):
        result = os.popen('mount ' + disk + " " + place).readlines()
    pattern = "Disk " + pattern
    result = os.popen('fdisk -l').readlines()
    for i in range(0, result.__len__())[::-1]:
        no = result[i].replace("\n","").replace("\r","")
        rea = re.search(pattern, no)
        if rea:
            mount(pattern,place)
            break

checkdisk(pattern,place)