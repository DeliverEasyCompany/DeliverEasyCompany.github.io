import pyqrcode
from pyqrcode import QRCode
from functools import reduce
from datetime import date

today = date.today() 
year = today.year
month = today.month
day = today.day

_order_num = [year, month, day, 1, 2, 3]

if __name__ == '__main__':
     _sec_num = _order_num
     _hlp = ''.join(str(x) for x in _sec_num)

_int_folio = int (_hlp)

qr = pyqrcode.create(_int_folio)
qr.png('QRCifrado.png', scale=11)
print(_int_folio)