from bs4 import BeautifulSoup
import requests

web = requests.get("https://www.google.com/finance/quote/USD-EGP?sa=X&sqi=2&ved"
                   "=2ahUKEwiKht_S6euAAxWmRPEDHQucA88QmY0JegQIDhAr")
# print(web)
soup = BeautifulSoup(web.content, "lxml")

egp = soup.find_all("div", {"class": "YMlKec fxKbKc"})
us_egp = ""
number = ""

for i in egp:
    us_egp = i.text

for lis in us_egp:
    for num in lis:
        if num.isdecimal() or "." in num:
            number += num

egp_result = float(number)


def main():
    print("*" * 63)
    print("*This program converts US Dollar(USD) to Egyptian Pounds(EGP).*")
    print("*" * 63)

    # print("*" * (9 + len(str(egp_result))))
    print(f"* 1$ = {egp_result} *")
    print("*" * (9 + len(str(egp_result))))

    dollars = eval(input("Enter amount of dollars: "))
    egp_pounds = convert_to_egp(dollars)
    print(f"{dollars}$ to EGP is equal: {egp_pounds:.2f}")


convert_to_egp = lambda usd: usd * egp_result


main()
