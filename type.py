# 1
def add(x: int, y: int) -> int:
    return x + y

# 2.list

numbers: list[int] = [1, 2, 3, 4]
names: list[str] = ["Ali", "Rafi"]

# 3.dist
user_scores: dict[str, int] = {"Ali": 95, "Rafi": 88}

# string | number)

id_code: str | int = 101
id_code = "A101" 

# func
def greet(name: str) -> None:
    print(f"Hello {name}")

