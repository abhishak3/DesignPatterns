from singleton import Singleton

def main() -> None:
    s1 = Singleton()
    s2 = Singleton()

    s1.set("mode", "production")

    print("Same instance:", s1 is s2)
    print("Value from s2:", s2.get("mode"))


if __name__ == "__main__":
    main()
