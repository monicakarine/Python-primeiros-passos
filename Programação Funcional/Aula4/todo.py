
def lastNames(L):
    """Mapeia uma lista de nomes para o ultimo nome de cada item.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    Entao lastNames(L) == ['Franco', 'Vitelus', 'Buarque']
    """

    return list(map( lambda x: x[-1], L))


def citations(L):
    """Mapeia uma lista de nomes para a primeira letra mais sobrenome.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
    Note que a primeira letra precisa estar capitalizada.
    """
    return list(map(lambda x: x[0][0].capitalize() + ". " + x[-1], L))
    
def fullCitations(L):
    """Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
    Por exemplo, seja:
    L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
    entao fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
    Note que as iniciais precisam estar capitalizada.
    """
    def construirACitacao(nameList):

        lastName = nameList[-1]# Leia o ultimo nome em nameList
        firstNames = nameList[:-1]# Remove o ultimo nome de nameList
        initials = map(lambda x: x[0][0].capitalize(), firstNames)# Mapeia cada nome em firstNames para sua inicial maiuscula

        return '. '.join(initials) + ". " + lastName 

    return list(map(construirACitacao, L))

L = [['Artur', 'Alberto', 'Vaz'], ['Micaelis','Aubertendraub', 'Witzengarten']]
print(citations(L))
print(fullCitations(L))

