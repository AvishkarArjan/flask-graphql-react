from ariadne import QueryType, MutationType
from uuid import uuid4
# we use uuid4 to automatically generate an ID for each coffee order

query = QueryType()
mutation = MutationType()

orders=[]

class Coffee:
   def __init__(self, size, name, coffee_type):
       self.size = size
       self.name = name
       self.type = coffee_type
       self.id = uuid4()

@query.field("orders")
def resolve_orders(_, info):
    return orders

@mutation.field("orderCoffee")
def resolve_hello(_, info, size, name, type):
    newOrder = Coffee(size, name, type)
    orders.append(newOrder)
    print(f"[*] NEW ORDER {newOrder.id}")
    return newOrder

@mutation.field("delCoffee")
def resolve_del(_,info,order_id):
    print(order_id)
    for order in orders:
        print(order.id)
        
        if str(order.id) == order_id:
            del_order=order
            orders.remove(order)
            break
           
    return del_order

@mutation.field("updateCoffee")
def resolve_update(_,info,order_id,name,size,type):
    for order in orders:
        if str(order.id) == order_id:
            _order=order
            order.name = name
            order.size = size
            order.type = type
            break
    return _order

