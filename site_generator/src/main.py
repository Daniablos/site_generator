from textnode import TextNode, TextType

def main():
    print(TextNode("some test text", TextType.LINK, "https://www.google.com"))

if __name__ == "__main__":
    main()