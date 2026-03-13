import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from main import SocialNetwork

print("Testing social network graph:")

sn = SocialNetwork()

print("\n1. Adding users:")
sn.add_user("Alice")
sn.add_user("Bob")
sn.add_user("Charlie")
sn.add_user("David")

print("\n2. Adding friendships:")
sn.add_friend("Alice", "Bob")
sn.add_friend("Alice", "Charlie")
sn.add_friend("Bob", "Charlie")
sn.add_friend("Bob", "David")

print("\n3. Showing friends of Alice:")
sn.show_friends("Alice")

print("\n4. Finding mutual friends of Alice and Bob:")
sn.mutual_friends("Alice", "Bob")

print("\n5. Displaying network:")
sn.display_network()

print("\n[OK] Social network graph works correctly!")
