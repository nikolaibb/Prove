def meter_per_sekund_til_baufort(mps: float) -> str:
    """
    endre hvor raskt det går i mps (meter per sekund) til Baufort-Skalaen.

    Args:
        mps (float): Hvor raskt det går, (meter per sekund.)

    Returns:
        str: Betegnelsen på Baufort-skalaen.
    """
    if mps < 0.2:
        return "Stille"
    elif mps < 1.5:
        return "Flau vind"
    elif mps < 3.3:
        return "Svak vind"
    elif mps < 5.4:
        return "Lett bris"
    elif mps < 7.9:
        return "Laber bris"
    elif mps < 10.7:
        return "Frisk bris"
    elif mps < 13.8:
        return "Liten kuling"
    elif mps < 17.1:
        return "Stiv kuling"
    elif mps < 20.7:
        return "Sterk kuling"
    elif mps < 24.4:
        return "Liten storm"
    elif mps < 28.4:
        return "Full Storm"
    elif mps < 32.6:
        return "Sterk Storm"
    else:
        return "Orkan"

print(meter_per_sekund_til_baufort(10))
print(meter_per_sekund_til_baufort(28.1))
print(meter_per_sekund_til_baufort(201))