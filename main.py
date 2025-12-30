import argparse

from generator import generate_password
from analyzer import analyze_password
from storage import save_analysis,load_history

def main():
    parser=argparse.ArgumentParser(
        description="Generator si analizator de parole securizate"
    )

    parser.add_argument("--length",type=int,help="Lunginea parolei")
    parser.add_argument("--upper",action="store_true",help="Incude litere mari")
    parser.add_argument("--digits",action="store_true",help="Include cifre")
    parser.add_argument("--special",action="store_true",help="Include caractere speciale")

    parser.add_argument("--check",type=str,help="Analizeaza o parola existenta")

    parser.add_argument(
        "--history",
        choices=["view"],
        help="Afisaza istoricul puterilor"
    )

    args=parser.parse_args()

    if args.history=="view":
       history=load_history()
      
       if not history:
            print("Istoric gol.")
            return
       
       print("Istoric parole:")
       print("-" * 30)

       for entry in history:
        print(f'Data: {entry["date"]}')
        print(f'Entropie: {entry["entropy"]}')
        print(f'Putere: {entry["strength"]} ({entry["score"]}/100)')
        print(f'Hash: {entry["hash"]}')
        print("-" * 30)
       return 

    if args.check:
        result=analyze_password(args.check)

        print(f'Analiza parolei "{args.check}":')
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
    
    if args.length:
        password=generate_password(
           length=args.length,
           use_lower=True,
           use_upper=args.upper,
           use_digits=args.digits,
           use_special=args.special
        ) 

        result=analyze_password(password)

        print("Parola generata:", password)
        print(f'Putere: {result["strength"]}')
        print(f'Entropie: {result["entropy"]}')
        print("Salvata in istoric")

        save_analysis(result)

if __name__=="__main__":
    main()  