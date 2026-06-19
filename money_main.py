"""
ユーザー_user
    アカウント id
        google google_id
        ユーザ名 user_name

        プロジェクト project
            イベントOR月 event_type
                日付
                    初日から最終日の日付
                        出費 expense
                            金額
                            理由
                        収入 income
                            LP work_income
                                開始時間 start
                                終了時間 up
                            その他 other_income
"""
from datetime import date

from project import Project
from transaction import Transaction
from transaction import TransactionType

def main():
    june = Project("2026/6")

    june.add_transaction(
        Transaction(
            transaction_date = date(2026,6,1),
            amount = 50000,
            transaction_type = TransactionType.INCOME,
            category = "LP",
            memo = "アルバイト"
        )
    )

    june.add_transaction(
        Transaction(
            transaction_date = date(2026,6,2),
            amount = 8000,
            transaction_type = TransactionType.EXPENSE,
            category = "チケット代",
            memo = "Wishing Umbrella"
        )
    )

    june.show_transactions()


if __name__ =="__main__":
    main()