#codewars.com 
#problem 15
#bekmuxtorov
#tocamelcase

def tocamelcase(string: str) -> str:
    return string.title().replace(' ', '')


string = "hello world"
print(tocamelcase(string))