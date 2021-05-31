class Solution:
   def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
       res = []
       products.sort()
       for i, c in enumerate(searchWord):
            count, current = 0, []
            search = searchWord[:i+1]
            for prod in products:
                if search == prod[:i+1]:
                    current.append(prod)
                    count += 1
                if count == 3:
                   break
            res.append(current)
        return res
