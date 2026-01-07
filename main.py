import argparse

from generator import generate_password,generate_memorable_password
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
    parser.add_argument("--history",choices=["view"],help="Vezi istoricul parolelor")

    parser.add_argument("--batch", type=int, help="Genereaza mai multe parole deodata")

    parser.add_argument("--memorable",action="store_true",help="Genereaza parola usor de retinut")
    parser.add_argument("--words",type=int,help="Numar de cuvinte pentru parola memorabila")

    args=parser.parse_args()

    if args.history=="view":
       history=load_history()
       for entry in history:
           print(entry)
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
    
    if args.memorable:
        num_words=args.words if args.words else 3
        password=generate_memorable_password(words=num_words)
        result=analyze_password(password)   

        print("Parola memorabila generata:",password)
        print(f'Putere: {result["strength"]}')
        print(f'Entropie: {result["entropy"]}')
        print("Salvata in istoric")

        save_analysis(result)
        return 
    
    if args.batch:
        for i in range(args.batch):
            password=generate_password(
                length=args.length,
                use_lower=True,
                use_upper=args.upper,
                use_digits=args.digits,
                use_special=args.special
            )
            result=analyze_password(password)

            print(f"\nParola {i+1}:{password}")
            print("Putere:",result["strength"])
            print("Entropie:",result["entropy"])

            save_analysis(result)
        print("\nToate parolele au fost salvate in istoric")
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