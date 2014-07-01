# Tui Popenoe
# Challenge 167 HTML Markup Generator

"""Implementation creates an HTML wrapper for the input paragraph."""

def getInput():
    """Get the input paragraph to wrap in HTML."""
    print("Enter your paragraph: ")
    paragraph = raw_input()

    return paragraph

def createHTML():
    """Create an HTML wrapper for the given paragraph."""
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

