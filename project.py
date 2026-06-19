from transaction import Transaction

# お金の収支に関する管理を行うクラス

class Project:
    def __init__(self,name):
        self.name=name
        self.transactions = []

    # 新しい履歴を追加する関数
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    # 履歴を削除する関数
    def remove_transaction(self, index):
        del self.transactions[index]


    # 収入の和を算出する関数
    def get_income_total(self):
        total = 0
        
        for transaction in self.transactions:
            if transaction.is_income():
                total += transaction.amount

        return total
    
    # 支出の和を算出する関数
    def get_expense_total(self):
        total = 0

        for transaction in self.transactions:
            if transaction.is_expense():
                total += transaction.amount

        return total
    
    # 収支を算出する関数
    def get_balance(self):
        return (self.get_income_total() - self.get_expense_total())
    


    def show_transactions(self):
        print(f"\n[{self.name}]")
        if len(self.transactions) == 0:
            print("取引は登録されていません。")
            return
        
        for transaction in self.transactions:
            print(transaction)



    def get_category_total(self,category):
        total = 0
        
        for transaction in self.transactions:
            if transaction.category == category:
                total += transaction.amount
        
        return total



    def categories(self):
        result_categories = []
        for transaction in self.transactions:
            if transaction.category not in result_categories:
                result_categories.append(transaction.category)

        return result_categories
        


    def get_transactions_by_category(self,category):
        result = []
        
        for transaction in self.transactions:
            if transaction.category == category:
                result.append(transaction)

        return result



    def find_transactions(self,category):
        print(f"\n[{self.name}]")
        if len(self.transactions) == 0:
            print("取引は登録されていません。")
            return
        
        for transaction in self.transactions:
            if transaction.category == category:
                print(transaction)
