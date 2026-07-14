from engine.duplicate_detector import DuplicateDetector

detector = DuplicateDetector()

blocks = detector.split_into_blocks(r"C:\Users\Harrison Media\Documents\Bluetooth\Daily Pulpit Compiled.docx")

print("Blocks found:", len(blocks))

for i, block in enumerate(blocks, start=1):

    if block:
        print(f"{i}: {block[0].text}")

    for p in block[:3]:
        print(p.text)