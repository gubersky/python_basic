def update_hero(hero="", power=0, alive="", speed=0, x=0.0, y=0.0):
    import configparser
    config = configparser.ConfigParser()
    config.read("hero.ini")
    if hero.isalpha():
        config.set("parameters", "hero", hero)
    if power != 0:
        config.set("parameters", "power", str(power))
    if alive.isalpha():
        config.set("parameters", "alive", alive)
    if speed != 0:
        config.set("parameters", "speed", str(speed))
    if x != 0.0:
        config.set("parameters", "x", str(x))
    if y != 0.0:
        config.set("parameters", "y", str(y))
    with open("hero.ini", "w") as configfile:
        config.write(configfile)


if __name__ == '__main__':
    update_hero(hero="Super-Man", power=480, y=2.0)
