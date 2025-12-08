from jattmail import JattMail

def main() -> int:
    smtp = JattMail(5, "127.0.0.1")
    smtp.run()

if __name__ == "__main__":
    exit(main())