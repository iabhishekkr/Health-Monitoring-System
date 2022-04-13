client = [[0,"Harry"],[1,"Rohan"],[2,"Hammad"]]
work1 = [[0, "Food"], [1, "Exercise"]]
print("Press 0 If running for the 1st time or To reset the Data\nPress 1 to continue : ")
reset = int(input())
while(reset == 0):
    f = open("HarryFood.txt","w")
    f.write("This is Food Routine of Harry")

    f = open("HarryExercise.txt", "w")
    f.write("This is Exercise Routine of Harry")

    f = open("RohanFood.txt", "w")
    f.write("This is Food Routine of Rohan")

    f = open("RohanExercise.txt", "w")
    f.write("This is Exercise Routine of Rohan")

    f = open("HammadFood.txt", "w")
    f.write("This is Food Routine of Hammad")

    f = open("HammadExercise.txt", "w")
    f.write("This is Exercise Routine of Hammad")

else:
    print("Select the client: ")

    for serial,name in list(client):
        print(serial,name,end="\n")

    n = int(input())
    name = list(client)[n][1]

    for serial,work in list(work1):
        print(serial,work,end="\n")

    workinp = int(input())
    work = list(work1)[workinp][1]


    def getdate():
        import datetime
        return datetime.datetime.now()


    def entry(name,work):
        """This Function is used to update the files"""
        while(True):
            p = open(name+work+".txt", "a")
            print("Enter the schedule of "+work)
            inputdata = input()
            p.write("\n"+str(getdate())+"        "+inputdata)
            p = open(name+work+".txt")
            print("The "+work+" Schedule of "+name+" is : ")
            print(p.read())
            p.close()
            print("1. Continue  2. Exit")
            rerun = int(input())
            if rerun == 1:
                print("Select the client: ")

                for serial, name in list(client):
                    print(serial, name, end="\n")

                n = int(input())
                name = client[n][1]

                for serial, work in list(work1):
                    print(serial, work, end="\n")

                workinp = int(input())
                work = list(work1)[workinp][1]
                continue
            else:
                break
    def view(name,work):
        p = open(name+work+".txt")
        print(p.read())
        p.close()
    print("1. View\n2.Edit")
    mode = int(input())
    if mode == 1:
        view(name,work)
    else:
        entry(name,work)


