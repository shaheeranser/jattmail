from jattmail import JattMail

def main() -> int:
    smtp = JattMail()
    smtp.run()
    return 0

if __name__ == "__main__":
    exit(main())