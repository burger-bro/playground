class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = {chr(ord('A')+i): [0]*(rows) for i in range(26)}

    def setCell(self, cell: str, value: int) -> None:
        ch, row = cell[0], cell[1:]
        self.spreadsheet[ch][int(row)-1] = value

    def resetCell(self, cell: str) -> None:
        ch, row = cell[0], cell[1:]
        self.spreadsheet[ch][int(row)-1] = 0


    def getValue(self, formula: str) -> int:
        op1, op2 = formula[1:].split('+')
        return self.get_num(op1) + self.get_num(op2)
    
    def get_num(self, op: str) -> int:
        if op[0].isalpha():
            ch, row = op[0], op[1:]
            num = self.spreadsheet[ch][int(row)-1]
        else:
            num = int(op)
        return num


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)