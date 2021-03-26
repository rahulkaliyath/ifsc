from prettytable import PrettyTable
def table(data):
    table = PrettyTable(["Name","Values"],title="Bank Details")
    for key,value in data.items():
        table.add_row([key,value])
    
    print(table)

def table_row(data):
    table = PrettyTable(["Bank Name","IFSC","Address"],title="Bank Details")
    for bank in data:
        table.add_row([bank["BANK"],bank["IFSC"],bank["ADDRESS"][:80]])
    
    print(table)

