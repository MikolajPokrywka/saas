import re
from tika import parser # pip install tika


# nazwy sprzedawcy,
# jego numeru NIP
# kwoty łącznej brutto faktury.

def extract(path):
    raw = parser.from_file(path)

    lines = raw['content'].split('\n')
    print('pdf, lines', lines)

    sales_name = ''
    nip = ''
    cost_brutto = ''
    for index, line in enumerate(lines):
        if 'Sprzedawca' in line:
            if index != len(lines):
                sales_name = lines[index + 1]

        if 'NIP' in line and nip == '':
            nip_prob = re.search(r"\d+", str(line))
            if nip_prob:
                nip = nip_prob.group()
        if 'Razem:' in line:
            cost_brutto_prob = re.findall(r"[0-9,.]+", str(line))
            if cost_brutto_prob:
                cost_brutto = cost_brutto_prob[-1]
    return sales_name, nip, cost_brutto