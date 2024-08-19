import re
from prettytable.colortable import ColorTable, Themes

class Alex:
    def __init__(self, code):
        self.__code = code
        
        self.__token_patterns = [        

            ('AND', r'and'),                        
            ('OR', r'or'),                          
            ('NOT', r'not'),                        
            ('AS', r'as'),                          
            ('ASSERT', r'assert'),                  
            ('BREAK', r'break'),                  
            ('CLASS', r'class'),                    
            ('CONTINUE', r'continue'),              
            ('DEL', r'del'),                        
            ('ELIF', r'elif'),                      
            ('ELSE', r'else'),                      
            ('EXCEPT', r'except'),                  
            ('FINALLY', r'finally'),                
            ('FOR', r'for'),                        
            ('FROM', r'from'),                      
            ('GLOBAL', r'global'),                  
            ('IF', r'if'),                          
            ('IMPORT', r'import'),                  
            ('IN', r'in'),                          
            ('IS', r'is'),                          
            ('LAMBDA', r'lambda'),                  
            ('NONE', r'None'),                      
            ('NONLOCAL', r'nonlocal'),              
            ('PASS', r'pass'),                      
            ('RAISE', r'raise'),                    
            ('RETURN', r'return'),                  
            ('TRY', r'try'),                        
            ('WHILE', r'while'),                    
            ('WITH', r'with'),                      
            ('SELF', r'self'),                    
            ('ASSIGN', r'=='),                      
            ('NOT_EQUALS', r'!='),                  
            ('GREATER_THAN', r'>'),                 
            ('LESS_THAN', r'<'),                    
            ('GREATER_OR_EQUAL', r'>='),            
            ('LESS_OR_EQUAL', r'<='),               
            ('EQUALS', r'='),                       
            ('INCREMENT', r'\+\+'),                 
            ('DECREMENT', r'--'),                   
            ('TRUE', r'True'),                      
            ('FALSE', r'False'),                    
            ('DEF', r'def'),                 
            ('L_DICT', r'\{'),                  
            ('SUPER', r'super'),                  
            ('R_DICT', r'\}'),                 
            ('EXPONENT', r'\*\*'),                  
            ('AT', r'@'),                           
            ('COLON', r':'),                        
            ('COMMA', r','),                        
            ('SEMI_COLON', r';'),                   

            ('NUMERO', r'\d+'),                      
            ('IDENTIFICADOR', r'[A-Za-z]\w*'),       
            ('SUMA', r'\+'),                         
            ('RESTA', r'-'),                         
            ('MULTIPLICACION', r'\*'),               
            ('DIVISION', r'/'),                      
            ('PARENTESIS_IZQ', r'\('),               
            ('PARENTESIS_DER', r'\)'),               
            ('ESPACIO', r'\s+'),                     
            ('SIMBOLO', r'.'),                       


        ]

        self.__token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.__token_patterns)

        self.__get_token = re.compile(self.__token_regex).match


    def __tokenize(self):
        line_number = 0
        position = 0
        tokens =  ColorTable(theme=Themes.OCEAN)
        tokens.field_names = ['No.', 'Token', 'Lexema']

        while position < len(self.__code):
            match = self.__get_token(self.__code, position)
        
            if not match:
                raise RuntimeError(f'Error de analisis en posición {position}')

            for name, value in match.groupdict().items():
                if value:
                    if name != 'ESPACIO':
                        line_number += 1
                        tokens.add_row([line_number, name, value])
                    break
            position = match.end()
        
        return tokens



    def run(self):
        tkns = self.__tokenize()
        print(tkns)

texto = "{} True False super  self if x > 10 and y < 5 or z == 3 not is None from import assert as class continue break lambda yield with try except finally pass raise return while global nonlocal def for in is == != > < >= <= = ++ -- & | ^ ~ << >> ** @ : , ;"
alex = Alex(texto)
alex.run()
        