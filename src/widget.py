import masks as masks

def mask_account_card(number: str) -> str:
    res = ""
    for i in number.split(" "):
        if i.isdigit():
            if len(i) == 20:
                i = masks.get_mask_account(i)
            elif len(i) == 16:
                i = masks.get_mask_card_number(i)
        res += i + " "
    res = res[:-1]
    return res

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Visa Gold 5999414228426353"))



