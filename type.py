# 1
def add(x: int, y: int) -> int:
    return x + y

# 2
# ১. শুধু সংখ্যা বা স্ট্রং-এর লিস্ট (TS-এর number[] বা string[])
numbers: list[int] = [1, 2, 3, 4]
names: list[str] = ["Ali", "Rafi"]

# ২. ডিকশনারি (TS-এর Record<string, number> বা Object)
# এখানে Key হবে string এবং Value হবে int
user_scores: dict[str, int] = {"Ali": 95, "Rafi": 88}

# ৩. একাধিক টাইপ সাপোর্ট করা বা Union Type (TS-এর string | number)
# পাইথনে এর জন্য পাইপ `|` সিম্বল ব্যবহার করা হয়
id_code: str | int = 101
id_code = "A101" # দুটিই সঠিক

# ৪. কোনো কিছু রিটার্ন না করলে (TS-এর void)
def greet(name: str) -> None:
    print(f"Hello {name}")

