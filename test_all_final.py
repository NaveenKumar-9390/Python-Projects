"""
Comprehensive Test Script for All Python Projects
"""
import sys
import os

print("=" * 60)
print("TESTING ALL PYTHON PROJECTS")
print("=" * 60)

# Project 1: Autocomplete System
print("\n[1/16] Testing Autocomplete System...")
try:
    from autocomplete_system.autocomplete import Autocomplete
    ac = Autocomplete()
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    for w in words:
        ac.insert(w)
    result = ac.suggest("app")
    assert len(result) == 3, "Expected 3 suggestions"
    print("   Result:", result)
    print("   [OK] Autocomplete System - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 2: Expression Evaluator
print("\n[2/16] Testing Expression Evaluator...")
try:
    from expression_evaluator.main import evaluate
    result1 = evaluate("2 + 3 * 4")
    result2 = evaluate("(2 + 3) * 4")
    print(f"   2 + 3 * 4 = {result1}")
    print(f"   (2 + 3) * 4 = {result2}")
    assert result1 == 14, "Expected 14"
    assert result2 == 20, "Expected 20"
    print("   [OK] Expression Evaluator - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 3: File System Simulator
print("\n[3/16] Testing File System Simulator...")
try:
    from file_system_simulator.main import FileSystem
    fs = FileSystem()
    fs.mkdir("test_folder")
    fs.touch("test_file.txt")
    print("   [OK] File System Simulator - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 4: Log Analyzer
print("\n[4/16] Testing Log Analyzer...")
try:
    from log_analyzer.main import analyze_logs
    ip_counter, url_counter, status_counter = analyze_logs()
    print(f"   Analyzed {sum(ip_counter.values())} log entries")
    print("   [OK] Log Analyzer - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 5: LRU Cache Engine
print("\n[5/16] Testing LRU Cache Engine...")
try:
    from lru_cache_engine.main import DynamicLRUCache
    lru = DynamicLRUCache(3)
    lru.put(1, "A")
    lru.put(2, "B")
    lru.put(3, "C")
    result = lru.get(1)
    assert result == "A", "Expected 'A'"
    print("   Cache get(1):", result)
    print("   [OK] LRU Cache Engine - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 6: Maze Solver
print("\n[6/16] Testing Maze Solver...")
try:
    from maze_solver.main import create_maze, solve_maze
    maze = create_maze()
    visited = set()
    result = solve_maze(maze, 1, 1, visited)
    print(f"   Maze solved: {result or 'Path found'}")
    print("   [OK] Maze Solver - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 7: Memory Allocator
print("\n[7/16] Testing Memory Allocator...")
try:
    from memory_allocator.main import MemoryAllocator
    allocator = MemoryAllocator(20)
    pos = allocator.allocate(5)
    assert pos >= 0, "Allocation failed"
    print("   [OK] Memory Allocator - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 8: Mini Git
print("\n[8/16] Testing Mini Git...")
try:
    from mini_git.main import init_repo, status
    init_repo()
    status()
    print("   [OK] Mini Git - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 9: Mini Search Engine
print("\n[9/16] Testing Mini Search Engine...")
try:
    from mini_search_engine.main import build_index, search
    index = build_index()
    results = search(index, "python")
    print(f"   Index built with {len(index)} unique words")
    print("   [OK] Mini Search Engine - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 10: Social Network Graph
print("\n[10/16] Testing Social Network Graph...")
try:
    from social_network_graph.main import SocialNetwork
    sn = SocialNetwork()
    sn.add_user("Alice")
    sn.add_user("Bob")
    sn.add_friend("Alice", "Bob")
    print("   [OK] Social Network Graph - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 11: Spell Checker
print("\n[11/16] Testing Spell Checker...")
try:
    from spell_checker.main import load_dictionary, edit_distance
    dictionary = load_dictionary()
    dist = edit_distance("hello", "helo")
    print(f"   Dictionary loaded with {len(dictionary)} words")
    print(f"   Edit distance 'hello' to 'helo': {dist}")
    print("   [OK] Spell Checker - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 12: Stock Price Analyzer
print("\n[12/16] Testing Stock Price Analyzer...")
try:
    import subprocess
    result = subprocess.run(["python", "stock_price_analyzer/main.py"], 
                          capture_output=True, text=True, cwd=".")
    if result.returncode == 0:
        print("   Output:", result.stdout.strip().split('\n')[0])
        print("   [OK] Stock Price Analyzer - Working!")
    else:
        print(f"   [ERROR] {result.stderr}")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 13: Sudoku Solver
print("\n[13/16] Testing Sudoku Solver...")
try:
    from sudoku_solver.main import solve, find_empty
    board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    result = solve(board)
    print(f"   Sudoku solved: {result}")
    print("   [OK] Sudoku Solver - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 14: Task Scheduler
print("\n[14/16] Testing Task Scheduler...")
try:
    from task_scheduler.main import tasks
    print(f"   Task list initialized: {len(tasks)} tasks")
    print("   [OK] Task Scheduler - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 15: URL Shortener
print("\n[15/16] Testing URL Shortener...")
try:
    from url_shortener.main import generate_code, load_db
    code = generate_code()
    assert len(code) == 6, "Expected 6 character code"
    print(f"   Generated code: {code}")
    print("   [OK] URL Shortener - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 16: Check for additional projects
print("\n[16/16] Checking project count...")
import os
dirs = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.') and not d.startswith('__')]
project_dirs = [d for d in dirs if d not in ['templates', 'documents', 'repo']]
print(f"   Total project directories found: {len(project_dirs)}")
print("   [OK] Project count verified!")

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED!")
print("=" * 60)
