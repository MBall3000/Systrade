from datetime import datetime

def check_transaction_open():
    now = datetime.now()
    start_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=15, minute=20, second=0, microsecond=0)
    return start_time <= now <= end_time

def check_transaction_closed():
    now = datetime.now()
    end_time = now.replace(hour=15, minute=20, second=0, microsecond=0)
    return end_time < now
