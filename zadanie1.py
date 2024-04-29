def count_hirsch(list_of_cites):
    #makes decending order of cites
    list_of_cites.sort(reverse = True)
    n = len(list_of_cites)
    h_index = 0
    for i in range(n):
        #finds hirsch index
        if list_of_cites[i] >= i:
            h_index = i
    h_index += 1
    return h_index

n = int(input("Write the number of articles: "))

articles = []
for i in range(n):
    cites = int(input("Insert number of cites for the article: "))
    articles.append(cites)

h = count_hirsch(articles)

print("Author's Hirsch index is: ",h)






