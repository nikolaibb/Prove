def fravær(udokumentert_fravær: float, dokumentert_fravær: float, årstimer: int) -> str:
    """
    Evaluerer fraværsprosenten og returnerer en melding basert på reglene.

    Argumenter:
        udokumentert_fravær (float): Andel udokumentert fravær i prosent.
        dokumentert_fravær (float): Andel dokumentert fravær i prosent.
        årstimer (int): Totalt antall årstimer.

    Returns:
        str: En melding om fraværssituasjonen.
    """

    udokumentert_fravær_prosent = (udokumentert_fravær / årstimer) * 100
    dokumentert_fravær_prosent = (dokumentert_fravær / årstimer) * 100

    if udokumentert_fravær_prosent >= 10.0 and udokumentert_fravær_prosent < 20.0:
        return "Mister karakteren i faget"
    elif udokumentert_fravær_prosent >= 5.0 and udokumentert_fravær_prosent < 10.0:
        return "Send varsel om fare for å miste karakteren grunnet fravær"
    elif dokumentert_fravær_prosent >= 20.0:
        return "Send varsel om fare for å miste karakteren grunnet manglende vurderingsgrunnlag"
    else:
        return ""
    


print(fravær(10.0, 0.0, 100)) # Mister karakteren i faget
print(fravær(8.0, 0.0, 100)) # Send varsel om fare for å miste karakteren grunnet fravær
print(fravær(0.0, 25.0, 100)) # Send varsel om fare for å miste karakteren grunnet manglende vurderingsgrunnlag