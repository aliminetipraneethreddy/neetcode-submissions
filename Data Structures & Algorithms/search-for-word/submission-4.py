class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l1=list(word)
        Flag=True
        for i in board:
            for j in i:
                if len(l1)==0:
                    return True
                if j in l1:
                    l1.remove(j)
        if len(l1)==0:
            return True
        else:
            return False


        