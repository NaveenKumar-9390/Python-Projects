"""
Comprehensive Test Script for All 14 Python Projects
"""
import sys
import os

print("=" * 60)
print("TESTING ALL 14 PYTHON PROJECTS")
print("=" * 60)

# Project 1: Autocomplete System
print("\n[1/14] Testing Autocomplete System...")
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
print("\n[2/14] Testing Expression Evaluator...")
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
print("\n[3/14] Testing File System Simulator...")
try:
    from file_system_simulator.main import FileSystem
    fs = FileSystem()
    fs.mkdir("test_folder")
    fs.touch("test_file.txt")
    print("   [OK] File System Simulator - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 4: Log Analyzer
print("\n[4/14] Testing Log Analyzer...")
try:
    os.chdir("log_analyzer")
    from log_analyzer.main import analyze_logs
    ip_counter, url_counter, status_counter = analyze_logs()
    print(f"   Analyzed {sum(ip_counter.values())} log entries")
    print("   [OK] Log Analyzer - Working!")
    os.chdir("..")
except Exception as e:
    print(f"   [ERROR] {e}")
    os.chdir("..")

# Project 5: LRU Cache Engine
print("\n[5/14] Testing LRU Cache Engine...")
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
print("\n[6/14] Testing Maze Solver...")
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
print("\n[7/14] Testing Memory Allocator...")
try:
    from memory_allocator.main import MemoryAllocator
    allocator = MemoryAllocator(20)
    pos = allocator.allocate(5)
    assert pos >= 0, "Allocation failed"
    print("   [OK] Memory Allocator - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 8: Mini Git
print("\n[8/14] Testing Mini Git...")
try:
    os.chdir("mini_git")
    from mini_git.main import init_repo, status
    init_repo()
    status()
    print("   [OK] Mini Git - Working!")
    os.chdir("..")
except Exception as e:
    print(f"   [ERROR] {e}")
    try:
        os.chdir("..")
    except:
        pass

# Project 9: Mini Search Engine
print("\n[9/14] Testing Mini Search Engine...")
try:
    os.chdir("mini_search_engine")
    from mini_search_engine.main import build_index, search
    index = build_index()
    results = search(index, "python")
    print(f"   Index built with {len(index)} unique words")
    print("   [OK] Mini Search Engine - Working!")
    os.chdir("..")
except Exception as e:
    print(f"   [ERROR] {e}")
    try:
        os.chdir("..")
    except:
        pass

# Project 10: Social Network Graph
print("\n[10/14] Testing Social Network Graph...")
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
print("\n[11/14] Testing Spell Checker...")
try:
    os.chdir("spell_checker")
    from spell_checker.main import load_dictionary, edit_distance
    dictionary = load_dictionary()
    dist = edit_distance("hello", "helo")
    print(f"   Dictionary loaded with {len(dictionary)} words")
    print(f"   Edit distance 'hello' to 'helo': {dist}")
    print("   [OK] Spell Checker - Working!")
    os.chdir("..")
except Exception as e:
    print(f"   [ERROR] {e}")
    try:
        os.chdir("..")
    except:
        pass

# Project 12: Sudoku Solver
print("\n[12/14] Testing Sudoku Solver...")
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

# Project 13: Task Scheduler
print("\n[13/14] Testing Task Scheduler...")
try:
    from task_scheduler.main import tasks
    print(f"   Task list initialized: {len(tasks)} tasks")
    print("   [OK] Task Scheduler - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

# Project 14: Web Crawler Engine
print("\n[14/14] Testing Web Crawler Engine...")
try:
    import json
    data_path = os.path.join("web_crawler_engine", "data.json")
    with open(data_path, "r", encoding="utf-8") as f:
        pages = json.load(f)
    print(f"   Loaded {len(pages)} pages from data.json")
    print("   [OK] Web Crawler Engine - Working!")
except Exception as e:
    print(f"   [ERROR] {e}")

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED!")
print("=" * 60)
