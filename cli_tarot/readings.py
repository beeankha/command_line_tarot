import time


def single_card_reading(card_list):
    time.sleep(1)
    print(f"\nāØ Your single card drawing is: āØ")
    time.sleep(1.5)
    print(*card_list, sep = "\n")


def seen_heard_held(card_list):
    time.sleep(1)
    print(f"\nš To Be Seen š\n{card_list[0]}")
    time.sleep(1.5)
    print(f"\nš To Be Heard š\n{card_list[1]}")
    time.sleep(1.5)
    print(f"\nš« To Be Held š«\n{card_list[2]}")
    time.sleep(1.5)
    print(f"\nš« Action š«\n{card_list[3]}")
    time.sleep(1)
