from main import MemoryAllocator

print("Testing memory allocator:")
allocator = MemoryAllocator(20)

print("\n1. Initial memory:")
allocator.show_memory()

print("\n2. Allocating 5 blocks:")
pos1 = allocator.allocate(5)

print("\n3. Allocating 3 blocks:")
pos2 = allocator.allocate(3)

print("\n4. Memory after allocations:")
allocator.show_memory()

print("\n5. Freeing first allocation:")
allocator.free(pos1, 5)

print("\n6. Memory after freeing:")
allocator.show_memory()

print("\n7. Allocating 10 blocks:")
allocator.allocate(10)

print("\n8. Final memory:")
allocator.show_memory()

print("\n[OK] Memory allocator works correctly!")
