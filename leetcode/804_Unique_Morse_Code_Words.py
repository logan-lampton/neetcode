def uniqueMorseRepresentations(self, words: List[str]) -> int:
    
    morse=dict(zip("abcdefghijklmnopqrstuvwxyz",[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))

    s = set()

    for word in words:
        code = ''
        for letter in word:
            code += morse.get(letter)
        s.add(code)
    
    return len(s)