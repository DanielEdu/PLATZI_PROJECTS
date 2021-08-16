
def palindrome(text):
    try:
        if len(text) == 0:
            raise ValueError("Error: empty text")
        return text == text[::-1]
    except ValueError as ve:
        print(ve)
        return False



def run():
    text = ''  #'anna'
    try:
        print(palindrome(text))
    except TypeError:
        print("only string, not integers")



if __name__ == '__main__':
    run()