from engine.duplicate_detector import DuplicateDetector
from engine.block_matcher import BlockMatcher

detector = DuplicateDetector()
matcher = BlockMatcher()

blocks = detector.split_into_blocks(
    r"C:\Users\Harrison Media\Documents\Bluetooth\Daily Pulpit Compiled.docx"
)

duplicates = matcher.find_duplicates(blocks)

print("=" * 70)
print(f"Blocks Found: {len(blocks)}")
print(f"Duplicates Found: {len(duplicates)}")
print("=" * 70)

for original, duplicate in duplicates:
    print(f"{duplicate} --> {original}")

print("\n")

# --------- INSPECT ANY BLOCK HERE ---------

inspect = [58, 60, 202, 203]

for number in inspect:

    print("\n")
    print("=" * 70)
    print(f"BLOCK {number}")
    print("=" * 70)

    block = blocks[number-1]

    for p in block:
        if p.text.strip():
            print(p.text)