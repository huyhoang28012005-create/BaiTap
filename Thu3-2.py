### 5.1 #######################################
# Quản lý Sách
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def display_info(self):
        print(f" Tên sách:{self.title}")
        print(f"   Tác giả: {self.author}")
        print(f"   Năm XB: {self.year}")
        print("-" * 30)

book1 = Book("Harry Potter", "J.K. Rowling", 1997)
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
book1.display_info()
book2.display_info()


# Quản lý tài khoản ngân hàng
class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number 
        self.balance = balance
        
    @property
    def account_number(self):
        return self._account_number
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Đã nạp: {amount}. Số dư mới: {self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Đã rút: {amount}. Số dư mới: {self.balance}")
        else:
            print("Lỗi: Số dư không đủ để thực hiện giao dịch!")
            
    def get_balance(self):
        return self.balance

my_account = BankAccount("VN123456789", 10000)
print(f"Số tài khoản của bạn là: {my_account.account_number}")
my_account.deposit(500)      
my_account.withdraw(200)     
my_account.withdraw(5000)    

print(f"Số dư cuối ngày: {my_account.get_balance()}")



# Kế thừa trong OOP
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) 
        self.student_id = student_id
        
    def study(self):
        print(f"Sinh viên {self.name} (Mã số: {self.student_id}) đang học bài.")

sinh_vien_1 = Student("Hoang", 20, "SV2023")

print(f"Tên: {sinh_vien_1.name}, Tuổi: {sinh_vien_1.age}")
sinh_vien_1.study()



# Quản lý phương tiện giao thông
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"[{self.brand} {self.model} ({self.year})]", end="")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.num_doors = doors
        
    def display_info(self):
        super().display_info() 
        print(f" - Loại: Ô tô, {self.num_doors} cửa")

class Bike(Vehicle):
    def __init__(self, brand, model, year, btype):
        super().__init__(brand, model, year)
        self.type = btype
        
    def display_info(self):
        super().display_info() 
        print(f" - Loại: Xe đạp {self.type}")

car = Car("Toyota", "Camry", 2024, 4)
bike = Bike("Giant", "XTC", 2023, "mountain")

for v in [car, bike]:
    v.display_info()



### 5.2 ########################################


# Tạo danh sách các số lẻ từ 1 đến 20
so_le = [x for x in range(1, 21) if x % 2 != 0]
print(so_le)
# Tạo danh sách các chuỗi "Hello" lặp lại 5 lần
hello_list = ["Hello" for _ in range(5)]
print(hello_list)
# Tạo generator chứa các số chia hết cho 3 từ 0 đến 15
gen = (x for x in range(16) if x % 3 == 0)
# Sử dụng next() để lấy 2 giá trị đầu tiên
print("Giá trị thứ nhất:", next(gen)) 
print("Giá trị thứ hai:", next(gen))  


# BÀI 1: Vẽ đồ thị đơn giản với matplotlib 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Plot")
plt.show()

# BÀI 2: List Comprehension (chia hết cho 3 và 5)
numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(numbers)


# BÀI 3: Generator( số nguyên tố từ 1 → 20 )
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

gen_nguyen_to = (x for x in range(1, 21) if la_so_nguyen_to(x))

print("Số nguyên tố thứ nhất:", next(gen_nguyen_to)) 
print("Số nguyên tố thứ hai:", next(gen_nguyen_to))  
print("Số nguyên tố thứ ba:", next(gen_nguyen_to))   
