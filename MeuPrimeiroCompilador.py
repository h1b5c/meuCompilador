#==================
#OI FIFLIPE
#==================

programa = open("programa.txt", "r")

transicoes = {
        ("S0", "A"): "S1",
        ("S0", "B"): "S8",
        ("S0", "C"): "S13",
        ("S0", "D"): "S21",
        ("S0", "E"): "S29",
        ("S0", "F"): "S35",
        ("S0", "G"): "S48",
        ("S0", "I"): "S52",
        ("S0", "L"): "S55",
        ("S0", "M"): "S60",
        ("S0", "N"): "S63",
        ("S0", "O"): "S68",
        ("S0", "P"): "S71",
        ("S0", "R"): "S89",
        ("S0", "S"): "S99",
        ("S0", "T"): "S102",
        ("S0", "U"): "S110",
        ("S0", "V"): "S115",
        ("S0", "W"): "S118",

        # =========================
        # A
        # =========================

        # AND
        ("S1", "N"): "S2",
        ("S2", "D"): "S3",

        # ARRAY
        ("S1", "R"): "S4",
        ("S4", "R"): "S5",
        ("S5", "A"): "S6",
        ("S6", "Y"): "S7",


        # =========================
        # BEGIN
        # =========================

        ("S8", "E"): "S9",
        ("S9", "G"): "S10",
        ("S10", "I"): "S11",
        ("S11", "N"): "S12",


        # =========================
        # CASE / CONST
        # =========================

        # CASE
        ("S13", "A"): "S14",
        ("S14", "S"): "S15",
        ("S15", "E"): "S16",

        # CONST
        ("S13", "O"): "S17",
        ("S17", "N"): "S18",
        ("S18", "S"): "S19",
        ("S19", "T"): "S20",


        # =========================
        # DIV / DO / DOWNTO
        # =========================

        # DIV
        ("S21", "I"): "S22",
        ("S22", "V"): "S23",

        # DO
        ("S21", "O"): "S24",

        # DOWNTO
        ("S24", "W"): "S25",
        ("S25", "N"): "S26",
        ("S26", "T"): "S27",
        ("S27", "O"): "S28",


        # =========================
        # ELSE / END
        # =========================

        # ELSE
        ("S29", "L"): "S30",
        ("S30", "S"): "S31",
        ("S31", "E"): "S32",

        # END
        ("S29", "N"): "S33",
        ("S33", "D"): "S34",


        # =========================
        # FILE / FOR / FUNCTION
        # =========================

        # FILE
        ("S35", "I"): "S36",
        ("S36", "L"): "S37",
        ("S37", "E"): "S38",

        # FOR
        ("S35", "O"): "S39",
        ("S39", "R"): "S40",

        # FUNCTION
        ("S35", "U"): "S41",
        ("S41", "N"): "S42",
        ("S42", "C"): "S43",
        ("S43", "T"): "S44",
        ("S44", "I"): "S45",
        ("S45", "O"): "S46",
        ("S46", "N"): "S47",


        # =========================
        # GOTO
        # =========================

        ("S48", "O"): "S49",
        ("S49", "T"): "S50",
        ("S50", "O"): "S51",


        # =========================
        # IF / IN
        # =========================

        # IF
        ("S52", "F"): "S53",

        # IN
        ("S52", "N"): "S54",


        # =========================
        # LABEL
        # =========================

        ("S55", "A"): "S56",
        ("S56", "B"): "S57",
        ("S57", "E"): "S58",
        ("S58", "L"): "S59",


        # =========================
        # MOD
        # =========================

        ("S60", "O"): "S61",
        ("S61", "D"): "S62",


        # =========================
        # NIL / NOT
        # =========================

        # NIL
        ("S63", "I"): "S64",
        ("S64", "L"): "S65",

        # NOT
        ("S63", "O"): "S66",
        ("S66", "T"): "S67",


        # =========================
        # OF / OR
        # =========================

        # OF
        ("S68", "F"): "S69",

        # OR
        ("S68", "R"): "S70",


        # =========================
        # PACKED / PROCEDURE / PROGRAM
        # =========================

        # P
        ("S71", "A"): "S72",
        ("S71", "R"): "S77",

        # PACKED
        ("S72", "C"): "S73",
        ("S73", "K"): "S74",
        ("S74", "E"): "S75",
        ("S75", "D"): "S76",

        # PROCEDURE
        ("S77", "O"): "S78",
        ("S78", "C"): "S79",
        ("S79", "E"): "S80",
        ("S80", "D"): "S81",
        ("S81", "U"): "S82",
        ("S82", "R"): "S83",
        ("S83", "E"): "S84",

        # PROGRAM
        ("S78", "G"): "S85",
        ("S85", "R"): "S86",
        ("S86", "A"): "S87",
        ("S87", "M"): "S88",


        # =========================
        # RECORD / REPEAT
        # =========================

        # R
        ("S89", "E"): "S90",

        # RECORD
        ("S90", "C"): "S91",
        ("S91", "O"): "S92",
        ("S92", "R"): "S93",
        ("S93", "D"): "S94",

        # REPEAT
        ("S90", "P"): "S95",
        ("S95", "E"): "S96",
        ("S96", "A"): "S97",
        ("S97", "T"): "S98",


        # =========================
        # SET
        # =========================

        ("S99", "E"): "S100",
        ("S100", "T"): "S101",


        # =========================
        # THEN / TO / TYPE
        # =========================

        # T
        ("S102", "H"): "S103",
        ("S102", "O"): "S106",
        ("S102", "Y"): "S107",

        # THEN
        ("S103", "E"): "S104",
        ("S104", "N"): "S105",

        # TO
        # S106 já é final

        # TYPE
        ("S107", "P"): "S108",
        ("S108", "E"): "S109",


        # =========================
        # UNTIL
        # =========================

        ("S110", "N"): "S111",
        ("S111", "T"): "S112",
        ("S112", "I"): "S113",
        ("S113", "L"): "S114",


        # =========================
        # VAR
        # =========================

        ("S115", "A"): "S116",
        ("S116", "R"): "S117",


        # =========================
        # WHILE / WITH
        # =========================

        # W
        ("S118", "H"): "S119",
        ("S118", "I"): "S123",

        # WHILE
        ("S119", "I"): "S120",
        ("S120", "L"): "S121",
        ("S121", "E"): "S122",

        # WITH
        ("S123", "T"): "S124",
        ("S124", "H"): "S125",
        
        # ==========================================
        # PONTUAÇÃO
        # ==========================================

        # ,
        ("S0", ","): "S126",

        # ;
        ("S0", ";"): "S127",

        # :
        ("S0", ":"): "S128",

        # := 
        ("S128", "="): "S129",

        # ^
        ("S0", "^"): "S130",

        # (
        ("S0", "("): "S131",

        # )
        ("S0", ")"): "S132",

        # .
        ("S0", "."): "S133",

        # ..
        ("S133", "."): "S134",

        # [
        ("S0", "["): "S135",

        # ]
        ("S0", "]"): "S136",

        # {
        ("S0", "{"): "S137",

        # }
        ("S0", "}"): "S138",


        # ==========================================
        # OPERADORES ARITMÉTICOS
        # ==========================================

        # +
        ("S0", "+"): "S139",

        # -
        ("S0", "-"): "S140",

        # *
        ("S0", "*"): "S141",

        # /
        ("S0", "/"): "S142",


        # ==========================================
        # OPERADORES RELACIONAIS
        # ==========================================

        # =
        ("S0", "="): "S143",

        # >
        ("S0", ">"): "S144",

        # >=
        ("S144", "="): "S145",

        # <
        ("S0", "<"): "S146",

        # <=
        ("S146", "="): "S147",

        # <>
        ("S146", ">"): "S148",
}

estados_finais = {
        # =========================
        # PALAVRAS RESERVADAS
        # =========================

        "S3": "AND",
        "S7": "ARRAY",
        "S12": "BEGIN",
        "S16": "CASE",
        "S20": "CONST",
        "S23": "DIV",
        "S24": "DO",
        "S28": "DOWNTO",
        "S32": "ELSE",
        "S34": "END",
        "S38": "FILE",
        "S40": "FOR",
        "S47": "FUNCTION",
        "S51": "GOTO",
        "S53": "IF",
        "S54": "IN",
        "S59": "LABEL",
        "S62": "MOD",
        "S65": "NIL",
        "S67": "NOT",
        "S69": "OF",
        "S70": "OR",
        "S76": "PACKED",
        "S84": "PROCEDURE",
        "S88": "PROGRAM",
        "S94": "RECORD",
        "S98": "REPEAT",
        "S101": "SET",
        "S105": "THEN",
        "S106": "TO",
        "S109": "TYPE",
        "S114": "UNTIL",
        "S117": "VAR",
        "S122": "WHILE",
        "S125": "WITH",


        # =========================
        # PONTUAÇÃO
        # =========================

        "S126": ",",
        "S127": ";",
        "S128": ":",

        # atribuição
        "S129": ":=",

        "S130": "^",
        "S131": "(",
        "S132": ")",

        # ponto
        "S133": ".",

        # intervalo
        "S134": "..",

        "S135": "[",
        "S136": "]",
        "S137": "{",
        "S138": "}",


        # =========================
        # ARITMÉTICOS
        # =========================

        "S139": "+",
        "S140": "-",
        "S141": "*",
        "S142": "/",


        # =========================
        # RELACIONAIS
        # =========================

        "S143": "=",
        "S144": ">",
        "S145": ">=",
        "S146": "<",
        "S147": "<=",
        "S148": "<>",
}

Tabela = {
        "palavra": [],
        "linha": [],
        "classe": [],
}

def adicionar_tabela(palavra, linha, classe):
    Tabela["palavra"].append(palavra)
    Tabela["linha"].append(linha)
    Tabela["classe"].append(classe)

def classificar_palavra(palavra):
        # PONTUAÇÃO
        if palavra in [",", ";", ":", "(", ")", ".", "..", "[", "]", "{", "}"]:
                return "P"

        # ATRIBUIÇÃO
        if palavra == ":=":
                return "A"

        # SÍMBOLOS
        if palavra in ["^", "+", "-", "*", "/", "=", ">", ">=", "<", "<=", "<>"]:
                return "S"

        retorno = "V"

        # NÚMERO
        if palavra[0] in "0123456789":
                retorno = "N"

                for caractere in palavra:
                        if caractere not in "0123456789":
                                retorno = "E"

        else:
                estado = "S0"

                for caractere in palavra:

                        if (estado, caractere) in transicoes:
                                estado = transicoes[(estado, caractere)]

                        else:
                                # verifica se ainda pode ser variável
                                for letra in palavra:
                                        if letra not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                                                retorno = "E"
                                break

                if estado in estados_finais:
                        retorno = "R"

        return retorno

def separar_tokens(linha):

        tokens = []
        palavra = ""
        i = 0

        while i < len(linha):

                caractere = linha[i]

                # Espaço, tab ou quebra de linha
                if caractere == " " or caractere == "\t" or caractere == "\n":

                        if palavra != "":
                                tokens.append(palavra)
                                palavra = ""

                # Verifica símbolos com dois caracteres
                elif caractere == ":":

                        if palavra != "":
                                tokens.append(palavra)
                                palavra = ""

                        if i + 1 < len(linha) and linha[i + 1] == "=":
                                tokens.append(":=")
                                i += 1
                        else:
                                tokens.append(":")

                elif caractere == "<":

                        if palavra != "":
                                tokens.append(palavra)
                                palavra = ""

                        if i + 1 < len(linha):
                                if linha[i + 1] == "=":
                                        tokens.append("<=")
                                        i += 1

                                elif linha[i + 1] == ">":
                                        tokens.append("<>")
                                        i += 1

                                else:
                                        tokens.append("<")
                        else:
                                tokens.append("<")

                elif caractere == ">":

                        if palavra != "":
                                tokens.append(palavra)
                                palavra = ""

                        if i + 1 < len(linha) and linha[i + 1] == "=":
                                tokens.append(">=")
                                i += 1
                        else:
                                tokens.append(">")

                elif caractere == ".":

                        if palavra != "":
                                tokens.append(palavra)
                                palavra = ""

                        if i + 1 < len(linha) and linha[i + 1] == ".":
                                tokens.append("..")
                                i += 1
                        else:
                                tokens.append(".")

                # Símbolos de um caractere
                elif caractere in ",;^()[]{}+-*/=":

                        if palavra != "":
                                tokens.append(palavra)
                                palavra = ""

                        tokens.append(caractere)

                else:

                        palavra += caractere

                i += 1

        # Se terminou a linha e ainda existe uma palavra
        if palavra != "":
                tokens.append(palavra)
        return tokens

cont = 1

for linha in programa.readlines():
        linha = linha.upper()

        tokens = separar_tokens(linha)

        for palavra in tokens:

                classe = classificar_palavra(palavra)

                adicionar_tabela(palavra, cont, classe)

        cont += 1

cabecalho = ("Palavra", "Linha", "Classe")
print(f"{'%-28s' % cabecalho[0]} {'%-8s' % cabecalho[1]} {'%5s' % cabecalho[2]}")
for i in range(len(Tabela["palavra"])):
    print(f"{'%-30s' % Tabela['palavra'][i]} {'%-5s' %Tabela['linha'][i]} {'%5s' %Tabela['classe'][i]}")
programa.close()