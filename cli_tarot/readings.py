import time


def single_card_reading(card_list):
    time.sleep(1)
    print(f"\n✨ Your single card drawing is: ✨")
    time.sleep(1.5)
    print(*card_list, sep = "\n")


def seen_heard_held(card_list):
    time.sleep(1)
    print(f"\n👁 To Be Seen 👁\n{card_list[0]}")
    time.sleep(1.5)
    print(f"\n👂 To Be Heard 👂\n{card_list[1]}")
    time.sleep(1.5)
    print(f"\n🫂 To Be Held 🫂\n{card_list[2]}")
    time.sleep(1.5)
    print(f"\n💫 Action 💫\n{card_list[3]}")
    time.sleep(1)


def past_present_future(card_list):
    time.sleep(1)
    print(f"\nPast\n{card_list[0]}")
    time.sleep(1.5)
    print(f"\nPresemt\n{card_list[1]}")
    time.sleep(1.5)
    print(f"\nFuture\n{card_list[2]}")
    time.sleep(1)
