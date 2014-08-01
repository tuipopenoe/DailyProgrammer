# Tui Popenoe
# Challenge 167 HTML Markup Generator

class HTMLMarkupGenerator():
    """Class to create an HTML wrapper for an input paragraph."""
    def get_input(self):
        """Get the input paragraph to wrap in HTML."""
        print("Enter your paragraph: ")
        paragraph = raw_input()
        return paragraph

    def create_html(self):
        """Create an HTML wrapper for the given paragraph."""
        f = open('index.html', 'w')

        output = """<!DOCTYPE html>
                        <html>
                            <head>
                                <link rel='stylesheet'
            href='//maxcdn.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css' 
                                <title></title>
                            </head>
                            <body>
                            </body>
                                <p>""" + self.get_input() + \
                """             </p>
                            </body>
                        </html>"""
        f.write(output)
        f.close()
        print(output)
        return output

    def main():
        create_html()

class TestHTMLMarkupGenerator():
    """
    Unit tests for the HTMLMarkupGenerator class
    """
    def setUp(self):
        """
        Setup variables for the unit tests
        """
        pass

    def test_get_input(self):
        """
        Test HTMLMarkupGenerator get_input method
        """
        pass

    def test_create_html(self):
        """
        Test HTMLMarkupGenerator create_html method
        """
        pass



if __name__ == "__main__":
    if len(sys.argv) == 1:
        unittest.main()
    else:
        HTMLMarkupGenerator.main

