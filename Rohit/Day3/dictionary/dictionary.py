helper = {
    "key":"value",


}
newhelper = dict(host = "db_server",port ="1106")
# print(newhelper.keys())
# print(newhelper.items())
usingList = list(newhelper)
# print(usingList[1])
newhelper.update(host="new Server")
newhelper["port"] ="2000"
# print(newhelper)
# print(newhelper.get("host"))
# orange_price = newhelper.get("port")
# print(orange_price)
#
# kiwi_price  = newhelper.get("kiwi")
# print(kiwi_price)
#
# kiwi_price  = newhelper.get("kiwi","Khatam tata bye bye")
# print(kiwi_price)

newhelper.update(kiwi= "new something")
print(newhelper)