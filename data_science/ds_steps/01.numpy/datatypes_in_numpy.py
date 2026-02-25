import numpy as np

# 1. Create arrays with different dtypes
a = np.array([1, 2, 3, 4, 5], dtype=np.int64)
print("a:", a, "| dtype:", a.dtype)

# 2. Convert int → smaller int
b = a.astype(np.int8)
print("b:", b, "| dtype:", b.dtype)

# 3. Convert int → float
c = a.astype(np.float32)
print("c:", c, "| dtype:", c.dtype)

# 4. Convert float → int
floats = np.array([1.9, 2.8, 3.1], dtype=np.float32)
d = floats.astype(np.int16)
print("d:", d, "| dtype:", d.dtype)

# 5. Boolean dtype
bools = np.array([True, False, True], dtype=bool)
print("bools:", bools, "| dtype:", bools.dtype)

# 6. String dtype
names = np.array(["ram", "shyam", "sid"], dtype="U10")
print("names:", names, "| dtype:", names.dtype)

# 7. Complex dtype
comp = np.array([3+4j, 5+6j], dtype=np.complex128)
print("complex:", comp, "| dtype:", comp.dtype)

# 8. Auto-upcast
mix = np.array([1, 2.5, 3])
print("mix:", mix, "| dtype:", mix.dtype)

# 9. Check itemsize
print("int64 bytes:", a.itemsize)
print("int8  bytes:", b.itemsize)
print("float32 bytes:", c.itemsize)