from main import evaluate

print("Testing expression evaluator:")
print("2 + 3 * 4 =", evaluate("2 + 3 * 4"))
print("(2 + 3) * 4 =", evaluate("(2 + 3) * 4"))
print("10 - 2 * 3 =", evaluate("10 - 2 * 3"))
print("100 / 5 + 2 =", evaluate("100 / 5 + 2"))
print("[OK] Expression evaluator works correctly!")
