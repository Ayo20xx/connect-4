class Gamestate:
    def __init__(self):
            self.board=[]
            for i in ["A","B","C","D","E","F","G",]:
                for x in [1,2,3,4,5,6]:
                    if i!= x:
                        self.board.append((i,x))


            self.redTomove = True
            
