from collections import deque

audio_queue = deque()

for minute in range(1, 6):

    # Audio capture produces 50 segments
    for segment in range(50):
        audio_queue.append(
            f"{minute}-{segment + 1}"
        )

    # Two recognition workers
    for worker in range(2):

        # Each worker processes 20 segments
        for _ in range(20):

            if audio_queue:
                audio_queue.popleft()

    print(f"Minute {minute}: {len(audio_queue)} waiting")


