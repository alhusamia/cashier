def main():
        # write code her
    items = []
    done=True
    while done:
        name = input('Item (enter "done" when finished): ')
        if name.lower() == "done":
                print()
                print("-"*20)
                print("receipt")
                print("-"*20)
                for i in items:
                    print(str(i["quantity"]) + " " +i["name"]+" " +str(i["price"]*i["quantity"]))
                done = False
                

        else:
          price = float(input("Price: "))
          quantity = int(input("Quantity: "))
          dicts={"name":name,"price":price, "quantity":quantity}
          items.append(dicts)
        
      #  if name.lower() == "done":
      #      print()
      #      print("-"*20)
      #      print("receipt")
      #      print("-"*20)
      #      for i in item:
      #          print(str(i["quantity"]) + " " +i["name"]+" " +str(i["price"]*i["quantity"])



if __name__ == '__main__':
     main()

