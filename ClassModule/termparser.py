from argparse import ArgumentParser

parser = ArgumentParser()
subparsers = parser.add_subparsers()

calc = subparsers.add_parser('calc')
calc.add_argument('--municipio', '-m', action='store_true', help='Fazer conta do limiar por cada município')
calc.add_argument('--bairro', '-b', action='store_true', help='Fazer conta do limiar por cada Estacão/Bairro')
calc.add_argument('--arquivo_saida', '-as', type=str, help='Seleciona o arquivo de saída', required=True)
calc.add_argument('--limiarA', '-lA', type=int,help='Define o limiar A', required=True)
calc.add_argument('--limiarB', '-lB', type=int,help='Define o limiar B', required=True)
calc.set_defaults(subparser='calc')

args = parser.parse_args()

def verify():
    if args.subparser == "calc":
        return True
    else:
        return False

def get_args():
    return {
        "lA": args.limiarA,
        "lB": args.limiarB,
        "outfile": args.arquivo_saida,
        "bairro": args.bairro,
        "municipio": args.municipio
    }