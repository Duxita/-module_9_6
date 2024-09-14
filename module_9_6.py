
def all_variants(text):

    for i in text:
        yield i
    for k in range(len(text)-1):
        yield text[k] + text[k+1]

    for j in text:
        yield text
        break
a = all_variants("abc")
for i in a:
    print(i)