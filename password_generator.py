import random
import string
import datetime
import pandas as pd
from csv import DictWriter
import sys
def get_random_string(length=11):
    # choose from all lowercase letter
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Random string of length", length, "is:", password)
    return password
def get_password(length = 11):
    passw = get_random_string(length)
    format = "%d-%m-%Y %H:%M:%S"
    curr = datetime.datetime.now().strftime(format)
    print(curr)
    op_dict = {"Date" : curr, "Password" : passw}
    with open('pass.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=["Date", "Password"])
        dictwriter_object.writerow(op_dict)
        f_object.close()
    print(op_dict)
    df2 = pd.read_csv("pass.csv")
    print(df2)
if __name__ == "__main__":
    length = int(sys.argv[1])
    get_password(length = length)