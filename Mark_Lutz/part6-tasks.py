# task #2
class MyList(list):
    data = None

    def __init__(self, list_object):
        super().__init__()
        if isinstance(list_object, list):
            self.data = list_object[:]
        else:
            self.data = list_object.data[:]

    def __repr__(self):
        return str(self.data)

    def __contains__(self, item):
        return True if item in self.data else False

    def __getitem__(self, index):
        return self.data[index]

    def __add__(self, other):
        self.add(other)
        return MyList(self.data)

    def __iadd__(self, other):
        self.add(other)
        return MyList(self.data)

    def __radd__(self, other):
        self.add(other)
        return MyList(self.data)

    def add(self, alist: list):
        self.data = self.data + alist

# task #3
class MyListSub(MyList):
    count_calls = 0
    def __init__(self, list_object):
        self.count_calls = 0
        MyList.__init__(self,list_object)
    def __add__(self, other):
        self.count_calls += 1
        print(f'Calls done: {self.count_calls}')
        MyList.add(self, other)
    def __repr__(self):
        __superstr = MyList.__repr__(self)
        return __superstr + f' "Add" calls done: {self.count_calls}'


# task #7 - FastFood Restaurant
class Lunch:
    def __init__(self):
        """
        instantiates Customer, Employee
        """
        self.customer = Customer()
        self.employee = Employee()
    def orderQueue(self, *args):
        """
        places orders for a customer
        :param args:
        :return:
        """
        for foodItem in args:
            self.order(foodItem)
    def order(self, foodName):
        """
        Customer buys foodName
        :param foodName:
        :return:
        """
        self.customer.placeOrder(foodName, self.employee)
    def result(self):
        """
        Customer asks for instance of food
        :return:
        """
        return self.customer.printFood()


class Customer:
    meal = None
    def __init__(self):
        """
        initializes meal
        """
        self.meal = []
    def placeOrder(self, foodName, employee):
        """
        places an order with employee instance
        :param foodName:
        :param employee:
        :return:
        """
        self.meal.append(employee.takeOrder(foodName))
    def printFood(self):
        """
        prints foodName
        :return:
        """
        return [item.foodName for item in self.meal]
    def __repr__(self):
        """
        debugging str
        :return:
        """
        return str([item.foodName for item in self.meal])

class Employee:
    processingQueue = None
    def __init__(self):
        """
        Queue for an employee
        """
        self.processingQueue = []
    def takeOrder(self, foodName):
        """
        returns Food instance with the given foodName
        :param foodName:
        :return:
        """
        self.processingQueue.append(Food(foodName))
        return self.processingQueue[-1]


class Food:
    foodName = None
    def __init__(self, foodName):
        """
        saves the foodName
        """
        self.foodName = foodName


# a = Lunch(); a.order("burito")
# a.orderQueue('nachos','cola','potatoes','sause','shawerma')
