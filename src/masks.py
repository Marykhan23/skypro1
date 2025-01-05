def get_mask_card_number(card_number: str) -> str:
    """This function adds a mask for a card number"""
    mask_card_number = card_number.replace(card_number[6:12], "******")
    card_num_with_spaces = ""
    for i in range(0, len(mask_card_number), 4):
        card_num_with_spaces += mask_card_number[i: i + 4] + " "
    card_num_with_spaces = card_num_with_spaces[:-1]
    return card_num_with_spaces


def get_mask_account(account_number: str) -> str:
    """This function adds a mask for an account number"""
    mask_account_number = account_number[-4::]
    return "**" + mask_account_number


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
