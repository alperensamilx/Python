from pprint import pprint

message ='''
Yet each man kills the thing he loves
By each let this be heard,
Some do it with a bitter look,
Some with a flattering word,
The coward does it with a kiss,
The brave man with a sword!

Some kill their love when they are young,
And some when they are old;
Some strangle with the hands of Lust,
Some with the hands of Gold:
The kindest use a knife, because
The dead so soon grow cold.

Some love too little, some too long,
Some sell, and others buy;
Some do the deed with many tears,
And some without a sigh:
For each man kills the thing he loves,
Yet each man does not die.

Oscar Wilde
'''
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] +=1

pprint(count)
