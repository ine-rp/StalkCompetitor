from stalkcompetitor.crew import build_crew

def main():
    company = input("Enter competitor name: ")
    crew = build_crew()
    result = crew.kickoff(inputs={"company_name": company})
    print("\nFinal Report:\n")
    print(result)

if __name__ == "__main__":
    main()
