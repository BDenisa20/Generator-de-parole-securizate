import argparse

from generator import generate_password
from analyzer import analyze_password
from storage import save_analysis

def main():
    parser=argparse.ArgumentParser(
        description="Generator si analizator de parole securizate"
    )
    
    parser.add_argument("--length",type=int,help="Lunginea parolei")
    parser.add_argument("--upper",action="store_true",help="Incude litere mari")
    parser.add_argument("--digits",action="store_true",help="Include cifre")
    parser.add_argument("--special",action="store_true",help="Include caractere speciale")

    parser.add_argument("--check",type=str,help="Analizeaza o parola existenta")

    args=parser.parse_args()
    if args.check:
        result=analyze_password(args.check)

        print(f'Analiza parolei "{args.check}:')
        print(f'Putere: {result["strength"]}({result["score"]}/100)')
        print("Probleme: ")
        for p in result["problems"]:
            print(f"- {p}")
        
        if result["suggestions"]:
            print("Sugestii:")
            for s in result["suggestions"]:
               print(f"- {s}") 

        save_analysis(result)
        return
    