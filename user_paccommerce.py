
from tabulate import tabulate

class User:
    data_user = {'Sumbul': 'Platinum',
                  'Ana': 'Gold', 
                  'Cahya': 'Platinum'}

    data_membership = [
        {
            "Membership": "Platinum",
            "Discount": 0.015,
            "Another Benefit": "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"
        },
        {
            "Membership": "Gold",
            "Discount": 0.01,
            "Another Benefit": "Benefit Silver + Voucher Ojek Online"
        },
        {
            "Membership": "Silver",
            "Discount": 0.08,
            "Another Benefit": "Voucher Makanan"
        }
    ]
    # Step 1: Extract headers
    headers_benefit = list(data_membership[0].keys())

    # Step 2: Extract content
    content_benefit = [list(member.values()) for member in data_membership]
    
    data_requirement = [
        {
            "Membership": "Platinum",
            "Expense" : 8,
            "Income" : 15
        },
        {
            "Membership": "Gold",
            "Expense" : 6,
            "Income" : 10
        },
        {
            "Membership": "Silver",
            "Expense" : 5,
            "Income" : 7
        }
    ]

    headers_requirement = list(x for x in data_requirement[0].keys())
    content_requirement = list(list(x.values()) for x in data_requirement)

    

    def __init__ (self,username):
        """
        Fungsi ini berperan untuk menginisiasi objek user

        input: username (str)
        """
        self.username = username
        self.expense = None
        self.income = None
        self.membership = None

    def show_benefit(self):
        """
        Fungsi ini digunakan untuk mencetak semua benefit

        input: None
        """
        print("List of available plans and benefits")
        print("")
        table = tabulate(self.content_benefit, headers=self.headers_benefit,tablefmt='simple') # , tablefmt="grid"
        print(table)
    
    def show_requirements(self):
        """
        Fungsi ini digunakan untuk mencetak requirement untuk mencapai benefit tier tertentu

        input: None
        """
        print("Detail requirement based on membership tier")
        print("")
        table = tabulate(self.content_requirement, headers=self.headers_requirement,tablefmt='simple')
        print(table)

    def predict_membership(self, expense,income):
        """
        Fungsi ini bertujuan untuk predict customer membership tier berdasar their income and expense

        input: 
        - username(str)
        - expense(int)
        - income(int)
        """
        # self.username = username
        self.income = income
        self.expense = expense

        r = 0
        final_result = []
        for i in self.__class__.data_requirement:
            expense_threshold = i['Expense']
            income_threshold = i['Income']
            r = ((expense_threshold - self.expense)**2 + (income_threshold - self.income)**2)**0.5

            result = {i['Membership']: r}
            final_result.append(result)
        
        # self.membership = None
        init_val = 0
        for i in final_result:
            value = list(i.values())[0] # ngambil dari dictionary -- convert ke list (isinya 1 nilai doang) -- kemudian ambil yang ke 0
            key = list(i.keys())[0] # ngambil dari dictionary -- convert ke list (isinya 1 nilai doang) -- kemudian ambil yang ke 0
            if init_val < value:
                self.membership = key
            else:
                pass
        print(self.membership)
    
    def calculate_price(self,membership, list_harga_barang):
        # self.membership = membership
        for i in self.__class__.data_membership:
            if i['Membership'] == membership:
                total_harga = sum(list_harga_barang) * (1-i['Discount'])
        
        print(total_harga)

                    # harga_barang = barang * (1-i['Discount'])
        # for i in list_harga_barang:

