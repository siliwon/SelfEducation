parties = []
votes = []
list = []
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        list.append(line)


def parties_separator(list, parties):
    votes_index = list.index('VOTES:')
    for i in range(1, votes_index):
        parties.append(list[i])
    return parties


def votes_separator(list, votes):
    votes_index = list.index('VOTES:')
    for i in range(votes_index + 1, len(list)):
        votes.append(list[i])
    return votes


parties_separator(list, parties)
votes_separator(list, votes)


def calculation(parties, votes):
    common_votes_amount = len(votes)
    for i in parties:
        percent = votes.count(i)
        if int(percent / common_votes_amount * 100) >= 7:
            print(i, file=file)


with open('output.txt', 'w', encoding='utf8') as file:
    calculation(parties, votes)
