from dataclasses import dataclass, asdict, field
from typing import List, Optional, Dict
import json
import uuid
import datetime

@dataclass
class Book:
    id: str
    title: str
    author: str
    year: int
    copies: int = 1

    def to_dict(self):
        return asdict(self)

@dataclass
class Member:
    id: str
    name: str
    email: str
    joined: str

    def to_dict(self):
        return asdict(self)

@dataclass
class Loan:
    id: str
    book_id: str
    member_id: str
    borrowed_on: str
    due_on: str
    returned_on: Optional[str] = None

    def to_dict(self):
        return asdict(self)

class Library:
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}
        self.loans: Dict[str, Loan] = {}

    def add(self, title: str, author: str, year: int, copies: int = 1) -> Book:
        book_id = str(uuid.uuid4())
        book = Book(id=book_id, title=title, author=author, year=year, copies=copies)
        self.books[book_id] = book
        return book

    def remove(self, book_id: str) -> bool:
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

    def update(self, book_id: str, copies: int) -> bool:
        book = self.books.get(book_id)
        if book:
            book.copies = copies
            return True
        return False

    def search_books(self, query: str) -> List[Book]:
        q = query.lower()
        return [b for b in self.books.values() if q in b.title.lower() or q in b.author.lower()]

    def memberadd(self, name: str, email: str) -> Member:
        member_id = str(uuid.uuid4())
        joined = datetime.date.today().isoformat()
        member = Member(id=member_id, name=name, email=email, joined=joined)
        self.members[member_id] = member
        return member

    def remove_member(self, member_id: str) -> bool:
        if member_id in self.members:
            del self.members[member_id]
            return True
        return False

    def borrow_book(self, book_id: str, member_id: str, days: int = 14) -> Optional[Loan]:
        book = self.books.get(book_id)
        member = self.members.get(member_id)
        if not book or not member:
            return None
        active_loans = [l for l in self.loans.values() if l.book_id == book_id and l.returned_on is None]
        available = book.copies - len(active_loans)
        if available <= 0:
            return None
        loan_id = str(uuid.uuid4())
        borrowed_on = datetime.date.today()
        due_on = borrowed_on + datetime.timedelta(days=days)
        loan = Loan(id=loan_id, book_id=book_id, member_id=member_id, borrowed_on=borrowed_on.isoformat(), due_on=due_on.isoformat())
        self.loans[loan_id] = loan
        return loan

    def return_book(self, loan_id: str) -> bool:
        loan = self.loans.get(loan_id)
        if loan and loan.returned_on is None:
            loan.returned_on = datetime.date.today().isoformat()
            return True
        return False

    def list_overdue(self) -> List[Loan]:
        today = datetime.date.today()
        overdue = []
        for loan in self.loans.values():
            if loan.returned_on is None:
                due = datetime.date.fromisoformat(loan.due_on)
                if due < today:
                    overdue.append(loan)
        return overdue

    def to_dict(self):
        return {
            "books": [b.to_dict() for b in self.books.values()],
            "members": [m.to_dict() for m in self.members.values()],
            "loans": [l.to_dict() for l in self.loans.values()]
        }

    def save_to_json(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)

    def load_from_json(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.books = {b["id"]: Book(**b) for b in data.get("books", [])}
        self.members = {m["id"]: Member(**m) for m in data.get("members", [])}
        self.loans = {l["id"]: Loan(**l) for l in data.get("loans", [])}

def listbooks(books: List[Book]):
    if not books:
        print("No books found")
        return
    for b in books:
        print(f"{b.id} | {b.title} | {b.author} | {b.year} | copies: {b.copies}")

def listmembers(members: List[Member]):
    if not members:
        print("No members")
        return
    for m in members:
        print(f"{m.id} | {m.name} | {m.email} | joined: {m.joined}")

def listloans(loans: List[Loan]):
    if not loans:
        print("No loans")
        return
    for l in loans:
        print(f"{l.id} | book: {l.book_id} | member: {l.member_id} | borrowed: {l.borrowed_on} | due: {l.due_on} | returned: {l.returned_on}")

def main():
    lib = Library()
    while True:
        print("1. Add book")
        print("2. Remove book")
        print("3. Search books")
        print("4. Add member")
        print("5. Borrow book")
        print("6. Return book")
        print("7. List overdue")
        print("8. Export to JSON")
        print("9. Import from JSON")
        print("10. List books")
        print("11. List members")
        print("12. List loans")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            year = int(input("Year: ").strip())
            copies = int(input("Copies: ").strip() or "1")
            b = lib.add(title, author, year, copies)
            print(f"Added book {b.id}")
        elif choice == "2":
            bid = input("Book ID: ").strip()
            ok = lib.remove(bid)
            print("Removed" if ok else "Not found")
        elif choice == "3":
            q = input("Query: ").strip()
            res = lib.search_books(q)
            listbooks(res)
        elif choice == "4":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            m = lib.memberadd(name, email)
            print(f"Added member {m.id}")
        elif choice == "5":
            bid = input("Book ID: ").strip()
            mid = input("Member ID: ").strip()
            days = int(input("Days (default 14): ").strip() or "14")
            loan = lib.borrow_book(bid, mid, days)
            print(f"Loan created {loan.id}" if loan else "Cannot borrow")
        elif choice == "6":
            lid = input("Loan ID: ").strip()
            ok = lib.return_book(lid)
            print("Returned" if ok else "Invalid loan")
        elif choice == "7":
            overdue = lib.list_overdue()
            listloans(overdue)
        elif choice == "8":
            path = input("Path to export (e.g. library.json): ").strip()
            lib.save_to_json(path)
            print(f"Exported to {path}")
        elif choice == "9":
            path = input("Path to import: ").strip()
            try:
                lib.load_from_json(path)
                print("Imported")
            except Exception as e:
                print(f"Failed to import: {e}")
        elif choice == "10":
            listbooks(list(lib.books.values()))
        elif choice == "11":
            listmembers(list(lib.members.values()))
        elif choice == "12":
            listloans(list(lib.loans.values()))
        elif choice == "0":
            break
        else:
            print("Unknown option")

if __name__ == "__main__":
    main()
