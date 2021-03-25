from prettytable import PrettyTable
def table(data):
    table = PrettyTable(["Name","Values"],title="Bank Details")
    for key,value in data.items():
        table.add_row([key,value])
    
    print(table)

