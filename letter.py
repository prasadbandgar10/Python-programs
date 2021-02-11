letter=''' Dear <|name|> 
     you are selected
    <|date|> '''
letter=letter.replace("<|name|>","Prasad")
letter=letter.replace("<|date|>","14/02/2021")
print(letter)          