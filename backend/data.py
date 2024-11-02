import json
import os

class Record:
    def __init__(self, id, date, amount, category, note):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category
        self.note = note

    def to_dict(self):
        """将记录对象转换为字典"""
        return {
            "id": self.id,
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "note": self.note
        }

    @staticmethod
    def from_dict(data):
        """从字典创建一个记录对象"""
        return Record(
            id=data.get("id"),
            date=data.get("date"),
            amount=data.get("amount"),
            category=data.get("category"),
            note=data.get("note")
        )

    def __repr__(self):
        """定义对象的字符串表示形式，便于调试"""
        return f"Record(id={self.id}, date='{self.date}', amount={self.amount}, category='{self.category}', note='{self.note}')"

def load_records(filename='data/records.json'):
    """从JSON文件加载所有记录"""
    records = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data.get("records", []):
                # 假设Record类存在，可以直接用它创建记录对象
                record = Record(
                    id=item.get("id"),
                    date=item.get("date"),
                    amount=item.get("amount"),
                    category=item.get("category"),
                    note=item.get("note")
                )
                records.append(record)
    return records