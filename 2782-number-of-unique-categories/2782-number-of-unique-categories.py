# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass

class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        categories = [0]

        for i in range(1, n):
            for category in categories:
                if categoryHandler.haveSameCategory(category, i):
                    break
            else:
                categories.append(i)

        return len(categories)
