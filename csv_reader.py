import csv

class csv_data_line:
    def __init__(self, line):
        self.date=self.date_format(line[0])
        self.IDA_users=line[4].split(";")
        self.IDA_containers=[]
        self.IDA_nr=int(line[1])
        self.user=line[3]
        self.event=line[5]

    def export_list(self):
        return [self.date, self.IDA_nr, self.IDA_containers, self.event,  self.user, self.IDA_users]

    def date_format(self,u_date):
        return u_date[8:9] + ":" + u_date[5:6] + ":" + u_date[0:3]




def read_CSV(csv_file):
    csv_format=[]
    with open(csv_file, newline=" ") as file:
        reader = csv.reader(file, delimeter=",")
        n=0
        for row in reader:
            if n != 0:
                csv_format.append(csv_data_line(row))
            else:
                n=1
