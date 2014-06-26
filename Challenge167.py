# Tui Popenoe
# Challenge 167

def getInput():
    print("Enter your paragraph: ")
    paragraph = raw_input()

    return paragraph

def createHTML():
    f = open('index.html', 'w')

    output ="""<!DOCTYPE html>
                    <html>
                        <head>
                            <title></title>
                        </head>
                        <body>
                        </body>
                            <p>""" + getInput() + \
            """             </p>
                        </body>
                    </html>"""
    f.write(output)
    f.close()
    print(output)
    return output

def main():
    createHTML()

if __name__ == "__main__":
    main()

