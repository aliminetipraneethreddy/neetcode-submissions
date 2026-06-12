class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l1=list(word)
        Flag=True
        for i in board:
            for j in i:
                if not l1:
                    return True
                if j in l1:
                    l1.remove(j)
        return len(l1)==0

        