
def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]






#def markdown_to_blocks(markdown):
    
 #   raw_blocks = markdown.split("\n\n")
  #  blocks = []
   # for block in raw_blocks:
    #    cleaned = block.strip()
     #   if cleaned !="":
      #      blocks.append(cleaned)
    #return blocks 


