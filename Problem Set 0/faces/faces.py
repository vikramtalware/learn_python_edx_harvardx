def main():
    icon = input()
    faces(icon)

def faces(emoji):
    print(emoji.replace(":)","🙂").replace(":(","🙁"))

main()
