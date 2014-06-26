# Tui Popenoe
# Challenge 167 HTML Markup Generator

def getInput():
    print("Enter your paragraph: ")
    paragraph = raw_input()

    return paragraph

def createHTML():
    f = open('index.html', 'w')

    output ="""<!DOCTYPE html>
                    <html>
                        <head>
                            <link rel='stylesheet'
        href='//maxcdn.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css' 
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

