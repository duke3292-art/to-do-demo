"""간단한 할 일 관리 모듈"""

class TodoList:
    def __init__(self):
        self.items = []

    def add(self, title):
        if not title.strip():
            raise ValueError("제목이 비어 있습니다")
        self.items.append({"title": title, "done": False})
        return len(self.items) - 1

    def complete(self, index):
        self.items[index]["done"] = True

    def delete(self, index):
        if not 0 <= index < len(self.items):
            raise ValueError(f"{index}번 항목이 없습니다")
        return self.items.pop(index)
