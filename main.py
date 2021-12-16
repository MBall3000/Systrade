from strategy.RSIStrategy import *
import sys

app = QApplication(sys.argv)

rsi_strategy = RSIStrategy()
rsi_strategy.start()


#kiwoom.get_account_number()
#df = kiwoom.get_price_data("005930")
#print(df)

#order_result = kiwoom.send_order('send_buy_order', '1001', 1 , '007700', 1, 39750, '00')
#print(order_result)

#deposit = kiwoom.get_deposit()

#orders = kiwoom.get_order()
#print(orders)

#position = kiwoom.get_balance()
#print(position)

# kiwoom.set_real_reg("1000", "", get_fid("장운영구분"), "0")
#fids = get_fid("체결시간")
#codes = '005930;007700;00060'
#kiwoom.set_real_reg("1000", codes, fids, "0")

"""
kospi_code_list = kiwoom.get_code_list_by_market("0")
print(kospi_code_list)
for code in kospi_code_list:
    code_name = kiwoom.get_master_code_name(code)
    print(code, code_name)

kosdaq_code_list = kiwoom.get_code_list_by_market("10")
print(kosdaq_code_list)
for code in kosdaq_code_list:
    code_name = kiwoom.get_master_code_name(code)
    print(code, code_name)
"""

app.exec_()
