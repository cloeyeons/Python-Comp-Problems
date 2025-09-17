def clean(address):

    at_index = address.find("@")
    local = address[:at_index]
    domain = address[at_index:]
    plus_index = local.find("+")

    if at_index == -1:
        return address.lower()

    if plus_index != -1:
        local = local[:plus_index]
        
    local = local.replace(".", "")
    
    cleaned_address = local + domain
    cleaned_address = cleaned_address.lower()

    return cleaned_address

for dataset in range(10):
    n = int(input())
    emails = set()
    for i in range(n):
        address = input()
        cleaned = clean(address)
        emails.add(cleaned)
    print(len(emails))
