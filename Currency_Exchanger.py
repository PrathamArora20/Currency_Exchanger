import requests
import csv
from tkinter import *


root=Tk()
root.title('Currency Conversion ')

def countyCodes():
  ''' This function reads from a CSV files and imports the information of each country and their corresponding currency code they use'''

  countryCurrency={}
  with open("Country_Codes.csv",'r') as file:
      csvreader=csv.reader(file)

      for row in csvreader:
          countryCurrency[row[1].lower()]=row[0].strip().lower()

  return countryCurrency



def ApiExtracting(convert_currency,base_currency,convert_amount):
  ''' This function with the help of API , Converts the currency from a base currency to a currency that is desired. The user can either input the country or the currency to be converted'''
  
  formatedResult=''
  url = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_currency}&from={base_currency}&amount={convert_amount}"

  payload = {}
  headers= {
    "apikey": "ij3O3znGdIGLL39dLNf2nqG2Z3rTQPR9"
  }

  response = requests.request("GET", url, headers=headers, data = payload)
  status=response.status_code

  if status==200:
    json_conversion=response.json()
    convertion=json_conversion['result']  #gets the converted currency
    formatedResult=str(convertion) + ' ' + convert_currency.upper()
    return formatedResult   
  else:
    formatedResult="Please check the Country name or Country Currency Code"

  return formatedResult


def calculate(base_currency,convert_currency,convert_amount):
  '''Checks weather the inputed value is a Country or a Currency code'''

  countryCurrency=countyCodes()

  if len(base_currency)>3:
    base_currency=countryCurrency.get(base_currency,0) # It either finds the country currency code or returns 0

  if len(convert_currency)>3:
    convert_currency=countryCurrency.get(convert_currency,0) 

  formatedResult=ApiExtracting(convert_currency,base_currency,convert_amount)  #Calls the API to get the information
  resultPrint=Entry(root,text=formatedResult,width=70) #Displays the results
  resultPrint.delete(0,END)
  resultPrint.insert(0,formatedResult)
  resultPrint.grid(row=5,column=0)
  

def main():
  label1=Label(root, text="Please enter the Country name or Currency Code you would like to convert from:")
  label2=Label(root, text="Please enter the Country name or Currency Code you would like to convert to:")
  amountLabel=Label(root, text="Please enter the amount you would like to convert:")
  label3=Label(root, text="")

  inputFrom=Entry(root)
  inputTo=Entry(root)
  inputAmount=Entry(root)

  #Formatting for Tinker
  label1.grid(row=0,column=0)
  inputFrom.grid(row=0,column=1)
  label2.grid(row=1,column=0)
  inputTo.grid(row=1,column=1)
  amountLabel.grid(row=2,column=0)
  inputAmount.grid(row=2,column=1)
  label3.grid(row=3,column=0)
  label3.grid(row=4,column=0)
  
  button1=Button(root, text="Convert",padx=50,command=lambda: calculate(inputFrom.get().strip().lower(),inputTo.get().strip().lower(),inputAmount.get()),border=4)
  button1.grid(row=4,column=0) 

  root.mainloop()
  button1=Button(root, text="Convert",padx=50,command=lambda: calculate(inputFrom.get().strip().lower(),inputTo.get().strip().lower(),inputAmount.get()),border=4)
  
  

main()